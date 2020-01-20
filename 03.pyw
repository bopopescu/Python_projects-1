
#----------1----------
def count_temp():
    """temp > 10 in week"""
    work = True
    day = 0
    count = 0
    while work:
        temp = int(input("Enter day temperature "))
        day += 1
        if temp > 10:
            count +=1
        if day == 7:
            break
    print("Temp >10: ", count, " times.")
# count_temp()

""" # ----------2v----------
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n") """
# ----------2v----------
def table():
    """table * n"""
    n = int(input("enter n: "))
    for i in range(1, 10):
        print(i, "*", n, "=", i*n, "\n")
# table()
# ----------3v----------
from random import randint

trying = 1

while True:
    rand = randint(1,6)
    print(rand)
    if rand != 6:
        trying += 1
    else:
        break
print("Try number ", trying) 



