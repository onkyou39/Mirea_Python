from math import cos


def main(m, y, a):
    result = 0
    for i in range(1, m + 1):
        result += (((1 + 23 * y ** 2 + i ** 3) ** 4) / 31) \
              - 60 * i ** 6 - 39 * cos(i) ** 5
    for c in range(1, a + 1):
        result -= (c ** 3 - 45 * y) ** 7 + c ** 3
    return result
  
