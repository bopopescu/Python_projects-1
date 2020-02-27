import mysql.connector
if __name__ == "main":
    pass


class Db_manager():

    def __init__(self, host: str, user: str, password: str, database: str):
        # self.__host = host
        # self.__user = user
        # self.__password = password
        # self.__database = database
        self.__db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="loginsystem"
        )

    def show_users(self):
        cursor = self.__db.cursor()
        cursor.execute("SELECT name, surname, age, email FROM users")
        result = cursor.fetchall()
        return result
        
    def register_user(self):
        cursor = self.__db.cursor()
        name_new = input("Enter your name: ")
        check_name = cursor.execute("SELECT name FROM users")
        if check_name:
            print("This user already exist!")
        else:
            surname_new = input("Enter your surname: ")
            age_new = input("Enter your age: ")
            email_new = input("Enter your email: ")
            cursor.execute(
                "INSERT users (name, surname, age, email) VALUE (name_new, surname_new, age_new, email_new)")
        result = cursor.fetchall()
        return result

    def login_user(self):
        cursor = self.__db.cursor()
        name_new = input("Enter your name: ")
        check_name = cursor.execute("SELECT name FROM users")        
        if check_name == name_new:
            password_new = input("Enter your password: ")
            check_password = cursor.execute("SELECT password FROM users")
            if password_new == check_password:
                print("You are welcome!")
            else:
                print("Incorrect password!")
        else:
            print("You mast register at first!")
        result = cursor.fetchall()
        return result



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
            test.register_user()            
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
