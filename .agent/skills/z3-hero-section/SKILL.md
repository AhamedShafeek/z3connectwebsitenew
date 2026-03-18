---
name: z3-hero-section
description: Use when building or modifying the hero section of any Z3Connect page. Contains the cinematic hero design with animation choreography, typography, and layout specifications.
---

# Z3Connect Hero Section

## Layout
- Full viewport `100vh`, content vertically and horizontally centered
- Background: Pure black `#000` with single subtle radial gradient glow in deep blue `#0a1628` behind text
- Overlay: Very faint grid pattern at `opacity: 0.03` for texture

## Content Stack (centered)
1. Navigation fades in first
2. Headline: **"We build software that runs businesses."** — Clash Display, 7-10rem desktop, 2.5rem mobile
3. Subtitle typewriter: "AI-driven tools for businesses that actually work"
4. Two CTAs: `[See Our Work]` outlined ghost + `[Get a Quote]` filled white
5. Stats: "30+ Clients · 50+ Projects · 15 Industries" — counter animation
6. Scroll indicator: pulsing down arrow

## Animation Choreography
| Time | Element | Animation |
|------|---------|-----------|
| 0.0s | Screen | Black |
| 0.3s | Nav | Fade in opacity 0→1 |
| 0.5s | Line 1 | Slide up + deblur: translateY(40px)→0, blur(8px)→0 |
| 0.8s | Line 2 | Slide up + deblur |
| 1.1s | Subtitle | Types character by character |
| 1.5s | CTAs | Fade in scale(0.95)→1 |
| 2.2s | Stats | Counter begins (0 → target) |
| 2.8s | Scroll arrow | Pulse begins |

## Mobile Adjustments
- Hero text: 2.5rem
- Reduced animations (no blur, simpler entrances)
- Single column layout
- Stats wrap to 2 rows
