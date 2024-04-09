from pathlib import Path
import json

def get_number():
    path = Path('number.json')
    if path.exists():
        content = path.read_text()
        number = json.loads(content)
        print(f'Your favorite number is {number}')
    else:
        number = input('What is your favorite number? ')
        path.write_text(json.dumps(number))

get_number()