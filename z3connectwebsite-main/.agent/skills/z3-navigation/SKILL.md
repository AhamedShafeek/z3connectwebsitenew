---
name: z3-navigation
description: Use when building or modifying the Z3Connect navigation. Contains the floating glass pill nav, scroll behavior, mobile menu, and context-aware theme switching.
---

# Z3Connect Navigation

## Desktop Nav
- Links: Z3Connect logo + About, Products, Work, Contact + `[Get Quote]` button
- Glass pill: `backdrop-filter: blur(20px)`, `rgba(0,0,0,0.5)`, `border-radius: 9999px`, `border: 1px solid rgba(255,255,255,0.08)`
- Hidden at page top, appears after 100px scroll
- Fixed position, horizontally centered, high z-index (9999)
- Sentence case links (never uppercase)
- `[Get Quote]` is the only solid button (white bg, black text)

## Context-Aware Theme Switching
- Dark glass on black sections: `rgba(0,0,0,0.5)` bg, white text
- Light glass on white sections: `rgba(255,255,255,0.8)` bg, black text, `border: 1px solid #EBEBEB`
- Use IntersectionObserver to detect which section is at nav position
- Transition between themes: 0.3s ease

## Scroll Behavior
- Slides down on scroll UP (user scrolling back)
- Hides on scroll DOWN (user reading content)
- Transition: `transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)`

## Mobile Nav
- Hamburger button (3 lines) replaces desktop nav
- Opens full-screen black overlay (`rgba(0,0,0,0.95)`, `backdrop-filter: blur(10px)`)
- Large centered links with staggered fade-in (100ms delay each)
- Close button as X in top-right
- Body scroll locked when open
