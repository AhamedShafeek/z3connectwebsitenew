---
name: z3-animation
description: Use when adding animations, scroll effects, or motion to Z3Connect pages. Contains all timing, easing, AOS/Lenis config, and accessibility rules.
---

# Z3Connect Animation System

## Libraries
- **AOS.js v2** — scroll reveal animations
- **Lenis** — smooth scroll (duration 1.2)

## Animation Table
| Element | Animation | Trigger | Duration | Easing |
|---------|-----------|---------|----------|--------|
| Headings | translateY(40px)→0 + blur(8px)→0 | scroll | 0.8s | cubic-bezier(0.16,1,0.3,1) |
| Cards | staggered translateY(30px)→0 + opacity | scroll | 0.6s, 100ms stagger | cubic-bezier(0.16,1,0.3,1) |
| Stats | count up from 0 | scroll trigger | 2s | ease-out |
| Images | parallax 20% slower | continuous | — | — |
| CTAs | scale(0.95)→1 + opacity | scroll | 0.6s | cubic-bezier(0.16,1,0.3,1) |
| Nav | slide down on scroll up, hide on down | scroll direction | 0.3s | cubic-bezier(0.16,1,0.3,1) |
| Quote | word-by-word reveal | scroll progress | 0.05s per word | ease |
| Timeline | line draws left→right | scroll progress | continuous | — |
| Hovers | translateY(-8px) + shadow | hover | 0.3s | cubic-bezier(0.16,1,0.3,1) |
| Hero | staggered entrance | page load | 0.0s–3.5s | cubic-bezier(0.16,1,0.3,1) |
| Logo marquee | infinite scroll | auto | 30s loop | linear (exception) |
| Industry hover | bg/text inversion | hover | 0.3s | ease |

## Rules
1. Reveals: 0.6-0.8s duration
2. Hovers: 0.3s duration
3. Easing: `cubic-bezier(0.16, 1, 0.3, 1)` — NEVER `linear` (except marquee)
4. Max 3 CSS properties animated simultaneously
5. ALWAYS respect `prefers-reduced-motion` — disable all non-essential motion
6. Only animate `transform` and `opacity` for performance (GPU compositing)

## Lenis Config
```js
const lenis = new Lenis({ duration: 1.2 });
```

## Scroll Progress Bar
- 2px white line at very top of viewport
- Width = scroll percentage
- `position: fixed; top: 0; z-index: 9999`
