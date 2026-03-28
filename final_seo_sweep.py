import os
import re

def optimize_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add loading="lazy" and decoding="async" to images (except first 2)
    img_count = 0
    def img_replacer(match):
        nonlocal img_count
        img_tag = match.group(0)
        img_count += 1
        
        # Add decoding="async" if missing
        if 'decoding=' not in img_tag:
            img_tag = img_tag.replace('<img', '<img decoding="async"')
        
        # Add loading="lazy" if missing and count > 2
        if img_count > 2 and 'loading=' not in img_tag:
            img_tag = img_tag.replace('<img', '<img loading="lazy"')
            
        return img_tag

    content = re.sub(r'<img[^>]+>', img_replacer, content)

    # 2. Add alt tags if missing (based on src)
    def alt_replacer(match):
        img_tag = match.group(0)
        if 'alt=' not in img_tag or 'alt=""' in img_tag:
            src_match = re.search(r'src="([^"]+)"', img_tag)
            if src_match:
                src = src_match.group(1)
                # Extract filename without extension and replace hyphens with spaces
                alt_text = os.path.splitext(os.path.basename(src))[0].replace('-', ' ').replace('_', ' ').capitalize()
                if 'alt=' in img_tag:
                    img_tag = re.sub(r'alt="[^"]*"', f'alt="{alt_text}"', img_tag)
                else:
                    img_tag = img_tag.replace('<img', f'<img alt="{alt_text}"')
        return img_tag

    content = re.sub(r'<img[^>]+>', alt_replacer, content)

    # 3. Add width and height if missing (defaulting to 800/600 or specific common ones)
    # This is a bit risky but good for CLS if you know common sizes. 
    # For now, let's at least ensure they exist for main banners or just skip if uncertain.
    # Let's skip auto-width/height to avoid distortion, but we'll flag them.

    # 4. Correct Instagram link
    content = content.replace('href="#"', 'href="https://instagram.com/z3connect"') # Targeted fix for social links

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Process all HTML files
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            optimize_html(os.path.join(root, file))

print("SEO Sweep Complete.")
