import os

def scrub_vlogs(directory):
    replacements = [
        ('vlogs.html', 'blogs.html'),
        ('vlog-', 'blog-'),
        ('Vlogs', 'Blogs'),
        ('Vlog', 'Blog'),
        ('vlog', 'blog')
    ]
    
    for root, dirs, files in os.walk(directory):
        if '.git' in root: continue
        for file in files:
            if file.endswith(('.html', '.js', '.css')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    new_content = content
                    for old, new in replacements:
                        new_content = new_content.replace(old, new)
                    
                    if new_content != content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Scrubbed: {path}")
                except Exception as e:
                    print(f"Error scrubbing {path}: {e}")

if __name__ == "__main__":
    scrub_vlogs('.')
