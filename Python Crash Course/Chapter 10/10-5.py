from pathlib import Path
names = ''

while (True):
    current_name = input("What is your name?\nType 'q' to quit\n")
    if current_name == 'q':
        break
    else:
        names += current_name + '\n'

path = Path('guest_book.txt')
path.write_text(names)