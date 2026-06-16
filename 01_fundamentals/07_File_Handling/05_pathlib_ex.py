# list all subdirectories inside root
from pathlib import Path
p=Path('/')
for subdir in p.iterdir():
    if subdir.is_dir():
        print(subdir)

#recursive search for all .py files in the root directory
p=Path.cwd()
files=p.rglob('.*py')
for f in files:
    print(f)

