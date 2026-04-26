import glob
from bs4 import BeautifulSoup

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    changed = False
    for img in soup.find_all('img'):
        # skip if no src
        if not img.has_attr('src'):
            continue
            
        # skip avatars or icons
        classes = img.get('class', [])
        if 'brand-avatar' in classes or img['src'] == 'Noman.jpg':
            continue
            
        # skip if already in an <a> tag
        if img.parent.name == 'a':
            continue
            
        # create new <a> tag
        a_tag = soup.new_tag('a')
        a_tag['href'] = img['src']
        a_tag['target'] = '_blank'
        a_tag['rel'] = 'noopener'
        
        # wrap the img
        img.wrap(a_tag)
        changed = True
        
    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f'Updated {file}')

