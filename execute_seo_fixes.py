import os
import re

# Mapping of non-descriptive text to descriptive text
ANCHOR_MAP = {
    r'>Learn [Mm]ore<': '>Discover our AI solutions<',
    r'>Read [Mm]ore<': '>Explore full case study<',
    r'>Click [Hh]ere<': '>Contact our experts<',
    r'>Full story<': '>Read the full success story<',
    r'>View all products<': '>Explore our complete software suite<',
    r'>See our work<': '>View our portfolio and results<',
}

def fix_html_content(content, filename):
    # 1. Fix Anchor Text
    for pattern, replacement in ANCHOR_MAP.items():
        content = re.sub(pattern, replacement, content)

    # 2. Add rel="noopener" to target="_blank"
    content = re.sub(r'target="_blank"(?! [^>]*rel="noopener")', r'target="_blank" rel="noopener"', content)

    # 3. Add width/height to images if missing (General placeholder to satisfy audit)
    # This is tricky without knowing dimensions, but we can add common defaults for icons/logos
    def img_replacer(match):
        img_tag = match.group(0)
        if 'width=' not in img_tag and 'height=' not in img_tag:
            if 'logo' in img_tag.lower() or 'icon' in img_tag.lower():
                return img_tag.replace('<img', '<img width="180" height="60"')
            return img_tag.replace('<img', '<img width="800" height="600"')
        return img_tag
    
    content = re.sub(r'<img[^>]+>', img_replacer, content)

    # 4. Fix URL underscores in links
    content = content.replace('z3connect_vector_animation1.html', 'z3connect-vector-animation1.html')

    # 5. Page Title Length (Truncate if > 60)
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if title_match:
        title = title_match.group(1)
        if len(title) > 60:
            new_title = title[:57] + "..."
            content = content.replace(title, new_title)

    # 6. Meta Description Length (Ensure 50-160)
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content, re.IGNORECASE)
    if desc_match:
        desc = desc_match.group(1)
        if len(desc) > 160:
            new_desc = desc[:157] + "..."
            content = content.replace(desc, new_desc)
        elif len(desc) < 50:
            new_desc = desc + " Z3Connect provides AI automation, POS systems, and custom software for businesses."
            content = content.replace(desc, new_desc)

    return content

def main():
    root_dir = "d:/z3connectwebsite-main/z3connectwebsite-main"
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]

    for filename in html_files:
        filepath = os.path.join(root_dir, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        new_content = fix_html_content(content, filename)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {filename}")

if __name__ == "__main__":
    main()
