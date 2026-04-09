import os
import re

workspace = "/Users/muhammadnomanashraf/Library/CloudStorage/OneDrive-ku.ac.ae/PhD Work/Research Work/noman_academic_site copy"

css_path = os.path.join(workspace, "style.css")
js_path = os.path.join(workspace, "script.js")

# 1. Update style.css
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add transition to site-header
css = css.replace(
    ".site-header {\n  position: sticky;\n  top: 0;\n  z-index: 50;\n  backdrop-filter: saturate(180%) blur(20px);\n  -webkit-backdrop-filter: saturate(180%) blur(20px);\n  background: var(--surface-glass);\n  border-bottom: 1px solid var(--line);\n}",
    ".site-header {\n  position: sticky;\n  top: 0;\n  z-index: 50;\n  backdrop-filter: saturate(180%) blur(20px);\n  -webkit-backdrop-filter: saturate(180%) blur(20px);\n  background: var(--surface-glass);\n  border-bottom: 1px solid transparent;\n  transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);\n}\n\n.site-header.scrolled {\n  background: rgba(255, 255, 255, 0.85);\n  border-bottom: 1px solid var(--line);\n  box-shadow: 0 8px 32px rgba(0,0,0,0.06);\n}"
)

# Increase nav-wrap min-height and add transition
css = css.replace(
    ".nav-wrap {\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  gap: 0.8rem;\n  min-height: 68px;\n}",
    ".nav-wrap {\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  gap: 0.8rem;\n  min-height: 100px;\n  transition: min-height 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);\n}\n\n.site-header.scrolled .nav-wrap {\n  min-height: 68px;\n}"
)

# Add nav link hover animations
css = css.replace(
    "transition: background 180ms ease, color 180ms ease, transform 180ms ease;",
    "transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);"
)
css = css.replace(
    ".site-nav a:hover,\n.site-nav a.active {\n  background: var(--surface-muted);\n  color: var(--text);\n}",
    ".site-nav a:hover,\n.site-nav a.active {\n  background: var(--surface-muted);\n  color: var(--text);\n}\n\n.site-nav a:hover {\n  transform: translateY(-2px) scale(1.02);\n}"
)

# Avatar animation 
css = css.replace(
    "box-shadow: 0 2px 8px rgba(0,0,0,0.06);",
    "box-shadow: 0 2px 8px rgba(0,0,0,0.06);\n  transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;\n}\n\n.brand:hover .brand-avatar {\n  transform: scale(1.15) rotate(5deg);\n  box-shadow: 0 8px 24px rgba(0,0,0,0.12);"
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# 2. Update script.js
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

scroll_js = """
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }
"""

if "header.classList.add('scrolled')" not in js:
    # Safely insert before the closing '});'
    js = js.replace("});", scroll_js + "\n});")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js)

print("Header increased and animations added.")
