import os
import glob
import re

workspace = "/Users/muhammadnomanashraf/Library/CloudStorage/OneDrive-ku.ac.ae/PhD Work/Research Work/noman_academic_site copy"
html_files = glob.glob(os.path.join(workspace, "*.html"))

cdns = """
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Inject CDNs again
    if "academicons.min.css" not in content:
        content = content.replace('<link rel="stylesheet" href="style.css">', cdns + '\n  <link rel="stylesheet" href="style.css">')

    # Add icons to common buttons
    buttons = {
        '>View Publications</a>': '><i class="fa-solid fa-book-open" style="margin-right:0.4rem"></i>View Publications</a>',
        '>Research Projects</a>': '><i class="fa-solid fa-microchip" style="margin-right:0.4rem"></i>Research Projects</a>',
        '>View Projects</a>': '><i class="fa-solid fa-microchip" style="margin-right:0.4rem"></i>View Projects</a>',
        '>Explore all projects</a>': '><i class="fa-solid fa-arrow-right-long" style="margin-right:0.4rem"></i>Explore all projects</a>',
        '>Download CV</a>': '><i class="fa-solid fa-arrow-down-to-bracket" style="margin-right:0.4rem"></i>Download CV</a>',
        '>Get in touch</a>': '><i class="fa-solid fa-envelope" style="margin-right:0.4rem"></i>Get in touch</a>',
        '>Teaching Experience</a>': '><i class="fa-solid fa-chalkboard-user" style="margin-right:0.4rem"></i>Teaching Experience</a>',
        '>Read Project Details</a>': '><i class="fa-solid fa-file-invoice" style="margin-right:0.4rem"></i>Read Project Details</a>',
        '>Read full project details</a>': '><i class="fa-solid fa-arrow-right" style="margin-right:0.4rem"></i>Read full project details</a>',
        '>Project Deck</a>': '><i class="fa-solid fa-person-chalkboard" style="margin-right:0.4rem"></i>Project Deck</a>'
    }

    for target, replacement in buttons.items():
        if replacement not in content:
            content = content.replace(target, replacement)

    # Specific replacements for At A Glance panel labels
    content = content.replace('<li><strong>Email</strong>', '<li><strong><i class="fa-solid fa-envelope" style="color:var(--accent); margin-right:0.3rem"></i> Email</strong>')
    content = content.replace('<li><strong>Contact</strong>', '<li><strong><i class="fa-solid fa-phone" style="color:var(--accent); margin-right:0.3rem"></i> Contact</strong>')
    content = content.replace('<li><strong>Affiliation</strong>', '<li><strong><i class="fa-solid fa-building-columns" style="color:var(--accent); margin-right:0.3rem"></i> Affiliation</strong>')
    content = content.replace('<li><strong>Focus</strong>', '<li><strong><i class="fa-solid fa-bolt" style="color:var(--accent); margin-right:0.3rem"></i> Focus</strong>')

    # Replace the Profiles row completely
    old_profile_str = '<li><strong>Profiles</strong><span><a href="https://scholar.google.com/citations?hl=en&amp;user=uXgbWVsAAAAJ&amp;view_op=list_works&amp;sortby=pubdate" target="_blank" rel="noopener">Scholar</a> · <a href="https://www.scopus.com/authid/detail.uri?authorId=57214337213" target="_blank" rel="noopener">Scopus</a> · <a href="https://orcid.org/0000-0003-0970-4592" target="_blank" rel="noopener">ORCID</a> · <a href="https://www.linkedin.com/in/muhammad-noman-ashraf-4a862bb4/" target="_blank" rel="noopener">LinkedIn</a></span></li>'
    
    new_profile_str = """<li style="display:flex; flex-direction:column; gap:0.6rem; padding-top:0.8rem;">
                  <strong><i class="fa-solid fa-globe" style="color:var(--accent); margin-right:0.3rem"></i> Profiles</strong>
                  <div style="display:flex; gap:0.6rem; flex-wrap:wrap; margin-top:0.2rem">
                    <a href="https://scholar.google.com/citations?hl=en&amp;user=uXgbWVsAAAAJ&amp;view_op=list_works&amp;sortby=pubdate" target="_blank" rel="noopener" class="profile-icon-link" aria-label="Google Scholar"><i class="ai ai-google-scholar"></i></a>
                    <a href="https://www.scopus.com/authid/detail.uri?authorId=57214337213" target="_blank" rel="noopener" class="profile-icon-link" aria-label="Scopus"><i class="ai ai-scopus"></i></a>
                    <a href="https://orcid.org/0000-0003-0970-4592" target="_blank" rel="noopener" class="profile-icon-link" aria-label="ORCID"><i class="ai ai-orcid"></i></a>
                    <a href="https://www.linkedin.com/in/muhammad-noman-ashraf-4a862bb4/" target="_blank" rel="noopener" class="profile-icon-link" aria-label="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
                  </div>
                </li>"""
    
    if "class=\"profile-icon-link\"" not in content and old_profile_str in content:
        content = content.replace(old_profile_str, new_profile_str)

    # In skills.html add some icons to headers
    content = content.replace('<h2>Experimental Skills</h2>', '<h2><i class="fa-solid fa-microchip" style="margin-right:0.4rem; color:var(--accent)"></i>Experimental Skills</h2>')
    content = content.replace('<h2>Software Skills</h2>', '<h2><i class="fa-solid fa-laptop-code" style="margin-right:0.4rem; color:var(--accent)"></i>Software Skills</h2>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Update style.css for profile-icon-link
css_path = os.path.join(workspace, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

profile_icon_css = """
.profile-icon-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--surface-muted);
  color: var(--text);
  font-size: 1.15rem;
  transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
  text-decoration: none;
  border: 1px solid var(--line);
}
.profile-icon-link:hover {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 113, 227, 0.2);
}
.profile-icon-link i {
  margin: 0;
}
"""

if ".profile-icon-link" not in css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n" + profile_icon_css)

print("Icons successfully distributed across the page content.")
