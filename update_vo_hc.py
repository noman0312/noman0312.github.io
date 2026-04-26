import re

with open('project-vo-hc.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = """
<div class="grid-2 image-showcase">
<figure class="image-card research-figure-card card" data-reveal="">
<a href="vo-hc-microgrid-setup.png" rel="noopener" target="_blank"><img alt="Two-inverter laboratory microgrid setup used for the VO-HC project" src="vo-hc-microgrid-setup.png"/></a>
<figcaption>Two-inverter laboratory microgrid used to test the VO-HC method under weak-grid and distorted-grid operation.</figcaption>
</figure>
<figure class="image-card research-figure-card card" data-reveal="">
<a href="phd_opal_rt_hil.jpg" rel="noopener" target="_blank"><img alt="OPAL-RT HIL setup" src="phd_opal_rt_hil.jpg"/></a>
<figcaption>Working on OPAL-RT for real time Hardware-in-the-Loop (HIL) simulations during my PhD.</figcaption>
</figure>
<figure class="image-card research-figure-card card" data-reveal="">
<a href="phd_custom_setup_2.jpg" rel="noopener" target="_blank"><img alt="Custom PhD setup" src="phd_custom_setup_2.jpg"/></a>
<figcaption>Custom hardware and testing setup that I developed during my PhD research.</figcaption>
</figure>
<figure class="image-card research-figure-card card" data-reveal="">
<a href="phd_custom_experimental_setup.jpg" rel="noopener" target="_blank"><img alt="Custom experimental setup during PhD" src="phd_custom_experimental_setup.jpg"/></a>
<figcaption>Overview of the custom experimental workbench I used for testing during my PhD.</figcaption>
</figure>
</div>
<div class="grid-2">
<article class="card" data-reveal="">
<h3>Hardware setup details</h3>
<ul class="highlights">
<li>Implemented the experiments on a two-level, two-inverter microgrid.</li>
<li>Ran inverter 1 in grid-forming mode to emulate the grid and injected 5th and 7th voltage harmonics.</li>
<li>Ran inverter 2 in grid-following mode with the proposed VO-HC method.</li>
<li>Added 1.5 mH series impedance to emulate a weak-grid condition at the PCC.</li>
<li>Used a parallel load and DC-supply return path so the injected power could be absorbed safely during tests.</li>
</ul>
</article>
</div>
"""

# Replace from `<div class="grid-2 image-showcase">` up to `</article>\n</div>`
pattern = r'<div class="grid-2 image-showcase">\s*<figure class="image-card research-figure-card card" data-reveal="">.*?vo-hc-microgrid-setup\.png.*?</ul>\s*</article>\s*</div>'

content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open('project-vo-hc.html', 'w', encoding='utf-8') as f:
    f.write(content)

