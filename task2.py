import hashlib
import json

def gen_hash(path):

    with open(f'result.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        for string in data:
            yield hash(string)

path = f'result.json'
h = gen_hash(path)

for item in h:
    print(item)



