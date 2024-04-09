from pathlib import Path

book = Path('mobydick.txt')

contents = book.read_text(encoding='utf-8').lower()

print(contents.count('the'))
print(contents.count('the '))
print(contents.count(' the '))