import re
import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all <img src="X" ...>
    # We will ignore brand-avatar since it's already in a link usually, or we just don't wrap it.
    
    def replacer(match):
        img_tag = match.group(0)
        if 'brand-avatar' in img_tag:
            return img_tag
        src = match.group(1)
        return f'<a href="{src}" target="_blank" rel="noopener">{img_tag}</a>'
    
    # Simple negative lookbehind to check if <a ...> precedes it? No, regex is hard.
    # Let's remove existing a wrappers first if any? No, we don't have a wrappers around these images yet, except maybe in some places.
    
    # Actually, we can just find <figure class="image-card card"> <img ...> </figure>
    # and replace the img part.
    
    def fig_replacer(match):
        fig_start = match.group(1)
        img_src = match.group(2)
        img_full = match.group(3)
        return f'{fig_start}<a href="{img_src}" target="_blank" rel="noopener">\n              {img_full}\n            </a>'

    # Pattern for <figure...>\s*(<img src="([^"]+)"[^>]+>)
    pattern = r'(<figure[^>]*>\s*)(<img[^>]*src="([^"]+)"[^>]*>)'
    # Wait, the img tag might have newlines if formatted.
    pattern = r'(<figure[^>]*>\s*)<img\s+[^>]*src="([^"]+)"[^>]*>'
    
    # Let's use a simpler approach. Just read lines and if we see <img src="X", and it's inside <figure>, wrap it.
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if '<img ' in line and 'src="' in line and 'brand-avatar' not in line and 'academicons' not in line:
            # Check if it's already wrapped in <a
            if '<a href=' not in lines[i-1] and '<a href=' not in line:
                match = re.search(r'<img[^>]*src="([^"]+)"[^>]*>', line)
                if match:
                    src = match.group(1)
                    img_tag = match.group(0)
                    lines[i] = line.replace(img_tag, f'<a href="{src}" target="_blank" rel="noopener">{img_tag}</a>')
                    
        # Some img tags are multi-line.
        if '<img ' in line and '>' not in line:
            # multi-line img
            # let's just use beautifulsoup!
            pass

with open('wrap_images.py', 'a') as f:
    pass
