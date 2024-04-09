from pathlib import Path

files = 'dogs.txt', 'cats.txt', 'lizards.txt'

for file in files:
    try:
        path = Path(file)
        print(path.read_text())
    except FileNotFoundError:
        print(f'File {file} not found')