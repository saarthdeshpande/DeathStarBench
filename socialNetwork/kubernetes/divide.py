# Python script to divide the all.yaml file into per-service directories
# Args: all.yaml file path

import os
import sys

PATH=sys.argv[1]

with open(PATH, 'r') as f:
    lines = f.readlines()

f = None
dirs = []
for i in range(len(lines)):
    line = lines[i]


    # Make a new file whenever '---' is encountered
    if line.startswith('---'):
        # Close the previous file
        if f is not None:
            f.close()
    
        # Open a new file
        dirname = lines[i+1].split('/')[2].lower()
        filename = lines[i+1].split('/')[4].lower()
        if dirname not in dirs:
            dirs.append(dirname)

        # Create the directory if it doesn't exist
        if not os.path.exists(os.path.join(os.getcwd(), dirname)):
            os.makedirs(os.path.join(os.getcwd(), dirname))
        f = open(dirname + '/' + filename, 'w')
    
    # Write to the file
    f.write(line)

print(' '.join(dirs))
