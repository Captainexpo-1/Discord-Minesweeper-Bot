"""
Minesweeper map generator for discord using spoiler formatting.
"""

import random

a = []


# A horrible function that could be a lot better with little work, but I don't care.
def around(x, y, size):
    count = 0
    try:
        if (a[y + 1][x + 1] == "💣" and x < size and y < size):
            count += 1
    except:
        1 == 1
    try:
        if (a[y - 1][x - 1] == "💣" and x > 0 and y > 0):
            count += 1
    except:
        1 == 1
    try:
        if (a[y - 1][x + 1] == "💣" and x < size and y > 0):
            count += 1
    except:
        1 == 1
    try:
        if (a[y + 1][x - 1] == "💣" and x > 0 and y < size):
            count += 1
    except:
        1 == 1
    try:
        if (a[y - 1][x] == "💣" and y > 0):
            count += 1
    except:
        1 == 1
    try:
        if (a[y + 1][x] == "💣" and y < size):
            count += 1
    except:
        1 == 1
    try:
        if (a[y][x - 1] == "💣" and x > 0):
            count += 1
    except:
        1 == 1
    try:
        if (a[y][x + 1] == "💣" and x < size):
            count += 1
    except:
        1 == 1
    return count


def GenerateMap(difficulty, size):
    bombs = 1-difficulty/100
    for i in range(size):
        n = []
        for j in range(size):
            if (random.random() > bombs):
                n.append("💣")
            else:
                n.append("⬜")
        a.append(n)
    j = ""
    numbers = "zero one two three four five six seven eight".split(" ")
    hint = False
    c = [0, 0]
    for y in range(size):
        j += "\n"
        for x in range(size):
            if (a[y][x] == "⬜"):
                a[y][x] = ":" + numbers[around(x, y, size)] + ":"
                if hint == False and around(x, y, size) == 0:
                    j += "**" + a[y][x] + "**"
                    hint = True
                else:
                    j += "||" + a[y][x] + "||"

            else:
                j += "||" + a[y][x] + "||"

    return j
