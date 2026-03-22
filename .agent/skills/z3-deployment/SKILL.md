---
name: z3-deployment
description: Use when preparing Z3Connect for production deployment.
---

# Z3Connect Deployment

## Build Steps
1. Minify HTML, CSS, JS
2. Optimize all images (WebP, compressed)
3. Check all links (no broken hrefs)
4. Zero console errors

## Deploy Targets
- Cloudflare Pages or Netlify (static hosting)
- Custom domain: z3connect.com

## Security Headers
- `Content-Security-Policy` — restrict sources
- `Strict-Transport-Security` — HSTS max-age 31536000
- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`

## Cache Strategy
- HTML: `no-cache` (always fresh)
- CSS/JS with hashed filenames: `immutable, max-age=31536000`
- Images: `max-age=604800` (1 week)

## Pre-Launch Checklist
- [ ] Favicon set (ico + apple-touch-icon)
- [ ] 404 page works
- [ ] `<meta name="theme-color">` set
- [ ] WhatsApp button functional
- [ ] Mobile test on real Android device
- [ ] Lighthouse 90+ on all pages
- [ ] Structured data validates (Google Rich Results Test)
- [ ] robots.txt allows crawling
- [ ] sitemap.xml submitted
