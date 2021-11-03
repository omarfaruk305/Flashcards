import json
from os import name


class Users:

    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    @classmethod
    def readjson_user(cls):
        with open("users.json") as f:
            cls.users_dict = json.load(f)

    @classmethod
    def save_to_json(cls, self):
        cls.readjson_user()
        cls.users_dict[self.name] = {"level": self.level}
        with open("users.json", "w") as f:
            json.dump(cls.users_dict, f, indent=2)

    def checkname(self):
        for names in Users.users_dict.keys():
            if self.name == names:
                return True
            else:
                pass
