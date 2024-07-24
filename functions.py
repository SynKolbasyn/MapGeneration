from datetime import datetime


last_int, last_float = 1, 0.1


def my_random(x=0, y=1):
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
        print(n - int(n))
        return n - int(n)

    n = abs(int(microsecs // (secs + minutes) - last_int * 2))
    last_int = n
    if last_float <= 0:
        last_float = 2
    print(n % (y - x + 1) + x)
    return n % (y - x + 1) + x


def summ(pix, i, j, mx, my) -> float:
    """
    in fact calculating average of some near pixels
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
    elif j == 0 and i < mx - 1 :
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


def colors(n):
    """
    creating palette
    :param n: int
    :return: list
    """

    inp = list(tuple(map(int, input().split())) for _ in range(n))
    return inp


def dots(x, y, Col, pix):
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
    if Col >= 2:
        if my_random() > 0.6 and b + 1 < y and a + 1 < x:
            pix[a + 1, b + 1] = (1, 1, 1)
        if my_random() > 0.65 and b - 1 < y and a + 1 < x:
            pix[a + 1, b - 1] = (1, 1, 1)
        if my_random() > 0.6 and b + 1 < y and a - 1 < x:
            pix[a - 1, b + 1] = (1, 1, 1)
        if my_random() > 0.55 and b - 1 < y and a - 1 < x:
            pix[a - 1, b - 1] = (1, 1, 1)
