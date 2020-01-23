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

def minus(*params):
    res = 0
    for item in params:
        res -= item
    return res

def mult(*params):
    res = 0
    for item in params:
        res *= item
    return res

def dev(*params):
    res = 0
    for item in params:
        res /= item
    return res
