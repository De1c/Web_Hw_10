import json

final_load = []

with open("authors.json", 'r', encoding='utf-8') as a:
    author = json.load(a)
    count = 1
    for el in author:
        one_author = {"model": "quotesapp.author",
                      "pk": count,
                      "fields": {"fullname": el['fullname'][0],
                                 "born_date": el['born_date'][0],
                                 "born_location": el['born_location'][0],
                                 "description": el['description']}}
        final_load.append(one_author)
        count += 1

print(final_load)

with open('final_authors.json', 'w', encoding='utf-8') as a:
    json.dump(final_load, a, ensure_ascii=False)