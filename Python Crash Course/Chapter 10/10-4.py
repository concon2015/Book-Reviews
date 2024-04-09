from pathlib import Path
name = input("What is your name? ")

path = Path('guest.txt')
path.write_text(name)