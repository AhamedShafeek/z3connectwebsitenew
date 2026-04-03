"""
Fix remaining HTML canonical issues:
- content-flow.html (still has .html canonical)
- case-study-*.html pages (still have .html canonicals)  
- 404.html (missing meta and canonical)
"""
import os
from bs4 import BeautifulSoup

CANONICAL_MAP = {
    "content-flow.html": "https://z3connect.com/content-flow",
    "case-study.html": "https://z3connect.com/case-study",
    "case-study-atom-infra.html": "https://z3connect.com/case-study-atom-infra",
    "case-study-crazy-coconut.html": "https://z3connect.com/case-study-crazy-coconut",
    "case-study-faam.html": "https://z3connect.com/case-study-faam",
    "case-study-femmic.html": "https://z3connect.com/case-study-femmic",
    "case-study-iqrah-academy.html": "https://z3connect.com/case-study-iqrah-academy",
    "case-study-lam-stacks.html": "https://z3connect.com/case-study-lam-stacks",
    "case-study-meta-giants.html": "https://z3connect.com/case-study-meta-giants",
    "case-study-mwi-groups.html": "https://z3connect.com/case-study-mwi-groups",
    "case-study-pd-turbo-tech.html": "https://z3connect.com/case-study-pd-turbo-tech",
    "case-study-pocket-delivery.html": "https://z3connect.com/case-study-pocket-delivery",
    "portfolio.html": "https://z3connect.com/work",
}

for filename, correct_canonical in CANONICAL_MAP.items():
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    changed = False
    
    canon = soup.find('link', rel='canonical')
    if canon and canon.get('href') != correct_canonical:
        canon['href'] = correct_canonical
        changed = True
    elif not canon:
        head = soup.find('head')
        if head:
            new_canon = soup.new_tag('link', rel='canonical', href=correct_canonical)
            head.append(new_canon)
            changed = True
    
    # Fix target="_blank" safety
    for a in soup.find_all('a', target='_blank'):
        rel_val = a.get('rel', [])
        if isinstance(rel_val, str): rel_val = rel_val.split()
        if 'noopener' not in rel_val: rel_val.append('noopener')
        if 'noreferrer' not in rel_val: rel_val.append('noreferrer')
        a['rel'] = " ".join(rel_val)
        changed = True
    
    if changed:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed: {filename}")

# Fix 404.html specially
if os.path.exists('404.html'):
    with open('404.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    changed = False
    head = soup.find('head')
    if head:
        if not soup.find('meta', attrs={'name': 'description'}):
            desc = soup.new_tag('meta', attrs={'name': 'description', 'content': 'Page not found. Navigate back to Z3Connect to explore our AI-powered software solutions for businesses in India.'})
            head.append(desc)
            changed = True
        if not soup.find('link', rel='canonical'):
            canon = soup.new_tag('link', rel='canonical', href='https://z3connect.com/404')
            head.append(canon)
            changed = True
        if not soup.find('meta', attrs={'name': 'robots'}):
            robots = soup.new_tag('meta', attrs={'name': 'robots', 'content': 'noindex, follow'})
            head.append(robots)
            changed = True
    if changed:
        with open('404.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print("Fixed: 404.html")

print("Done.")
