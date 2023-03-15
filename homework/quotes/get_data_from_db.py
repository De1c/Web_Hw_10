import json

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.my_db


def change_id_to_name(id):
    authors = db.authors.find({})

    for author in authors:
        if str(author['_id']) == id:
            return author['fullname']

    return id


all_authors = []
dict_to_write = {}

result = db.authors.find({})
for el in result:
    dict_to_write['fullname'] = el['fullname'],
    dict_to_write['born_date'] = el['born_date'],
    dict_to_write['born_location'] = el['born_location'],
    dict_to_write['description'] = el['description']
    all_authors.append(dict_to_write)
    dict_to_write = {}

with open('quotes/authors.json', 'a', encoding='utf-8') as a_file:
    json.dump(all_authors, a_file, ensure_ascii=False)

all_quotes = []
temp_dict = {}

result = db.quotes.find({})
for el in result:
    temp_dict["tags"] = el["tags"]
    temp_dict["author"] = change_id_to_name(str(el["author"]))
    temp_dict["quote"] = el["quote"]
    all_quotes.append(temp_dict)
    temp_dict = {}

with open('quotes/quotes.json', 'a', encoding='utf-8') as q_file:
    json.dump(all_quotes, q_file, ensure_ascii=False)