def zero(x, left, middle, right):
    if x[0] == 1958:
        return left
    if x[0] == 1977:
        return middle
    return right


def main(x):
    if x[1] == 1976:
        if x[3] == 'XPROC':
            return zero(x, 0, 1, 2)
        if x[3] == 'AMPL':
            return zero(x, 4, 5, 6)
        return 3
    if x[1] == 1970:
        if x[3] == 'XPROC':
            return zero(x, 8, 9, 10)
        if x[3] == 'AMPL':
            return 12
        return 11
    return 7
