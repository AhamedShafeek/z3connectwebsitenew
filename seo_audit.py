import os
from bs4 import BeautifulSoup

def audit_html(directory):
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    report = []
    
    for filename in html_files:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
            # Check Meta
            title = soup.title.string if soup.title else 'MISSING'
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            desc = meta_desc['content'] if meta_desc else 'MISSING'
            
            # Check Schema
            schema = soup.find_all('script', type='application/ld+json')
            schema_count = len(schema)
            
            # Check Images Alt
            images = soup.find_all('img')
            missing_alt = [img['src'] for img in images if not img.get('alt')]
            
            report.append({
                'file': filename,
                'title': title,
                'description': desc,
                'schemas': schema_count,
                'missing_alt_count': len(missing_alt),
                'missing_alt_files': missing_alt[:3] # Show first 3
            })
            
    return report

if __name__ == "__main__":
    results = audit_html('.')
    for r in results:
        print(f"File: {r['file']}")
        print(f"  Title: {r['title']}")
        print(f"  Desc: {r['description'][:50]}...")
        print(f"  Schemas: {r['schemas']}")
        print(f"  Missing Alts: {r['missing_alt_count']}")
        if r['missing_alt_files']:
            print(f"  Samples: {r['missing_alt_files']}")
        print("-" * 20)
