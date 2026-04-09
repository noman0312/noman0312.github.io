import os
import glob
import re

workspace = "/Users/muhammadnomanashraf/Library/CloudStorage/OneDrive-ku.ac.ae/PhD Work/Research Work/noman_academic_site copy"

# 1. Update HTML files
html_files = glob.glob(os.path.join(workspace, "*.html"))
fonts_html = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update theme color to Apple's f5f5f7
    content = re.sub(r'<meta name="theme-color".*?>', '<meta name="theme-color" content="#f5f5f7">', content)
    
    # Update google fonts
    if "fonts.googleapis.com" not in content:
        content = content.replace('  <link rel="stylesheet" href="style.css">', fonts_html)
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Update style.css
css_path = os.path.join(workspace, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace :root with Apple-like vars
new_root = """:root {
  --bg: #f5f5f7;
  --bg-soft: #ebebf0;
  --surface: #ffffff;
  --surface-glass: rgba(255, 255, 255, 0.72);
  --surface-strong: #ffffff;
  --surface-alt: #fbfbfd;
  --surface-muted: #f5f5f7;
  --line: rgba(0, 0, 0, 0.08);
  --line-strong: rgba(0, 0, 0, 0.12);
  --text: #1d1d1f;
  --muted: #86868b;
  --muted-strong: #424245;
  --accent: #0071e3;
  --accent-strong: #0077ed;
  --accent-ink: #ffffff;
  --shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
  --shadow-hover: 0 10px 32px rgba(0, 0, 0, 0.08);
  --radius: 18px;
  --radius-sm: 12px;
  --maxw: 1040px;
  --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  --serif: var(--sans);
}"""

css = re.sub(r':root\s*\{[^}]+\}', new_root, css, count=1)

# Ensure transitions exist for all cards
css = css.replace(
    ".card {\n  border: 1px solid var(--line);\n  border-radius: var(--radius);\n  background: var(--surface);\n  box-shadow: var(--shadow);\n}",
    ".card {\n  border: 1px solid var(--line);\n  border-radius: var(--radius);\n  background: var(--surface);\n  box-shadow: var(--shadow);\n  transition: transform 300ms cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 300ms cubic-bezier(0.2, 0.8, 0.2, 1);\n}\n\n.card:hover {\n  transform: translateY(-4px);\n  box-shadow: var(--shadow-hover);\n}"
)

# Header bg replaced with glassmorphism
css = re.sub(
    r'.site-header \{[\s\S]*?\}',
    ".site-header {\n  position: sticky;\n  top: 0;\n  z-index: 50;\n  backdrop-filter: saturate(180%) blur(20px);\n  -webkit-backdrop-filter: saturate(180%) blur(20px);\n  background: var(--surface-glass);\n  border-bottom: 1px solid var(--line);\n}",
    css, count=1
)

# Fix hover of btn explicitly
css = css.replace(
    ".btn:hover {\n  transform: translateY(-1px);\n  border-color: #b8c1b4;\n}",
    ".btn:hover {\n  transform: translateY(-2px);\n  border-color: var(--line-strong);\n  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);\n}\n\n.btn.primary:hover {\n  background: var(--accent-strong);\n  border-color: transparent;\n  box-shadow: 0 4px 14px rgba(0, 113, 227, 0.3);\n}"
)

# Fix background color of brand-mark
css = css.replace(
    "background: #e3e8df;",
    "background: #f5f5f7;"
).replace(
    "border: 1px solid #cfd7ca;",
    "border: 1px solid var(--line);"
)

# Add Gradient glow to hero
css = css.replace(
    ".hero-home::before,\n.page-hero::before {\n  content: \"\";\n  position: absolute;\n  inset: 0;\n  background:\n    radial-gradient(circle at 15% 0%, rgba(107, 127, 103, 0.08), transparent 28%),\n    radial-gradient(circle at 100% 15%, rgba(88, 103, 82, 0.06), transparent 22%);\n  pointer-events: none;\n}",
    ".hero-home::before,\n.page-hero::before {\n  content: \"\";\n  position: absolute;\n  inset: 0;\n  background:\n    radial-gradient(circle at 15% 0%, rgba(0, 113, 227, 0.04), transparent 35%),\n    radial-gradient(circle at 85% 15%, rgba(0, 113, 227, 0.02), transparent 30%);\n  pointer-events: none;\n}"
)

# Update some structural aspects to fit Apple clean UI
css = css.replace("font-weight: 700;", "font-weight: 600;") # softer weight for mark

# Fix About Page Hardcoded colors so they don't override the Apple theme
css = re.sub(r'color:\s*#1f241f;', 'color: var(--text);', css)
css = re.sub(r'background:\s*#f3f1eb;', 'background: var(--bg);', css)
css = re.sub(r'background:\s*rgba\(243,\s*241,\s*235,\s*0\.94\);', 'background: var(--surface-glass); backdrop-filter: saturate(180%) blur(20px); -webkit-backdrop-filter: saturate(180%) blur(20px);', css)
css = re.sub(r'border-bottom:\s*1px solid rgba\(58, 72, 58, 0.08\);', 'border-bottom: 1px solid var(--line);', css)
css = re.sub(r'color:\s*#2f4a3a;', 'color: var(--accent);', css)
css = re.sub(r'color:\s*#556257;', 'color: var(--muted-strong);', css)
css = re.sub(r'background:\s*#e3e8df;', 'background: var(--surface-muted);', css)
css = re.sub(r'border-color:\s*#cfd7ca;', 'border-color: var(--line);', css)
css = re.sub(r'color:\s*#5f6f55;', 'color: var(--muted-strong);', css)
css = re.sub(r'background:\s*#fbfaf7;', 'background: var(--surface);', css)
css = re.sub(r'border-color:\s*#d9ddd4;', 'border-color: var(--line);', css)
css = re.sub(r'background:\s*#e5e8e0;', 'background: var(--surface-muted);', css)
css = re.sub(r'color:\s*#405243;', 'color: var(--text);', css)
css = re.sub(r'border:\s*1px solid #dde2d8;', 'border: 1px solid var(--line);', css)
css = re.sub(r'background:\s*#6b7f67;', 'background: var(--accent);', css)
css = re.sub(r'border-top:\s*1px solid #e1e4dc;', 'border-top: 1px solid var(--line);', css)
css = re.sub(r'border-color:\s*#e1e4dc;', 'border-color: var(--line);', css)
css = re.sub(r'background:\s*#f4f4ee;', 'background: var(--surface-muted);', css)
css = re.sub(r'background:\s*#f7f5ef;', 'background: var(--surface-muted);', css)
css = re.sub(r'box-shadow: none;', '', css) # allow shadows back



# Ensure headers look Apple-like (tighter letter spacing on big text)
css = re.sub(r'letter-spacing:\s*-0.02em;', 'letter-spacing: -0.015em;', css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Updates applied successfully.")
