import json

all_tags = []
final_load = []

with open("quotes.json", 'r', encoding='utf-8') as t:
    data = json.load(t)
    for quote in data:
        lists_of_tags = quote['tags']
        for tag in lists_of_tags:
            all_tags.append(tag)

count = 1
for el in set(all_tags):
    structure = {"model": 'quotesapp.tag',
                 "pk": count,
                 "fields": {"name": el}}
    final_load.append(structure)
    count += 1

with open('final_tags.json', 'w', encoding='utf-8') as t:
    json.dump(final_load, t, ensure_ascii=False)