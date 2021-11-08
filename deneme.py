import threading
import time
import os


def a():

    s = 0
    m = 0

    while s <= 60:
        os.system('cls')
        print(m, 'Minutes', s, 'Seconds')
        time.sleep(1)
        s += 1
        if s == 60:
            m += 1
            s = 0


def b():
    s = 0
    m = 0

    while s <= 60:
        os.system('cls')
        print(m, 'Minutes', s, 'Seconds')
        time.sleep(1)
        s += 1
        if s == 60:
            m += 1
            s = 0


threading.Thread(target=a).start()
threading.Thread(target=b).start()
