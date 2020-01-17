""" numb1 = int(input("enter 1 number\n"))
numb2 = int(input("enter 2 number\n"))
action = input("enter an action: + - * / \n")

if action == "+":
    print(numb1+numb2)
elif action == "-":
    print(numb1-numb2)
elif action == "*":
    print(numb1*numb2)
elif action == "/":
    if action==0:
        print("division by 0")
    else:
        print(numb1/numb2) """

m = int(input("enter a number of month\n"))
if m == 12 or m == 1 or m == 2:
    print("winter")
elif m == 3 or m == 4 or m == 5:
    print("spring")
elif m == 6 or m == 7 or m == 8:
    print("summer")
elif m == 9 or m == 10 or m == 11:
    print("autumn")
else:
    print("enter a number from 1 to 12")
