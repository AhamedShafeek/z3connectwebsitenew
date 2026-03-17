import re

# Read the SVG file
with open('image/z3-logo-animated.svg', 'r', encoding='utf-8') as f:
    svg_content = f.read()

# Remove XML declaration
svg_content = re.sub(r'<\?xml.*?\?>', '', svg_content, flags=re.DOTALL).strip()

# Replace width/height with responsive styling
svg_content = svg_content.replace('width="500"', '')
svg_content = svg_content.replace('height="500"', 'id="hero-logo-svg" style="height: 360px; width: auto; overflow: visible;"')

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build inline SVG wrapper (replace the img tag)
old_block = '''      <div class="hero-logo-wrapper nav-logo">
        <img src="image/z3-logo-animated.svg" alt="Z3Connect Logo" class="hero-logo"
          style="height: 360px; filter: none; mix-blend-mode: normal;">
      </div>'''

new_block = '''      <div class="hero-logo-wrapper nav-logo" id="hero-logo-wrapper">
        ''' + svg_content + '''
      </div>'''

if old_block in html:
    html = html.replace(old_block, new_block)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('SUCCESS: Inline SVG injected into hero section.')
else:
    print('ERROR: Could not find the target block. Check the search string.')
    # Try fuzzy find
    if 'z3-logo-animated.svg' in html:
        print('  Found SVG reference in HTML - checking context...')
        idx = html.find('z3-logo-animated.svg')
        print(repr(html[max(0, idx-200):idx+200]))
