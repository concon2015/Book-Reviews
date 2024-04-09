from pathlib import Path
import json

path = Path('number.json')
number = input('What is your favorite number? ')
path.write_text(json.dumps(number))

path = Path('number.json')
content = path.read_text()
number = json.loads(content)
print(f'Your favorite number is {number}')