if __name__ == "main":
    calc_ansv()


def calc_ansv():

    print("Question 1. Is 'boolean' a type of data in Python? ")
    ans1 = int(input("1 - yes, 2 - no"))

    print("Question 2. Is 'int' a type of data in Python? ")
    ans2 = int(input("1 - yes, 2 - no"))

    print("Question 3. Is 'float' a type of data in Python? ")
    ans3 = int(input("1 - yes, 2 - no"))

    print("Question 4. Is 'complex' a type of data in Python? ")
    ans4 = int(input("1 - yes, 2 - no"))

    print("Question 5. Is 'str' a type of data in Python? ")
    ans5 = int(input("1 - yes, 2 - no"))

    print("Question 6. Is 'bytes' a type of data in Python? ")
    ans6 = int(input("1 - yes, 2 - no"))

    print("Question 7. Is 'bytes array' a type of data in Python? ")
    ans7 = int(input("1 - yes, 2 - no"))

    print("Question 8. Is 'list' a type of data in Python? ")
    ans8 = int(input("1 - yes, 2 - no"))

    print("Question 9. Is 'tuple' a type of data in Python? ")
    ans9 = int(input("1 - yes, 2 - no"))

    print("Question 10. Is 'set' a type of data in Python? ")
    ans10 = int(input("1 - yes, 2 - no"))

    print("Question 11. Is 'frozen set' a type of data in Python? ")
    ans11 = int(input("1 - yes, 2 - no"))

    print("Question 12. Is 'dict' a type of data in Python? ")
    ans12 = int(input("1 - yes, 2 - no"))

    res_correct = 0
    res_uncorrect = 0

    if ans1 == 1:
        res_correct += 1
    else:
        res_uncorrect += 1

    if ans2 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans3 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans4 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans5 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans6 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans7 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans8 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans9 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans10 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans11 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    if ans12 == 1:
        res_correct += 1
    else: res_uncorrect += 1

    print(res_correct)
