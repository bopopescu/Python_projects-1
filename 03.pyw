""" day=0
while True:
    if day == 7:
            break
    temp = int(input("enter dey temperature "))
   
    day += 1
    if temp > 10:
        counter = 0
        counter += 1
    
print("Temp >10: ", counter, " times.") """

""" # ----------2v----------
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n") """

# ----------3v----------
""" from random import randint

trying = 1

while True:
    rand = randint(1,6)
    print(rand)
    if rand != 6:
        trying += 1
    else:
        break
print("Try number ", trying) """

# ----------4----------

from random import randint
plaing = True
my_score = 0
pc_score = 0
N = int(input("enter N"))
while plaing == True:
    rand_my_1 = randint(1, 6)
    print(rand_my_1)
    rand_my_2 = randint(1, 6)
    print(rand_my_2)
    my_score = rand_my_1 + rand_my_2
    if rand_my_1 == rand_my_2:
        my_score += 1
    print("my_score: ", my_score)
    input("your turn")

    rand_pc_1 = randint(1, 6)
    print(rand_pc_1)
    rand_pc_2 = randint(1, 6)
    print(rand_pc_2)
    pc_score = rand_pc_1 + rand_pc_2
    if rand_pc_1 == rand_pc_2:
        pc_score += 1
    print("pc_score: ", pc_score)
    input("your turn")

    if my_score >= N or pc_score >= N:
        plaing = False


""" exit = True
trying = 1

while True:
    rand = randint(1,6)
    print(rand)
    if rand != 6:
        trying += 1
    else:
        exit = False
print("Try number ", trying) """
