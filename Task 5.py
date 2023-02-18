from math import ceil


def main(y):
    result = 0
    n = len(y) - 1
    for i in range(1, len(y) + 1):
        result += (1 - 32 * y[n + 1 - ceil(i / 3)]) ** 4
    return result
