import os

html_dir = r'd:\z3connectwebsite-main\z3connectwebsite-main'
files = [f for f in os.listdir(html_dir) if f.endswith('.html')]
fixed = []

for fname in files:
    path = os.path.join(html_dir, fname)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    new_content = content.replace('href="/" class="nav-logo"', 'href="index.html" class="nav-logo"')
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed.append(fname)

print(f'Fixed {len(fixed)} files: {", ".join(fixed)}')
