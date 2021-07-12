import json
import requests
import os

class CountriesIterate:

    def __init__(self):
        self.list_names = None

    def __iter__(self):
        self.get_list()

        return self

    def __next__(self):
        if not self.list_names:
            raise StopIteration
        wiki_page = self.list_names.pop()
        wiki_page = wiki_page.replace(' ','_')
        requests.get(f'https://en.wikipedia.org/wiki/{wiki_page}')
        return (f'{wiki_page} - https://en.wikipedia.org/wiki/{wiki_page}')

    def get_list(self):
        with open('countries/countries.json', encoding='utf-8') as f:
            data = json.loads(f.read())
            self.list_names = [name['name']['official'] for name in data]


for country in CountriesIterate():

    a = []
    if not os.path.isfile('result.json'):
        a.append(country)
        with open('result.json', mode='w') as f:
            f.write(json.dumps(a, indent=2))
    else:
        with open('result.json') as feedsjson:
            feeds = json.load(feedsjson)
        feeds.append(country)
        with open('result.json', mode='w') as f:
            f.write(json.dumps(feeds, indent=2))