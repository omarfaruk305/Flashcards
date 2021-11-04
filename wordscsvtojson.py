import json
import csv
with open("words.csv", "r") as f:
    reader = csv.reader(f)
    data = dict()
    next(reader)
    for row in reader:
        data[row[0]] = {"Dutch": row[2], "ENG": row[3], "Freq": row[1]}
with open("words.json", "w") as f:
    json.dump(data, f, indent=4)
