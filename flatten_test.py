import os, re
root = '/Users/muhammadnomanashraf/Library/CloudStorage/OneDrive-ku.ac.ae/PhD Work/Research Work/noman_academic_site copy'
old_to_new = {}

# find all directories to process
dirs_to_process = []
for item in os.listdir(root):
    path = os.path.join(root, item)
    if os.path.isdir(path) and item not in ['.git', '__pycache__']:
        dirs_to_process.append(item)

print(dirs_to_process)
