import os.path
from random import random

from PIL import Image

import functions as fun


# colors: 2 sand, 3 grass n 2 water
colors = [(252, 188, 25), (149, 237, 26), (157, 252, 25), (116, 214, 24), (252, 186, 3), (24, 176, 214), (38, 189, 235)]
colors1 = [(116, 214, 24), (252, 188, 25), (38, 189, 235)]
colors2 = [(116, 214, 24), (38, 189, 235)]


def main(size, name, palette):
    Col = len(palette) - 1
    im = Image.new("RGB", size, (Col, Col, Col))
    x, y = size
    pix = im.load()
    for i in range(20):
        fun.dots(x, y, Col, pix)

    for j in range(y):
        for i in range(x):
            val = fun.summ(pix, i, j, x, y)
            val = val * (random() + 0.3)  # a bit more random

            val = Col if round(val) > Col else round(val)

            if val == Col // 2 and random() > 0.45:  # less fuckin sand more water or whatever
                val = val - 1 if random() > 0.45 else val + 1

            # if round(fun.summ(pix, i, j, x, y)) != val:

            pix[i, j] = (val, val, val)  # it is temporary cuz i cant put an <int> here

    for i in range(x):
        for j in range(y):
            pix[i, j] = palette[pix[i, j][0]]  # finally the colors of map

    if not os.path.exists("generated/"):
        os.mkdir("generated/")
    im.save(f'generated/{name}.png')


if __name__ == "__main__":
    main((60, 60), 'image_1', colors1)
    main((60, 60), 'image_2', colors1)
    main((60, 60), 'image_3', colors1)
