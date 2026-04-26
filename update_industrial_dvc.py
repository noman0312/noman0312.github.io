import re

with open('industrial-experience.html', 'r') as f:
    content = f.read()

new_figure = """
            <figure class="image-card card" data-reveal>
              <img src="oky_dvc_testing_bed.jpg" alt="DVC testing bed">
              <figcaption>Testing bed during DVC tests where I upgraded and tuned inverter controllers to reduce peak overshoots and ensure compliance.</figcaption>
            </figure>
"""

# Find the end of the grid-3 div
# It ends with:
#             <figure class="image-card card" data-reveal>
#               <img src="transless-inverter-assembly.png" alt="Inverter assembly hardware from the OKY Ltd. project">
#               <figcaption>Hardware realization of the inverter section that I designed and integrated.</figcaption>
#             </figure>
#           </div>

pattern = r'(<img src="transless-inverter-assembly\.png".*?</figure>\n)'
content = re.sub(pattern, r'\1' + new_figure, content, flags=re.DOTALL)

with open('industrial-experience.html', 'w') as f:
    f.write(content)
