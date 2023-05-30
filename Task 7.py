def main(s):
    d = int(s)
    d1 = 0b111 & d
    d2 = 0b111111 & (d >> 3)
    d3 = 0b111 & (d >> 9)
    d4 = 0b1111111 & (d >> 12)
    d5 = 0b111 & (d >> 19)
    d6 = 0b1 & (d >> 22)
    result = {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5, 'D6': d6}
    return result
