from datetime import datetime

def my_random(x, y):
    '''
    :param x: int
    :param y: int
    :return: int
    '''
    minutes, secs, microsecs = datetime.now().minute, datetime.now().second, datetime.now().microsecond
    secs = secs if secs > 0 else 1
    minutes = minutes if minutes > 0 else 1
    n = microsecs // (secs + minutes)
    return n % (y - x + 1) + x

def summ(pix, i, j, mx, my) -> float:
    '''
    in fact calculating average of some near pixels
    :param pix: matrix
    :param i: int
    :param j: int
    :param mx: int
    :param my: int
    :return: float
    '''
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
