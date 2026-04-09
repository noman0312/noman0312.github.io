import os
import glob
import re

workspace = "/Users/muhammadnomanashraf/Library/CloudStorage/OneDrive-ku.ac.ae/PhD Work/Research Work/noman_academic_site copy"

html_files = glob.glob(os.path.join(workspace, "*.html"))

original_span = '<span class="brand-mark">MNA</span>'
new_img = '<img class="brand-avatar" src="Noman.jpg" alt="Muhammad Noman Ashraf">'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if original_span in content:
        content = content.replace(original_span, new_img)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
    # Some pages might have a slightly different indentation or formatting just in case, but replace should catch it.
    # We will also use regex to be safe.
    content = re.sub(r'<span class="brand-mark">\s*MNA\s*</span>', new_img, content)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

css_path = os.path.join(workspace, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add styles for the new avatar
avatar_css = """
.brand-avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  border: 1px solid var(--line-strong);
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
"""

if ".brand-avatar" not in css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n" + avatar_css)

print("Avatar replaced successfully in all files and CSS updated.")
