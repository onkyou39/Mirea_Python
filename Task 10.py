class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def smash(self):
        if self.state == 'C':
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'C'
            return 8
        raise MealyError('smash')

    def apply(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'B':
            self.state = 'G'
            return 2
        if self.state == 'D':
            self.state = 'G'
            return 6
        raise MealyError('apply')

    def jog(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('jog')


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.jog() == 0
    assert o.jog() == 1
    assert o.smash() == 4
    assert o.apply() == 3
    assert o.smash() == 5
    assert o.smash() == 8
    assert o.apply() == 3
    assert o.smash() == 5
    assert o.jog() == 7
    assert o.jog() == 9
    o = main()
    assert o.jog() == 0
    assert o.jog() == 1
    assert o.apply() == 3
    assert o.apply() == 6
    o = main()
    assert o.jog() == 0
    assert o.apply() == 2
    raises(lambda: o.jog(), MealyError)
    raises(lambda: o.apply(), MealyError)
    raises(lambda: o.smash(), MealyError)
