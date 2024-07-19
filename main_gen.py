from PIL import Image
from random import random  # later will be destructed
from datetime import datetime


def summ(pix, i, j, mx, my) -> float:
    '''
    :param pix:
    :param i:
    :param j:
    :param mx:
    :param my:
    :return: float
    '''
    # in fact calculating average of some near pixels
    if i == 0 and j == 0:
        return (pix[i + 1, j + 1][0] + pix[i, j + 1][0] + pix[i + 1, j][0]) / 3
    elif i == 0 and j == my - 1:
        return sum([pix[i + 1, j][0], pix[i + 1, j - 1][0], pix[i, j - 1][0]]) / 3
    elif i == mx - 1 and j == 0:
        return sum([pix[i - 1, j][0], pix[i - 1, j + 1][0], pix[i, j + 1][0]]) / 3
    elif i == mx - 1 and j == my - 1:
        return (pix[i - 1, j - 1][0] + pix[i - 1, j][0] + pix[i, j - 1][0]) / 3
    elif i == 0 and j != 0 and j != my - 1:
        a, b, c, d, e = pix[i + 1, j + 1][0], pix[i, j + 1][0], pix[i + 1, j][0], pix[i, j - 1][0], pix[i + 1, j - 1][0]
        return sum([a, b, c, d, e]) / 5
    elif i != 0 and i != mx - 1 and j == 0:
        return sum(
            [pix[i + 1, j + 1][0], pix[i, j + 1][0], pix[i + 1, j][0], pix[i - 1, j][0], pix[i - 1, j + 1][0]]) / 5
    elif i < mx - 1 and j < my - 1:
        return sum([pix[i - 1, j - 1][0], pix[i, j - 1][0], pix[i - 1, j][0], pix[i + 1, j + 1][0]]) / 4
    else:
        return sum([pix[i - 1, j - 1][0], pix[i, j - 1][0], pix[i - 1, j][0]]) / 3


colors = {0: (252, 186, 3), 1: (116, 214, 24), 2: (157, 252, 25), 3: (149, 237, 26), 4: (252, 188, 25),
          5: (24, 176, 214), 6: (38, 189, 235)}  # colors: 2 sand, 3 grass n 2 water

im = Image.new("RGB", (50, 50), (6, 6, 6))
x, y = im.size
pix = im.load()
for i in range(9):
    pix[0, random() * (y - 1)] = (0, 0, 0)
for i in range(7):
    pix[random() * (x - 1), 0] = (0, 0, 0)  # a bit of fun

for i in range(x):
    for j in range(y):
        val = summ(pix, i, j, x, y)
        if val < 2 and random() > 0.7:
            val += 1  # less grass more water

        # a = a if a > 0.7 else 0.6
        val = val * (random() + 0.3)  # a bit more random
        val = 6 if round(val) > 6 else round(val)  # i made 6 colors only
        pix[i, j] = (val, val, val)  # it is temporary cuz i cant put an <int> here

for i in range(x):
    for j in range(y):
        pix[i, j] = colors[pix[i, j][0]] # finally the colors of map

im.save('result.jpg')
