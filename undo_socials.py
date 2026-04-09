import os
import glob
import re

workspace = "/Users/muhammadnomanashraf/Library/CloudStorage/OneDrive-ku.ac.ae/PhD Work/Research Work/noman_academic_site copy"
html_files = glob.glob(os.path.join(workspace, "*.html"))

cdns_to_remove = """  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove CDNs
    if cdns_to_remove in content:
        content = content.replace(cdns_to_remove, "")

    # Remove social nav
    social_nav_pattern = r'<div class="social-nav">[\s\S]*?</div>'
    if re.search(social_nav_pattern, content):
        content = re.sub(social_nav_pattern, "", content)

    # Note: re.sub above might leave an empty line, but that's harmless.
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Update style.css
css_path = os.path.join(workspace, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove social CSS block
social_css_pattern = r'\n\.social-nav \{[\s\S]*?\}\n\}'
# The block actually ends with `}\n}` due to media query and lack of EOF formatting.
# Also it could be simpler: search for .social-nav and slice string text or use regex to remove everything from .social-nav to the end of the file.
# Since we appended it at the end, we can just find its starting position.
start_idx = css.find(".social-nav {")
if start_idx != -1:
    css = css[:start_idx].rstrip()

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Reverted social icons addition successfully.")
