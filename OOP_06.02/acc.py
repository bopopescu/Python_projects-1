from random import randint

#  = 0
# currancy = "G"
# 

class Account:
    """ Card operations"""    
    def __init__(self, card_number, amount, currancy):        
        self.__card_number = card_number
        self.__amount = amount
        self.__currancy = currancy    
        

    def show_info(self):
        print("Card number: ", self.__card_number, "\nAmount: ", self.__amount, "\nCurrancy: ", self.__currancy)

    def change_currancy(self, curr):
        self.__currancy = curr

    def add_money(self, added_mon):        
        self.__amount += added_mon
        return self.__amount

    def take_money(self, taked_mon):
        self.__amount -= taked_mon
        return self.__amount

exit = False
while not exit:
    print("========= CardOperations =========")
    choice = int(input("1. Create an account \n2. Show info \n3. Change a currancy \n4. Add money \n5. Take money \n0. Exit\n"))        
    try:
        if choice == 1:
            print('Creating an account: \n')
            amount = int(input("Enter amount of money for your new account: "))
            currancy = input("Enter currancy: UAN=G USD=$ EUR=E: ")
            card_number = randint(1000000, 9999999)        
            NewAccount = Account(card_number, amount, currancy)           
        elif choice == 2:
            NewAccount.show_info()
        elif choice == 3:
            new_currancy = str("Enter currancy: UAN=G USD=$ EUR=E: ")
            NewAccount.change_currancy(new_currancy)
        elif choice == 4:
            how_much_add = int(input("Enter how much add: "))            
            NewAccount.add_money(how_much_add)
        elif choice == 5:
            how_much_take = int(input("Enter how much take: "))
            NewAccount.take_money(how_much_take)
        elif choice == 0:
            exit = True
            print("By!")
        else:
            print("Please, enter a number from 1 to 4 or 0!")
    except Exception as error:
        print("Error => ", error)
   