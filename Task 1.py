from math import ceil, asin, atan, cos


def main(y):
    return (pow(y, 5) - 79 * pow(y, 9)) \
        / (58 * ceil(21 * pow(y, 2)) + 66 * pow(y, 5)) \
        - ((1 - 55 * pow(asin(y), 2)) / (
                98 * pow(atan(31 - pow(y, 2) / 96), 3)
                + pow(cos(y - 73), 4)))
