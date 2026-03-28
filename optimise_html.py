import os
import re

target_files = ['team.html', 'founder.html', 'terms.html', 'case-study.html', 'portfolio.html']
base_dir = r'd:\z3connectwebsite-main\z3connectwebsite-main'

def fix_metadata(content, filename):
    # 1. Favicon standardization
    # Remove existing icons
    content = re.sub(r'<link[^>]*rel=["\'](?:shortcut\s+)?icon["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<link[^>]*rel=["\']apple-touch-icon["\'][^>]*>', '', content, flags=re.IGNORECASE)
    
    # Add new standardized favicon just before <!-- Fonts --> or inside <head>
    new_favicon = '<!-- Favicon -->\n  <link rel="icon" href="/image/icon/z3icon.ico" type="image/x-icon">\n  <link rel="apple-touch-icon" href="/image/icon/z3icon.ico">\n'
    
    if '<!-- Fonts -->' in content:
        content = content.replace('<!-- Fonts -->', new_favicon + '<!-- Fonts -->')
    else:
        content = re.sub(r'(</title>)', r'\1\n  ' + new_favicon, content, flags=re.IGNORECASE)
        
    # 2. Theme color
    if '<meta name="theme-color"' not in content:
        content = re.sub(r'(<meta name="viewport"[^>]*>)', r'\1\n  <meta name="theme-color" content="#000000">', content, flags=re.IGNORECASE)
        
    # 3. Meta description
    if '<meta name="description"' not in content:
        desc_text = f"Z3Connect {filename.replace('.html', '').replace('-', ' ').title()} - We build automation tools for MSMEs."
        base_desc = f'<meta name="description" content="{desc_text}">'
        content = re.sub(r'(<meta name="theme-color"[^>]*>)', r'\1\n  ' + base_desc, content, flags=re.IGNORECASE)

    return content

def fix_performance(content):
    # Add loading="lazy" decoding="async" to images without them
    # We skip hero images or navigational logos like logo0.png, logo_wbg.png
    def repl_img(m):
        full_tag = m.group(0)
        # Check standard ignores
        if 'logo0.png' in full_tag or 'logo_wbg.png' in full_tag or 'hero' in full_tag.lower():
            return full_tag
            
        # Add attributes if not present
        if 'loading="lazy"' not in full_tag:
            full_tag = full_tag.replace('<img ', '<img loading="lazy" decoding="async" ')
        return full_tag
        
    content = re.sub(r'<img\s+[^>]*>', repl_img, content, flags=re.IGNORECASE)
    return content

def fix_accessibility(content):
    # Fix Instagram generic links # -> real link or correct aria
    content = re.sub(r'<a href="#" aria-label="Instagram">', r'<a href="https://instagram.com/z3connect" aria-label="Instagram">', content)
    
    return content

# Execute for targets
for file_name in target_files:
    file_path = os.path.join(base_dir, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
            
        updated_content = fix_metadata(original_content, file_name)
        updated_content = fix_performance(updated_content)
        updated_content = fix_accessibility(updated_content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"✅ Optimized {file_name}")
    else:
        print(f"❌ File not found: {file_name}")
