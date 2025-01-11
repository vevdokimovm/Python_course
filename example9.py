def f(x, y):
    try:
        return x / y
    except TypeError:
        print("Type error")

f(5, [])