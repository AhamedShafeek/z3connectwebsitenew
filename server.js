const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const path = require('path');

const app = express();
const PORT = 3000;
const VITE_PORT = 5173;

// 1. Define React-specific routes and Vite internal paths
const isViteAsset = (url) => {
  return url.startsWith('/src') || 
         url.startsWith('/@vite') || 
         url.startsWith('/@id') || 
         url.startsWith('/@fs') || 
         url.startsWith('/node_modules') || 
         url.startsWith('/__vite') ||
         url.includes('.jsx') || 
         url.includes('.tsx') ||
         url.includes('?v=');
};

const isReactRoute = (url) => {
  const routes = ['/blogs', '/contact', '/admin', '/blog'];
  return routes.some(route => url.startsWith(route));
};

// 2. Comprehensive Proxy for Vite
// This captures BOTH React entry points and all internal Vite modules
app.use((req, res, next) => {
  if (isViteAsset(req.url) || isReactRoute(req.url)) {
    return createProxyMiddleware({
      target: `http://127.0.0.1:${VITE_PORT}`,
      changeOrigin: true,
      secure: false, // For local self-signed
      ws: true, // Crucial for HMR (Hot Module Replacement)
      logLevel: 'debug', // Helpful for initial debugging
      xfwd: true, // Crucial for Vite's module resolution
      onError: (err, req, res) => {
        console.error('Proxy Error:', err);
        res.status(500).send('Proxy to Vite failed. Is the React dev server running on ' + VITE_PORT + '?');
      }
    })(req, res, next);
  }
  next();
});

// 3. Serve static HTML and assets from the root
app.use(express.static(__dirname));

// 4. Handle clean URLs for static pages (e.g., /about -> about.html)
app.get('/:page', (req, res, next) => {
  const page = req.params.page;
  if (!page.includes('.')) {
    const fullPath = path.join(__dirname, `${page}.html`);
    res.sendFile(fullPath, (err) => {
      if (err) next();
    });
  } else {
    next();
  }
});

// 5. Default route to index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`\x1b[36m%s\x1b[0m`, `--------------------------------------------------`);
  console.log(`\x1b[32m%s\x1b[0m`, `Z3Connect UNIFIED SERVER (Hybrid Architecture)`);
  console.log(`\x1b[36m%s\x1b[0m`, `--------------------------------------------------`);
  console.log(`Main Hub:    http://localhost:${PORT}`);
  console.log(`React Proxy: http://localhost:${VITE_PORT}`);
  console.log(`Static Root: ${__dirname}`);
  console.log(`\x1b[36m%s\x1b[0m`, `--------------------------------------------------`);
  console.log(`Directly open http://localhost:${PORT} to see the full site.`);
});
