from lib.db_manager import Db_manager
if __name__ == "main":
    manager()


def manager():
    """db_manager based on classes"""
    exit = False
    while not exit:
        print("=========== DB Manager ==========")
        choice = int(input(
            "1. Register user \n2. Login \n3. Show users \n4. Delete user \n5. Exit \n"
        ))
        if choice < 1 or choice > 4:
            raise Exception("Number of choice must be 1...4!")
        print("Your choice is: ", choice, "\n")
        if choice == 1:
            print("Your choice is: ", choice, "\n")
            # name = input("User name: ")
            # surname = input("User surname: ")
            # age = int(input("User age: "))
            # email = input("User email: ")
            Db_manager.register
