import time


class levels:

    def readjsonword(self):
        self.wordsid = [i for i in range(1, 5000)]
        return self.wordsid

    def get_level_words(self, n):
        self.readjsonword()
        return self.wordsid[(n*20)-20:n*20]

    def totalprogress(self, level):
        return len((self.wordsid / 20) - level)  # yüzdelik ifade dönecek


class user:
    def __init__(self, name):
        self.name = name
        self.level = levels()

    @classmethod
    def readjsonuser(cls):
        return "cls.usernames"

    def checkname(self):
        self.readjsonuser()
        pass


class game:
    def __init__(self) -> None:
        self.user = user(input("name : "))

    def play(self):
        pass

    def backtomenu(self):
        pass

    def quit(self):
        "save user json"
        pass


flashcard = game()
flashcard.user.level.get_level_words(3)
