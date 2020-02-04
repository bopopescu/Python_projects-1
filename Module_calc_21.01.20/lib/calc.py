if __name__ == "main":
    plus()
    minus()
    mult()
    dev()

# def plus(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res

# def minus(*params):
#     res = 0
#     for item in params:
#         res -= item
#     return res

# def mult(*params):
#     res = 0
#     for item in params:
#         res *= item
#     return res

# def dev(*params):
#     res = 0
#     for item in params:
#         res /= item
#     return res
#-----------------------------------
def plus(a, b):
    res = a + b
    return res
    
def minus(a, b):
    res = a - b
    return res

def mult(a, b):
    res = a * b
    return res
def dev(a, b):
    res = a / b
    return res
