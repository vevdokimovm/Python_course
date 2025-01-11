def foo():
    assert 0 == 1

try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")