import os
import re

dir_path = '.'

# Regex to find <link rel="icon" ...> or <link rel="apple-touch-icon" ...>
# We will just replace any href associated with standard favicons.
tags_patterns = [
    r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>',
    r'<link[^>]*rel=["\']apple-touch-icon["\'][^>]*>'
]

new_icon = '<link rel="icon" href="image/icon/faviicon.png" type="image/png">'
new_apple = '<link rel="apple-touch-icon" href="image/icon/faviicon.png">'

html_files = []
for root, dirs, files in os.walk(dir_path):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace ALL occurrences of favicon tags with nothing,
    # except the very first one which we replace with our new tags!
    
    # Actually, simpler: just remove all matching tags.
    # Then insert the new tags right before </head>.
    new_content = content
    for p in tags_patterns:
        new_content = re.sub(p, '', new_content, flags=re.IGNORECASE)
    
    # insert new tags before </head>
    # Note: we should handle </head> case insensitively
    new_tags = f'  {new_icon}\n  {new_apple}\n'
    new_content = re.sub(r'(\s*</head>)', r'\n' + new_tags + r'\1', new_content, flags=re.IGNORECASE, count=1)
    
    # Clean up multiple blank lines that might have been left by removing old tags
    # Usually they leave an empty line with spaces
    new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
