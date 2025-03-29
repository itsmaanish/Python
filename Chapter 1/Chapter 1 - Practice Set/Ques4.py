import os

# Specify the directory path
directory_path = '/Resume'

# List all entries in the directory
entries = os.listdir(directory_path)

# Iterate and print each entry
for entry in entries:
    print(entry)
