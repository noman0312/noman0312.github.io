import re

with open('project-transless-dvc.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace the image-showcase section in project-transless-dvc.html
# with the full 13-image gallery.

gallery_html = """
          <div class="grid-3 image-showcase" style="gap: 1.5rem; margin-top: 2rem; margin-bottom: 2rem;">
            <figure class="image-card card" data-reveal>
              <a href="transless-topology.png" target="_blank" rel="noopener"><img src="transless-topology.png" alt="Topology figure from the transformerless dynamic voltage compensator project"></a>
              <figcaption>System topology that I selected and implemented during industrial converter development work.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="10kw_converter_assembled.jpg" target="_blank" rel="noopener"><img src="10kw_converter_assembled.jpg" alt="Final assembled 10kW bidirectional converter"></a>
              <figcaption>Final assembled 10kW product including the DC-DC converter and bidirectional inverter stages.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="10kw_converter_front_panel.jpg" target="_blank" rel="noopener"><img src="10kw_converter_front_panel.jpg" alt="10kW bidirectional project front panel"></a>
              <figcaption>Front panel of the completed 10kW bidirectional converter project.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="10kw_converter_pcb.jpg" target="_blank" rel="noopener"><img src="10kw_converter_pcb.jpg" alt="10kW bidirectional converter PCBs"></a>
              <figcaption>Close-up of the power stage PCBs and hardware integration for the 10kW project.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="10kw_module_hand_size.jpg" target="_blank" rel="noopener"><img src="10kw_module_hand_size.jpg" alt="10kW module hand size comparison"></a>
              <figcaption>10kW power module that I designed, with hand for size comparison.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="10kw_converter_oscilloscope.jpg" target="_blank" rel="noopener"><img src="10kw_converter_oscilloscope.jpg" alt="10kW bidirectional converter under testing with oscilloscope"></a>
              <figcaption>Oscilloscope waveforms captured during the live testing of the 10kW bidirectional converter.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="oky_low_voltage_testing.jpg" target="_blank" rel="noopener"><img src="oky_low_voltage_testing.jpg" alt="Low voltage testing of the 10kW project"></a>
              <figcaption>Low voltage testing setup for the 10kW bidirectional converter project.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="oky_leakage_inductance_testing.png" target="_blank" rel="noopener"><img src="oky_leakage_inductance_testing.png" alt="Leakage inductance testing for the 10kW project"></a>
              <figcaption>Leakage inductance testing procedure for the magnetic components of the 10kW project.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="oky_control_board_testing.jpg" target="_blank" rel="noopener"><img src="oky_control_board_testing.jpg" alt="Control board and gate driver testing"></a>
              <figcaption>Custom control board and gate driver testing platform I developed at OKY.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="oky_testing_bench.jpg" target="_blank" rel="noopener"><img src="oky_testing_bench.jpg" alt="My testing bench for OKY"></a>
              <figcaption>My primary testing bench at OKY Ltd., showing measurement tools, DSP emulator, and analyzers used during hardware validation.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="oky_dvc_testing_bed.jpg" target="_blank" rel="noopener"><img src="oky_dvc_testing_bed.jpg" alt="DVC testing bed"></a>
              <figcaption>Testing bed during DVC tests where I upgraded and tuned inverter controllers to reduce peak overshoots and ensure compliance.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="oky_50kw_dvc.jpg" target="_blank" rel="noopener"><img src="oky_50kw_dvc.jpg" alt="50kW single phase DVC"></a>
              <figcaption>50kW single phase DVC system for which I developed and updated the complete firmware.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="transless-dcdc-assembly.png" target="_blank" rel="noopener"><img src="transless-dcdc-assembly.png" alt="10 kilowatt transless DC-DC converter board assembly"></a>
              <figcaption>DC-DC hardware assembly that I designed, including stacked gate modules and high-side / low-side integration.</figcaption>
            </figure>
            <figure class="image-card card" data-reveal>
              <a href="transless-inverter-assembly.png" target="_blank" rel="noopener"><img src="transless-inverter-assembly.png" alt="Inverter assembly hardware from the OKY Ltd. project"></a>
              <figcaption>Hardware realization of the inverter section that I designed and integrated.</figcaption>
            </figure>
          </div>
"""

# Replace the existing grid-2 image-showcase in project-transless-dvc.html
pattern = r'<div class="grid-2 image-showcase">.*?</div>'
# We have to be careful since there are multiple grid-2 in the document.
# Let's insert the gallery at the end of the "Hardware" section.
hardware_section_start = content.find('<h2>What I designed on the hardware side</h2>')
if hardware_section_start != -1:
    grid_end = content.find('</div>', content.find('</div>', content.find('<div class="grid-2 image-showcase">', hardware_section_start) + 30) + 6) + 6
    # It's safer to just regex replace the specific block.
    # The block starts with <div class="grid-2 image-showcase"> and contains transless-dcdc-assembly.png
    block_pattern = r'<div class="grid-2 image-showcase">\s*<figure class="image-card card"[^>]*>.*?transless-dcdc-assembly\.png.*?</figure>\s*<figure class="image-card card"[^>]*>.*?transless-inverter-assembly\.png.*?</figure>\s*</div>'
    
    content = re.sub(block_pattern, gallery_html, content, flags=re.DOTALL)

with open('project-transless-dvc.html', 'w', encoding='utf-8') as f:
    f.write(content)
