import os

def fix_footer_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix robots.txt to sitemap.xml in footer
    new_content = content.replace('href="robots.txt">Sitemap</a>', 'href="sitemap.xml">Sitemap</a>')
    
    # Also ensure canonical matches the filename if missing or incorrect
    # This is a bit complex, but for now let's focus on footer fixes.
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Process all HTML files
files_fixed = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            if fix_footer_links(os.path.join(root, file)):
                files_fixed += 1

print(f"Fixed footer links in {files_fixed} files.")
