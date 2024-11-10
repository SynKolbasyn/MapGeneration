from datetime import datetime
from time import perf_counter_ns
import os.path
from random import random
from PIL import Image
import pathlib

import sqlite3
# import sys
# from PyQt6.QtWidgets import QApplication

last_int, last_float = 1, 0.1
prev_rand = perf_counter_ns()


# If you want to use good random,
# just remove the "y" in the name of bad random function,
# and add "y" to the name of this function
def m_random(x: int = 0, y: int = 1):  # good
    """
    :param x: int
    :param y: int
    :return: int
    """
    global prev_rand
    a, c, m = 1103515245, 12345, 2 ** 31

    prev_rand = (a * prev_rand + c) % m

    if x == 0 and y == 1:
        return prev_rand / m

    return x + prev_rand % (y - x)


def my_random(x=0, y=1):  # bad
    """
    :param x: int
    :param y: int
    :return: int
    """

    global last_float, last_int

    minutes, secs, microsecs = datetime.now().minute, datetime.now().second, datetime.now().microsecond

    secs = secs if secs > 0 else 1
    minutes = minutes if minutes > 0 else 1

    if x == 0 and y == 1:
        n = abs(microsecs / (secs + minutes) - last_float * 2)
        last_float = n
        if last_float <= 0.0:
            last_float = 0.2
        return n - int(n)

    n = abs(int(microsecs // (secs + minutes) - last_int * 2))
    last_int = n
    if last_float <= 0:
        last_float = 2
    return n % (y - x + 1) + x


def summ(pix, i, j, mx, my) -> float:
    """
    in fact just calculating average of near pixels
    :param pix: matrix
    :param i: int
    :param j: int
    :param mx: int
    :param my: int
    :return: float
    """

    if i == 0 and j == 0:
        return sum([pix[i + 1, j + 1][0], pix[i, j + 1][0], pix[i + 1, j][0]]) / 3
    elif i == 0 and j == my - 1:
        return sum([pix[i + 1, j][0], pix[i + 1, j - 1][0], pix[i, j - 1][0]]) / 3
    elif i == mx - 1 and j == 0:
        return sum([pix[i - 1, j][0], pix[i - 1, j + 1][0], pix[i, j + 1][0]]) / 3
    elif i == mx - 1 and j == my - 1:
        return sum([pix[i - 1, j - 1][0] + pix[i - 1, j][0] + pix[i, j - 1][0]]) / 3

    elif i == 0 and j < my - 1:
        a, b, c, d, e = pix[i + 1, j + 1][0], pix[i, j + 1][0], pix[i + 1, j][0], pix[i, j - 1][0], pix[i + 1, j - 1][0]
        return sum([a, b, c, d, e]) / 5
    elif j == 0 and i < mx - 1:
        return sum(
            [pix[i + 1, j + 1][0], pix[i, j + 1][0], pix[i + 1, j][0], pix[i - 1, j][0], pix[i - 1, j + 1][0]]) / 5
    elif i == mx - 1 and j < my - 1:
        return sum([pix[i, j - 1][0], pix[i, j + 1][0], pix[i - 1, j - 1][0],
                    pix[i - 1, j + 1][0], pix[i - 1, j][0]]) / 5
    elif j == my - 1 and i < mx - 1:
        return sum([pix[i, j - 1][0], pix[i - 1, j - 1][0], pix[i + 1, j - 1][0],
                    pix[i - 1, j][0], pix[i + 1, j][0]]) / 5

    else:
        return sum([pix[i - 1, j - 1][0], pix[i + 1, j - 1][0], pix[i - 1, j + 1][0], pix[i + 1, j + 1][0],
                    pix[i, j + 1][0], pix[i, j - 1][0], pix[i + 1, j][0], pix[i - 1, j][0]]) / 8


def colors(form_col):
    """
    creating palette
    :param form_col: str
    :return: tuple | None
    """
    if form_col.text():
        try:
            r, g, b = form_col.text()[1:-1].split(',')
            r, g, b = int(r.strip(', .')), int(g.strip(', .')), int(b.strip(', .'))
        except Exception as err:
            return err
        return tuple([r, g, b])
    return None


def dots(x, y, col, pix):
    a, b = int(my_random() * (x - 1)), int(my_random() * (y - 1))
    pix[a, b] = (0, 0, 0)  # a bit of fun
    if my_random() > 0.6 and a + 1 < x:
        pix[a + 1, b] = (0, 0, 0)
    if my_random() > 0.2 and b - 1 >= 0:
        pix[a, b - 1] = (0, 0, 0)
    if my_random() > 0.4 and a - 1 >= 0:
        pix[a - 1, b] = (0, 0, 0)
    if my_random() > 0.5 and b + 1 < y:
        pix[a, b + 1] = (0, 0, 0)
    if col >= 2:
        if my_random() > 0.6 and b + 1 < y and a + 1 < x:
            pix[a + 1, b + 1] = (1, 1, 1)
        if my_random() > 0.65 and b - 1 < y and a + 1 < x:
            pix[a + 1, b - 1] = (1, 1, 1)
        if my_random() > 0.6 and b + 1 < y and a - 1 < x:
            pix[a - 1, b + 1] = (1, 1, 1)
        if my_random() > 0.55 and b - 1 < y and a - 1 < x:
            pix[a - 1, b - 1] = (1, 1, 1)


# based colors: 2 sand, 3 grass n 2 water
colors1 = [(116, 214, 24), (252, 188, 25), (38, 189, 235)]


# TODO: enter those in ui form as default ^^^


def creating_func(size: tuple, name: str, palette: list):
    """

    :param size: tuple
    :param name: str
    :param palette: list
    :return: image
    """
    Col = len(palette) - 1
    im = Image.new("RGB", size, (Col, Col, Col))
    x, y = size
    pix = im.load()
    for i in range(20):
        dots(x, y, Col, pix)

    for j in range(y):
        for i in range(x):
            val = summ(pix, i, j, x, y)
            val = val * (random() + 0.3)  # a bit more random

            val = Col if round(val) > Col else round(val)

            if val == Col // 2 and random() > 0.45:  # less sand more water or whatever
                val = val - 1 if random() > 0.45 else val + 1

            # if round(fun.summ(pix, i, j, x, y)) != val: <-- bad problem solving

            pix[i, j] = (val, val, val)  # it is temporary cuz I cant put an <int> here

    for i in range(x):
        for j in range(y):
            pix[i, j] = palette[pix[i, j][0]]  # finally the colors of map

    if not os.path.exists("generated/"):
        os.mkdir("generated/")
    im.save(f'generated/{name}.png')
    return None
    # TODO: connect with db


def db_request(name):
    db = sqlite3.connect("../db/database.sqlite")
    cur = db.cursor()
    try:
        result = cur.execute(f"""SELECT image FROM generations WHERE name = '{name}';""").fetchone()
        print(type(result))
        return result
    except Exception as err:
        return (err,)

# a = len(db_request("aboba1")) // 3
# im = Image.new(mode="RGB", size=(int(a ** 0.5), int(a ** 0.5)))
# im.frombytes(db_request("aboba1"))
# im.show()