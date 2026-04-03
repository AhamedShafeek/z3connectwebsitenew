import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def inspect_seo():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    issues = {
        'long_titles': [],
        'long_meta_desc': [],
        'unsafe_blank': [],
        'non_descriptive_anchors': [],
        'empty_anchors': [],
        'missing_img_sizes': [],
        'multiple_h2': [],
        'underscore_urls': []
    }
    
    for filename in html_files:
        if '_' in filename:
            issues['underscore_urls'].append(filename)

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Titles
        title = soup.find('title')
        if title and len(title.text.strip()) > 60:
            issues['long_titles'].append((filename, title.text.strip()))
            
        # Meta Desc
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content') and len(meta_desc.get('content').strip()) > 155:
            issues['long_meta_desc'].append((filename, meta_desc.get('content').strip()))
            
        # target="_blank"
        for a in soup.find_all('a', target='_blank'):
            rel = a.get('rel', [])
            if isinstance(rel, str):
                rel = rel.split()
            if 'noopener' not in rel and 'noreferrer' not in rel:
                issues['unsafe_blank'].append((filename, str(a)))
                
        # Anchors
        for a in soup.find_all('a'):
            href = a.get('href', '')
            text = a.text.strip().lower()
            if text in ['click here', 'learn more', 'read more']:
                issues['non_descriptive_anchors'].append((filename, str(a)))
            if not text and not a.find('img'): # Text empty and no image
                issues['empty_anchors'].append((filename, str(a)))
            if not text:
                img = a.find('img')
                if img and not img.get('alt'):
                    issues['empty_anchors'].append((filename, str(a)))
                    
        # Images sizes
        for img in soup.find_all('img'):
            if not img.get('width') or not img.get('height'):
                issues['missing_img_sizes'].append((filename, str(img)))
                
        # H2
        h2s = soup.find_all('h2')
        if len(h2s) > 1:
            issues['multiple_h2'].append((filename, len(h2s)))

    import json
    print(json.dumps(issues, indent=2))

if __name__ == "__main__":
    inspect_seo()
