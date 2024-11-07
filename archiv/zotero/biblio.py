from pyzotero import zotero
import csv
import re
import os

ZOTERO_KEY = os.environ.get("ZOTERO_KEY")

zot = zotero.Zotero(9702503, "user", ZOTERO_KEY)

csv_file_path = r"C:\Users\Reinhard\Desktop\nabucco\data\csv\Bibliography.csv"
biblio_array = []
not_imported = []

with open(csv_file_path, "r", encoding="utf-8") as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)

    for row in csv_reader:
        biblio_array.append(row)
# print(ZOTERO_KEY)
for x in biblio_array:
    if x["Journal"]:
        template = zot.item_template("journalArticle")
        template["title"] = x["Title"]
        template["publicationTitle"] = x["Journal"]
        template["volume"] = x["Volume no."]
        template["date"] = x["Publication year"]
        template["pages"] = x["Pages"]
        template["volume"] = x["Volume no."]
        template["shortTitle"] = x["Short title"]
        template["creators"][0]["lastName"] = x["Author"].split(", ")[0]
        if len(x["Author"].split(", ")) >= 2:
            template["creators"][0]["firstName"] = x["Author"].split(", ")[1]
        else:
            template["creators"][0]["firstName"] = "-"
        resp = zot.create_items([template])
    elif x["Book"] and x["Editor"]:
        template = zot.item_template("bookSection")
        template["title"] = x["Title"]
        template["bookTitle"] = x["Book"]
        template["pages"] = x["Pages"]
        template["date"] = x["Publication year"]
        template["shortTitle"] = x["Short title"]
        template["creators"][0]["lastName"] = x["Author"].split(", ")[0]
        if len(x["Author"].split(", ")) >= 2:
            template["creators"][0]["firstName"] = x["Author"].split(", ")[1]
        else:
            template["creators"][0]["firstName"] = "-"
        # print(template)
        resp = zot.create_items([template])
    elif (
        not x["Book"]
        and not x["Editor"]
        and not x["Journal"]
        and len(x["Short title"].split(" ")) == 2
    ):
        # the data is is mess: accepted as BOOK are entries that use as short title "Author-Year"
        if re.match(r"[0-9]{4}$", x["Short title"].split(" ")[1]):
            template = zot.item_template("book")
            template["title"] = x["Title"]
            template["date"] = x["Publication year"]
            template["shortTitle"] = x["Short title"]
            template["creators"][0]["lastName"] = x["Author"].split(", ")[0]
            if len(x["Author"].split(", ")) >= 2:
                template["creators"][0]["firstName"] = x["Author"].split(", ")[1]
            else:
                template["creators"][0]["firstName"] = "-"
            resp = zot.create_items([template])
    else:
        not_imported.append(x)
