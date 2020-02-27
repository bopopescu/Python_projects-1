from lib.db_manager import Db_manager


def manager():
    """db_manager based on classes"""
    exit = False
    while not exit:
        test = Db_manager("localhost", "root", "", "loginsystem")
        print("=========== DB Manager ==========")
        choice = int(input(
            "1. Register user \n2. Login \n3. Show users \n4. Delete user \n5. Exit \n"
        ))
        if choice < 1 or choice > 5:
            raise Exception("Number of choice must be 1...5!")
        print("Your choice is: ", choice, "\n")
        if choice == 1:
            a = test.register_user()
            print(a)
        if choice == 2:
            res = test.login_user()
            for item in res:
                print(item)
        if choice == 3:
            res = test.show_users()
            for item in res:
                print(item)
        if choice == 4:
            test.delete_user()
        if choice == 5:
            exit = True
            print("By!")

try:
    manager()
except Exception as e:
    print("Error => ", e)
