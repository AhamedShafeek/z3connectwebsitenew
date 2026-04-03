"""
Phase 2 SEO Fixer: Targeted fixes for canonicals, unsafe external links,
broken internal links, and image compression reporting.
"""
import os
import re
from bs4 import BeautifulSoup

SITE_URL = "https://z3connect.com"

# Map file -> canonical URL (no .html for clean URLs, except where needed)
CANONICAL_MAP = {
    "index.html":                "https://z3connect.com/",
    "about.html":                "https://z3connect.com/about",
    "team.html":                 "https://z3connect.com/team",
    "founder.html":              "https://z3connect.com/founder",
    "philosophy.html":           "https://z3connect.com/philosophy",
    "why-we-exist.html":         "https://z3connect.com/why-we-exist",
    "products.html":             "https://z3connect.com/products",
    "solutions-detailed.html":   "https://z3connect.com/solutions",
    "work.html":                 "https://z3connect.com/work",
    "case-studies.html":         "https://z3connect.com/case-studies",
    "clients.html":              "https://z3connect.com/clients",
    "blogs.html":                "https://z3connect.com/blogs",
    "contact.html":              "https://z3connect.com/contact",
    "get-quote.html":            "https://z3connect.com/get-quote",
    "portfolio.html":            "https://z3connect.com/portfolio",
    "privacy-policy.html":       "https://z3connect.com/privacy-policy",
    "terms.html":                "https://z3connect.com/terms",
    "404.html":                  "https://z3connect.com/404",
}

SKIP_FILES = {"cards-partial.html", "cards_partial.html"}

modified_files = []

for filename in os.listdir("."):
    if not filename.endswith(".html"):
        continue
    if filename in SKIP_FILES or "demo" in filename or "animation" in filename:
        continue

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    changed = False

    # ── 1. Fix canonical tag ─────────────────────────────────────────────────
    canon = soup.find("link", rel="canonical")
    if canon and filename in CANONICAL_MAP:
        correct_url = CANONICAL_MAP[filename]
        # Case studies subpages — keep their own canonical
        if filename.startswith("case-study-") and not canon.get("href", "").startswith(SITE_URL + "/case-study"):
            canon["href"] = SITE_URL + "/" + filename.replace(".html", "")
            changed = True
        elif canon.get("href") != correct_url:
            canon["href"] = correct_url
            changed = True

    # ── 2. Fix target="_blank" without rel="noopener noreferrer" ─────────────
    for a in soup.find_all("a", target="_blank"):
        rel_val = a.get("rel", [])
        if isinstance(rel_val, str):
            rel_val = rel_val.split()
        needs_noopener = "noopener" not in rel_val
        needs_noreferrer = "noreferrer" not in rel_val
        if needs_noopener or needs_noreferrer:
            if needs_noopener:
                rel_val.append("noopener")
            if needs_noreferrer:
                rel_val.append("noreferrer")
            a["rel"] = " ".join(rel_val)
            changed = True

    # ── 3. Fix empty anchors with no text and no aria-label ─────────────────
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        if not text:
            img = a.find("img")
            if img:
                if not img.get("alt"):
                    img["alt"] = "Z3Connect navigation"
                    changed = True
                if not a.get("aria-label"):
                    a["aria-label"] = img.get("alt", "Navigate to page")
                    changed = True
            elif not a.get("aria-label"):
                href = a.get("href", "")
                a["aria-label"] = "Navigate to " + href.strip("/").replace("-", " ") if href else "Navigate to page"
                changed = True

    # ── 4. Ensure all internal links go to canonical form (no .html suffix) ──
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Only process relative .html internal links (not anchors, not external)
        if href.startswith("http") or href.startswith("#") or href.startswith("mailto") or href.startswith("tel") or href.startswith("//"):
            continue
        # Strip query and strip root slashes
        clean = href.split("?")[0].split("#")[0]
        # Normalize: if e.g. "../about.html" just extract basename
        base = os.path.basename(clean)
        if base in CANONICAL_MAP:
            # Build the canonical path
            canon_path = CANONICAL_MAP[base].replace(SITE_URL, "")
            # Replace if different
            if href != canon_path and href != base:
                # only if it's a simple local ref like "about.html"
                if href == base:
                    a["href"] = canon_path
                    changed = True

    # ── 5. Shorten page titles over 60 chars ────────────────────────────────
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        t = title_tag.string.strip()
        if len(t) > 60:
            # Try to trim at pipe separator
            parts = t.split("|")
            if len(parts) > 1:
                core = parts[0].strip()
                brand = parts[-1].strip()
                # Keep brand suffix short
                new_title = f"{core} | {brand}"
                if len(new_title) > 60:
                    # Trim core
                    max_core = 60 - len(brand) - 3  # " | "
                    core = core[:max_core].rsplit(" ", 1)[0]
                    new_title = f"{core} | {brand}"
            else:
                new_title = t[:57] + "..."
            title_tag.string = new_title
            changed = True

    # ── 6. Shorten meta descriptions over 155 chars ─────────────────────────
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content"):
        desc = meta["content"].strip()
        if len(desc) > 155:
            trimmed = desc[:152].rsplit(" ", 1)[0].rstrip(",;") + "..."
            meta["content"] = trimmed
            changed = True

    # ── 7. Add width/height to imgs missing them ─────────────────────────────
    for img in soup.find_all("img"):
        if not img.get("width") or not img.get("height"):
            src = img.get("src", "")
            if src and not src.startswith("http") and not src.startswith("data:"):
                local = src.lstrip("/")
                if os.path.exists(local):
                    try:
                        from PIL import Image as PILImage
                        with PILImage.open(local) as pimg:
                            w, h = pimg.size
                        if not img.get("width"):
                            img["width"] = str(w)
                        if not img.get("height"):
                            img["height"] = str(h)
                        changed = True
                    except Exception:
                        pass

    if changed:
        modified_files.append(filename)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(soup))

print(f"Modified {len(modified_files)} files:")
for f in modified_files:
    print(f"  - {f}")
