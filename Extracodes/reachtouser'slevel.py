users = {
    "omer": {
        "level": 7
    },
    "yusuf": {
        "level": 4
    },
    "esra": {
        "level": 1
    }
}
name = "omer"
for i, j in users.items():
    if i == name:
        print(j["level"])
