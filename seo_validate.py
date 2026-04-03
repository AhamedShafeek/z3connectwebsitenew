"""
Final SEO Validation: Scan all HTML files and report remaining issues.
"""
import os
from bs4 import BeautifulSoup

issues = []

for filename in sorted(os.listdir('.')):
    if not filename.endswith('.html'):
        continue
    if 'demo' in filename or 'animation' in filename or filename == 'cards-partial.html':
        continue

    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Title check
    title = soup.find('title')
    if not title or not title.string:
        issues.append(f"[MISSING TITLE] {filename}")
    elif len(title.string.strip()) > 60:
        issues.append(f"[LONG TITLE {len(title.string.strip())}c] {filename}: {title.string.strip()[:70]}")

    # Meta description
    meta = soup.find('meta', attrs={'name': 'description'})
    if not meta or not meta.get('content'):
        issues.append(f"[MISSING META DESC] {filename}")
    elif len(meta['content']) > 155:
        issues.append(f"[LONG META DESC {len(meta['content'])}c] {filename}")

    # Canonical
    canon = soup.find('link', rel='canonical')
    if not canon or not canon.get('href'):
        issues.append(f"[MISSING CANONICAL] {filename}")
    elif canon.get('href', '').endswith('.html'):
        issues.append(f"[.html CANONICAL] {filename}: {canon['href']}")

    # target=_blank without rel
    for a in soup.find_all('a', target='_blank'):
        rel = a.get('rel', [])
        if isinstance(rel, str): rel = rel.split()
        if 'noopener' not in rel:
            issues.append(f"[UNSAFE BLANK] {filename}: {a.get('href','')[:60]}")

    # Images missing width or height
    missing_dims = [img for img in soup.find_all('img') if not img.get('width') or not img.get('height')]
    if missing_dims:
        issues.append(f"[IMG NO DIMS x{len(missing_dims)}] {filename}")

    # Empty anchors
    for a in soup.find_all('a'):
        text = a.get_text(strip=True)
        if not text and not a.get('aria-label'):
            img = a.find('img')
            if not img or not img.get('alt'):
                issues.append(f"[EMPTY ANCHOR] {filename}: {a.get('href','')[:50]}")

    # H1 missing
    if not soup.find('h1'):
        issues.append(f"[MISSING H1] {filename}")

if issues:
    print(f"\n=== {len(issues)} remaining issues ===\n")
    for i in issues:
        print(f"  {i}")
else:
    print("\n✅ All checks passed — no remaining issues!")
