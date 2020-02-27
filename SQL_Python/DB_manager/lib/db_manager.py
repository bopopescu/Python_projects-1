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

    def register_user(self):
        cursor = self.__db.cursor()
        name_new = input("Enter your name: ")
        surname_new = input("Enter your surname: ")
        age_new = input("Enter your age: ")
        email_new = input("Enter your email: ")
        password_new = input("Enter your password: ")
        sql = "INSERT users (name, surname, age, email, password) VALUE (%s, %s, %s, %s, %s)"
        val = (name_new, surname_new, age_new, email_new, password_new)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        self.__db.commit()
        return result

        # sql = "SELECT email FROM users WHERE email =(%s)"
        # val = (email_new,)
        # res = cursor.fetchone()
        # print("This user already exist!")

        

        

    def login_user(self):
        cursor = self.__db.cursor()
        email_new = input("Enter your email: ")
        check_email = cursor.execute(
            "SELECT email FROM users WHERE email ='%s'")
        val = (email_new,)
        print(check_email)
        # if check_name == name_new:
        # password_new = input("Enter your password: ")
        # check_password = cursor.execute("SELECT password FROM users")
        #     if password_new == check_password:
        #         print("You are welcome!")
        #     else:
        #         print("Incorrect password!")
        # else:
        #     print("You mast register at first!")

    def show_users(self):
        cursor = self.__db.cursor()
        cursor.execute("SELECT name, surname, age, email, password FROM users")
        result = cursor.fetchall()
        return result
