import json

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="567234")


def replace_name_to_id(name):
    cursor = conn.cursor()
    SQL = "select * from quotesapp_author"
    cursor.execute(SQL)
    records = cursor.fetchall()
    for el in records:
        if name == el[1]:
            return el[0]
    return name


def replace_tags_to_id(tags):
    list_of_tags = []
    cursor = conn.cursor()
    SQL = "select * from quotesapp_tag"
    cursor.execute(SQL)
    records = cursor.fetchall()
    for el in records:
        for tag in tags:
            if tag == el[1]:
                list_of_tags.append(el[0])
    return list_of_tags


all_quotes = []
with open("quotes.json", 'r', encoding='utf-8') as t:
    data = json.load(t)
    count = 1
    for el in data:
        tags_id = replace_tags_to_id(el["tags"])
        author_id = replace_name_to_id(el["author"])
        structure = {"model": 'quotesapp.quote',
                     "pk": count,
                     "fields": {"text": el["quote"],
                                "tags": tags_id,
                                "author": author_id}}
        all_quotes.append(structure)
        count += 1

with open('final_quotes.json', 'w', encoding='utf-8') as q:
    json.dump(all_quotes, q, ensure_ascii=False)