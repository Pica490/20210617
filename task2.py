import hashlib
import json

with open('result.json', encoding='utf-8') as f:
    data = json.loads(f.read())

def gen_hash(start,end):

    while start < end:
        yield start
        start += 1

for item in gen_hash(0, len(data)-1):
    print(hashlib.md5(data[item].encode('utf-8')).hexdigest())


