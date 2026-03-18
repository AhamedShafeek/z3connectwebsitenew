---
name: z3-design-system
description: Use when building or styling any Z3Connect page. Contains the complete design token system — colors, typography, spacing, glass effects, card patterns, and section transitions for the black-white-black theme.
---

# Z3Connect Design System

## CSS Custom Properties — ON BLACK SECTIONS
```css
.section-dark {
  --bg: #000000;
  --text-primary: #FFFFFF;
  --text-secondary: rgba(255,255,255,0.6);
  --text-muted: rgba(255,255,255,0.35);
  --accent: #FFFFFF;
  --border: rgba(255,255,255,0.08);
  --glass-bg: rgba(255,255,255,0.04);
  --glass-hover: rgba(255,255,255,0.08);
  --glow: rgba(59,130,246,0.15);
}
```

## CSS Custom Properties — ON WHITE SECTIONS
```css
.section-light {
  --bg: #FFFFFF;
  --text-primary: #0A0A0A;
  --text-secondary: #555555;
  --text-muted: #999999;
  --accent: #0A0A0A;
  --border: #EBEBEB;
  --card-bg: #FAFAFA;
  --card-shadow: 0 1px 3px rgba(0,0,0,0.04);
  --card-hover-shadow: 0 8px 30px rgba(0,0,0,0.08);
}
```

## Brand Accent (use sparingly)
- `--primary-blue: #2563EB` — links and primary CTAs only
- `--success-green: #22C55E` — success states only

## Typography Scale
| Role | Font | Weight | Size |
|------|------|--------|------|
| Display headings | Clash Display | 600-700 | 4rem-8rem desktop |
| Body text | Satoshi / General Sans | 400-500 | 1rem-1.125rem |
| Accent labels | Satoshi | 500, uppercase, tracked | 0.75rem |
| Code/numbers | JetBrains Mono / Space Mono | 400 | inherit |

## Spacing Scale
4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px, 192px

## Glass Morphism Recipe
```css
/* Dark variant */
.glass-dark {
  backdrop-filter: blur(20px);
  background: rgba(0,0,0,0.5);
  border-radius: 9999px; /* pill */ or 16px; /* cards */
  border: 1px solid rgba(255,255,255,0.08);
}

/* Light variant */
.glass-light {
  backdrop-filter: blur(20px);
  background: rgba(255,255,255,0.8);
  border-radius: 9999px;
  border: 1px solid #EBEBEB;
}
```

## Card Patterns
**White section cards:**
- bg: #FAFAFA
- border: 1px solid #f0f0f0
- shadow: 0 1px 3px rgba(0,0,0,0.06)
- hover: translateY(-8px) + shadow 0 8px 30px rgba(0,0,0,0.08)

**Black section cards:**
- Glass morphism: rgba(255,255,255,0.04) bg
- border: rgba(255,255,255,0.08)
- hover: animated gradient border

## Section Transitions (black ↔ white)
1. **Gradient fade**: 100px gradient from black to white at section boundaries
2. **Diagonal clip-path**: `polygon(0 0, 100% 5%, 100% 100%, 0 95%)`
3. **SVG wave divider**: subtle, minimal wave
4. **Fade-through-gray**: #000 → #111 → #333 → #888 → #ccc → #fff over 200px
