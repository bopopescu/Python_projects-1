from lib.dbf_manager import Dbf_manager


def dbf_manager():
    """db_manager based on api & class"""
    exit = False
    while not exit: 
        print("=========== DB Manager (api & class) ==========")      
        manager = Dbf_manager("localhost", "root", "")
        choice = int(input(
            "1. Get data by city \n2. Insert data into DB \n3. Select by city \n4. Select by street \n5. Delete by city \n6. Exit \n"
        ))
        if choice < 1 or choice > 6:
                raise Exception("Number of choice must be 1...6!")
        print("Your choice is: ",choice,"\n")
        if choice == 1:
            data = manager.get_data_by_city()
            for item in data:
                print(item)

        elif choice == 2:
            manager.insert_data_into_db()

        elif choice == 3:
            res = manager.select_by_city()
            for item in res:
                print(item)

        elif choice == 4:
            res = manager.select_by_street()
            for item in res:
                print(item)

        elif choice == 5:
            manager.delete_by_city()

        elif choice == 6:
            exit = True

dbf_manager()
