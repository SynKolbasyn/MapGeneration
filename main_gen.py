from PIL import Image
from random import random  # later will be destructed
import functions as fun


colors = {0: (252, 188, 25), 1: (149, 237, 26), 2: (157, 252, 25), 3: (116, 214, 24), 4: (252, 186, 3),
          5: (24, 176, 214), 6: (38, 189, 235)}  # colors: 2 sand, 3 grass n 2 water

def main(size, name):
    im = Image.new("RGB", size, (6, 6, 6))
    x, y = im.size
    pix = im.load()
    for i in range(15):
        pix[fun.my_random() * (x - 1), fun.my_random() * (y - 1)] = (0, 0, 0)  # a bit of fun

    for i in range(x):
        for j in range(y):
            val = fun.summ(pix, i, j, x, y)
            if val < 4 and random() > 0.65:
                val += 1  # less grass more water

            # a = a if a > 0.7 else 0.6
            val = val * (random() + 0.3)  # a bit more random
            val = 6 if round(val) > 6 else round(val)  # i made 6 colors only
            pix[i, j] = (val, val, val)  # it is temporary cuz i cant put an <int> here

    for i in range(x):
        for j in range(y):
            pix[i, j] = colors[pix[i, j][0]] # finally the colors of map

    im.save(f'{name}.jpg')


main((40, 40), 'result')
