from math import log


def main(x):
    if x < 165:
        return 20 * log(x, 10) ** 7
    if 165 <= x < 256:
        return (91 + 24 * x ** 2 + 5 * x ** 3) \
            ** 7 + 41 * log(x, 10) ** 5
    if 256 <= x < 273:
        return x - 1
    else:
        return x ** 6 - (x ** 2 - 76 - 92 * x ** 3) \
            ** 7 - 55 * (1 + x ** 2) ** 3
