import json
import csv
with open("words.csv", "r") as f:
    reader = csv.reader(f)
    data = dict()
    next(reader)
    for row in reader:
        data[row[0]] = {"Dutch": row[2], "ENG": row[3], "Freq": row[1]}

willsortwods = list()
for i in data.values():
    willsortwods.append(list(i.items()))

sorteddict = dict()
datasorted = sorted(willsortwods, key=lambda x: int(x[2][1]), reverse=True)
id = 1
for i, j, k in datasorted:
    sorteddict[id] = {
        i[0]: i[1], j[0]: j[1], k[0]: k[1]}
    id += 1
with open("words.json", "w") as f:
    json.dump(sorteddict, f, indent=4)
