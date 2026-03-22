---
name: z3-seo-performance
description: Use when optimizing Z3Connect for SEO, performance, or Core Web Vitals.
---

# Z3Connect SEO & Performance

## Performance Targets
- FCP < 1.5s, LCP < 2.5s, INP < 200ms, CLS < 0.1
- Total page weight < 500KB
- Lighthouse score 90+

## Meta Tags (every page)
- `<title>` — unique, descriptive, under 60 chars
- `<meta name="description">` — unique, compelling, under 160 chars
- `<link rel="canonical">` — self-referencing
- Open Graph: og:title, og:description, og:image, og:url, og:type
- Twitter Cards: twitter:card, twitter:title, twitter:description, twitter:image

## Structured Data
- Organization JSON-LD (name, url, logo, contactPoint)
- LocalBusiness JSON-LD (Nagercoil, Tamil Nadu, IN)

## Image Optimization
- WebP format preferred
- Lazy loading: `loading="lazy"` on below-fold images
- `srcset` for responsive images
- Always include `alt` text
- Explicit `width` and `height` attributes to prevent CLS

## Font Loading
- `<link rel="preconnect">` for font CDNs
- `font-display: swap` on all font imports

## Build
- Minify HTML, CSS, JS for production
- Inline critical CSS in `<head>`
- Generate `sitemap.xml` and `robots.txt`
