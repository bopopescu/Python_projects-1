from random import randint

class Account:
    """ Card operations: create new account, add and take money, show info""" 

    def __init__(self, card_number, amount, currancy):        
        self.__card_number = card_number
        self.__amount = amount
        self.__currancy = currancy  

    def show_info(self):
        print("Card number: ", self.__card_number, "\nAmount: ", self.__amount, "\nCurrancy: ", self.__currancy)

    def add_money(self, added_mon):        
        self.__amount += added_mon
        return self.__amount

    def take_money(self, taked_mon):
        self.__amount -= taked_mon
        return self.__amount

exit = False
account_exist = False
while not exit:
    print("========= CardOperations =========")
    choice = int(input("1. Create an account \n2. Show info \n3. Add money \n4. Take money \n0. Exit\n"))        
    try:        
        if choice == 1:
            print('Creating an account: \n')
            amount = int(input("Enter amount of money for your new account: "))
            currancy = input("Enter currancy: UAN=G USD=$ EUR=E: ")
            card_number = randint(1000000, 9999999)        
            NewAccount = Account(card_number, amount, currancy)  
            account_exist = True         
        elif choice == 2:
            NewAccount.show_info()        
        elif choice == 3:
            if not account_exist:
                raise Exception("Creat an account at first!")
            else:
                how_much_add = int(input("Enter how much add: "))            
                NewAccount.add_money(how_much_add)
        elif choice == 4:
            if not account_exist:
                raise Exception("Creat an account at first!")
            else:
                how_much_take = int(input("Enter how much take: "))
                if amount > how_much_take:
                    NewAccount.take_money(how_much_take)
                else:
                    print("You have not anough money to take this summ, your money is - ", amount, "\n")
        elif choice == 0:
            exit = True
            print("By!")
        else:
            print("Please, enter a number from 1 to 3 or 0!")
    except Exception as error:
        print("Error => ", error)
   