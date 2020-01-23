if __name__ == "main":
    calc_ansv()


def calc_ansv():

    print("\nQuestion 1.\n Python was created by .... during 1985- 1990 ")
    ans1 = int(input("Coose from variants: \n1 - James Gosling,\n2 - Guido van Rossum \n3 - Tim Berners-Lee \n\tEnter a number of answer: "))

    print("\nQuestion 2. \nWhat gets printed? \n\tprint(type(1/2)) ")
    ans2 = int(input("Coose from variants: \n1 - class 'number',\n2 - class 'tuple' \n3 - class 'float'\n4 - class 'double' \n\tEnter a number of answer: "))

    print("\nQuestion 3.\n names1 = ['Amir', 'Barry', 'Chales', 'Dao']\n if 'amir' in names1:\n \tprint(1)\n else:\n \tprint(2) ")
    ans3 = int(input("Coose from variants: \n1 - An exeption is thrown \n2 - 1 \n3 - 2\n\tEnter a number of answer: "))

    print("\nQuestion 4. What gets printed?\n x = 4.5 \n y = 2 \n print(x//y)")
    ans4 = int(input("Coose from variants: \n1 - 2.25 \n2 - 21 \n3 - 2.0 \n4 - 9.0, \n5 - 20.25 \n\tEnter a number of answer: "))

    print("\nQuestion 5. What gets printed?\n one = chr(104) \n two = chr(105) \n print(one + two) ")
    ans5 = int(input("Coose from variants: \n1 - 209 \n2 - h \n3 - hi \n4 - None \n5 - 104105 \n\tEnter a number of answer: "))

    print("\nQuestion 6. What gets printed? \n confusion = {}\n confusion[1] = 1 \n confusion['1'] = 2 \n confusion[1.0] = 4 \n sum = 0 \n for k in confusion: \n \tsum += confusion[k] \n print(sum)")
    ans6 = int(input("Coose from variants: \n1 - 2 \n2 - 6 \n3 - An exeption is thrown \n4 - 4 \n5 - 7 \n\tEnter a number of answer: "))

    print("\nQuestion 7. What gets printed? \n my_tuple = (1,2,3,4) \n my_tuple.append((5,6,7)) \n print(len(my_tuple)) ")
    ans7 = int(input("Coose from variants: \n1 - 7 \n2 - 5 \n3 - 2 \n4 - 1 \n5 - An exeption is thrown \n\tEnter a number of answer: "))

    print("\nQuestion 8. What gets printed? \n def myfunc(x,y,z,a): \n \tprint(x+y) \n nums = [1,2,3,4] \n myfunc(*nums)")
    ans8 = int(input("Coose from variants: \n1 - An exeption is thrown \n2 - 10 \n3 - 6 \n4 - 1 \n5 - 3 \n\tEnter a number of answer: "))

    print("\nQuestion 9. \n fo = open('foo.txt', 'wb')\n What is wb here? ")
    ans9 = int(input("Coose from variants: \n1 - The file name argument,\n2 - buffering value \n3 - access mode \n\tEnter a number of answer: "))

    print("\nQuestion 10. \n Python strings can have:")
    ans10 = int(input("Coose from variants: \n1 - just text \n2 - binary data and text \n3 - binary data, text and numbers\n\tEnter a number of answer: "))

    print("\nQuestion 11. What gets printed? \n position = fo.seek(0, 0) \nIt is:")
    ans11 = int(input("1 - Reposition pointer at the end \n2 - Reposition file fo at the begin of files list \n3 - Reposition pointer at the beginning \n4 - This method doesn't exist \n\tEnter a number of answer: "))

    print("\nQuestion 12. What gets printed?\n class Person: \n \tdef __init__(self, id): \n \t\tself.id = id \n obama = Person(100) \n obama.__dict__['age'] = 49 \n print(obama.age + len(obama.__dict__))")
    ans12 = int(input("Coose from variants: \n1 - 51 \n2 - 1 \n3 - 49 \n4 - 2 \n5 - 50 \n\tEnter a number of answer: "))

    res_correct = 0   
    if ans1 == 2:
        res_correct += 1
    if ans2 == 3:
        res_correct += 1
    if ans3 == 3:
        res_correct += 1
    if ans4 == 3:
        res_correct += 1
    if ans5 == 3:
        res_correct += 1
    if ans6 == 2:
        res_correct += 1
    if ans7 == 1:
        res_correct += 1
    if ans8 == 3:
        res_correct += 1
    if ans9 == 3:
        res_correct += 1
    if ans10 == 2:
        res_correct += 1
    if ans11 == 3:
        res_correct += 2
    if ans12 == 1:
        res_correct += 1    
   
    if res_correct < 4:
        print("Незадовільно!\n")
    elif res_correct >= 4 and res_correct <= 6:
        print("Задовільно!\n")
    elif res_correct >= 7 and res_correct <= 9:
        print("Добре!\n")
    elif res_correct >= 10 and res_correct <= 12:
        print("Відмінно!\n")