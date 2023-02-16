from math import atan


def main(n):
    if n == 0:
        return -0.16
    elif n == 1:
        return -0.11
    else:
        return 1 - main(n - 2) \
            ** 2 - atan(59 * main(n - 1) -
                        23 * main(n - 1)
                        ** 2 - main(n - 1)
                        ** 3 / 57) ** 3
