from random import randint


class Account:
    """ Card """
    print("=========CardOperation=========")
    choice = int(input(
            "1. Show info \n2. Take money \n3. Add money"
        ))
    print("your choice is => ", choice)
    def __init__(self, card_number, amount, currancy):
            self.__card_number = card_number
            self.__amount = amount
            self.__currancy = currancy
            print("Account constructor")
    exit = False
    while not exit:
    
        if choice == 1:
            show_info()
        elif choice == 2:
            take_money()
        elif choice == 3:
            take_money()

    def show_info(self):
        print("Card number: ", self.__card_number, "\nAmount: ",
            self.__amount, "\nCurrancy: ", self.__currancy)
    def take_money(self):
        how_much_take = int(input("Enter how much take: "))
        self.__amount -= how_much_take
        return self.__amount
    def add_money(self):
        how_much_add = int(input("Enter how much add: "))
        self.__amount += how_much_add
        return self.__amount    


amount = int(input("Enter money "))
currancy = input("Enter currancy: UAN=G USD=$ EUR=E: ")
card_number = randint(1000000, 9999999)

credit_card = Account(card_number, amount, currancy)
credit_card.show_info()
credit_card.take_money()
credit_card.show_info()
credit_card.add_money()
credit_card.show_info()

