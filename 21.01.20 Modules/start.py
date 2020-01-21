from lib.calc import plus, minus, mult, dev

print("Hello! Choose an action! \n Enter 1,2,3,4 or 5")
print("1 - +")
print("2 - -")
print("3 - *")
print("4 - /")
print("5. Quit \n")

action = int(input("Enter action: "))
a = int(input("Enter a"))
b = int(input("Enter b"))


if action == 1:
    res = plus(a, b, 10)
    print("plus = ", res, "\n")
elif action == 2:
    res = minus(a, b)
    print("a-b= ", res, "\n")
elif action == 3:
    mult = res(a, b)
    print("a*b= ", res, "\n")
elif action == 4:
    dev = res(a, b)
    print("a/b= ", res, "\n")
    if b == 0:
        print("division by 0!")
else:
    print("Invalid choice. Enter a number! \n")
    exit
