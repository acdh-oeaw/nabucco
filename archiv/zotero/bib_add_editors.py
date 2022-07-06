from pyzotero import zotero
import csv
import os

ZOTERO_KEY = os.environ.get('ZOTERO_KEY')

zot = zotero.Zotero(9702503, 'user', ZOTERO_KEY)
csv_file_path = r'C:\Users\Reinhard\Desktop\nabucco\data\csv\Bibliography.csv'

items = zot.everything(zot.items(itemType='bookSection'))
chapters = []
# x = zot.count_items()
# y = zot.collections()
for i in items:
    chapters.append(i)
    # print(i['data']['title'])
# print(chapters)
biblio_array = []

with open(csv_file_path, 'r', encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)

    for row in csv_reader:
        biblio_array.append(row)

template = zot.item_template('bookSection')
for c in chapters:
    for b in biblio_array:
        if c['data']['title'] == b['Title']:
            if len(b['Editor'].split(', ')) >= 2:
                c['data']['creators'].append({'creatorType': 'editor', 'firstName': b['Editor'].split(', ')[1],
                                              'lastName': b['Editor'].split(', ')[0]})
            else:
                c['data']['creators'].append({'creatorType': 'editor', 'firstName': '-',
                                              'lastName': b['Editor'].split(', ')[0]})
    print(c['data']['creators'])
    zot.update_item(c)
    # zot.check_items(chapters)
