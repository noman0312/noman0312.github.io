import os
import glob
import re

workspace = "/Users/muhammadnomanashraf/Library/CloudStorage/OneDrive-ku.ac.ae/PhD Work/Research Work/noman_academic_site copy"

html_files = glob.glob(os.path.join(workspace, "*.html"))

nav_link_to_insert = '<li><a href="skills.html">Skills</a></li>'
anchor_pattern = r'(<li><a href="about\.html">.*?</a></li>)'

for file_path in html_files:
    if "skills.html" in os.path.basename(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if nav_link_to_insert not in content:
        # Insert Skills link right after the About & Contact link
        content = re.sub(
            anchor_pattern,
            r'\1\n            ' + nav_link_to_insert,
            content
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Navigation updated successfully.")
