if __name__ == "main":
    plus()
    minus()
    mult()
    dev()


def plus(*params):
    res = 0
    for item in params:
        res += item
    return res


def minus(a, b):
    return a-b


def mult(a, b):
    return a-b


def dev(a, b):
    return a-b
