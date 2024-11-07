import glob
import pandas as pd
from collections import defaultdict
from acdh_xml_pyutils.xml import XMLReader

files = glob.glob("./data/xml/*.xml")

data = defaultdict(list)
for x in files:
    doc = XMLReader(x)
    for node in doc.tree.xpath(".//item"):
        item_type = (node.xpath("./itemType/name/text()")[0],)
        item = {
            "id": node.xpath("./@itemId")[0],
            "item_type": item_type,
            "item_type_id": node.xpath("./itemType/@itemTypeId")[0],
            "props": {},
        }
        for prop in node.xpath(".//element"):
            item["props"][f"{prop.xpath('./name/text()')[0]}"] = prop.xpath(
                ".//text/text()"
            )[0]
        data[item_type].append(item)

for x in data.keys():
    class_data = [item["props"] for item in data[x]]
    df = pd.DataFrame(class_data)
    df.to_csv(f"./data/csv/{x[0]}.csv", index=False)
