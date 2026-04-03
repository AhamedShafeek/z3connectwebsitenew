import os, sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

issues = []
for filename in sorted(os.listdir('.')):
    if not filename.endswith('.html'):
        continue
    if 'demo' in filename or 'animation' in filename or filename == 'cards-partial.html':
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    title = soup.find('title')
    if not title or not title.string:
        issues.append(f"MISSING_TITLE|{filename}")
    elif len(title.string.strip()) > 60:
        issues.append(f"LONG_TITLE {len(title.string.strip())}|{filename}|{title.string.strip()[:65]}")
    meta = soup.find('meta', attrs={'name': 'description'})
    if not meta or not meta.get('content'):
        issues.append(f"MISSING_META|{filename}")
    elif len(meta['content']) > 155:
        issues.append(f"LONG_META {len(meta['content'])}|{filename}")
    canon = soup.find('link', rel='canonical')
    if not canon or not canon.get('href'):
        issues.append(f"MISSING_CANONICAL|{filename}")
    elif canon.get('href','').endswith('.html'):
        issues.append(f"HTML_CANONICAL|{filename}|{canon['href']}")
    for a in soup.find_all('a', target='_blank'):
        rel = a.get('rel', [])
        if isinstance(rel, str): rel = rel.split()
        if 'noopener' not in rel:
            issues.append(f"UNSAFE_BLANK|{filename}|{a.get('href','')[:50]}")

for i in issues:
    print(i)
print(f"TOTAL={len(issues)}")
