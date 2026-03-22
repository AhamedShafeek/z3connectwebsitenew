import os

def fix_menus_and_footers(directory):
    for root, dirs, files in os.walk(directory):
        if '.git' in root: continue
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    new_content = content
                    
                    # Fix mobile menu (inject Blogs before Contact if missing)
                    mobile_blog_link = '<a href="blogs.html" class="mobile-menu-link">Blogs</a>'
                    contact_link = '<a href="contact.html" class="mobile-menu-link">Contact</a>'
                    
                    if mobile_blog_link not in new_content and contact_link in new_content:
                        new_content = new_content.replace(
                            contact_link,
                            mobile_blog_link + '\n      ' + contact_link
                        )
                        print(f"Injected mobile link: {path}")
                    
                    # Ensure Blogs is in footer if missing or still vlogs
                    if 'vlogs.html' in new_content:
                         new_content = new_content.replace('vlogs.html', 'blogs.html')
                    
                    if 'Vlogs' in new_content:
                         new_content = new_content.replace('Vlogs', 'Blogs')

                    if new_content != content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Fixed menu/footer: {path}")
                except Exception as e:
                    print(f"Error fixing {path}: {e}")

if __name__ == "__main__":
    fix_menus_and_footers('.')
