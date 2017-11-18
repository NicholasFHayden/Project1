import json

data = {}
data['row1'] = []
data['row1'].append({
    "type":"C",
    "cell":"H1299",
    "source":"Lady",
    "seq":"MetAP",
    "size":"50",
    "tissue":"Lung",
    "time":"m",
    "subtype":"epithelial",
    "culture":"emem",
    "advSus":"A",
    "application":"undergrad",
    "pubs":"na",
    "productsheets":"PDF",
    "institution":"UST"})

with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
