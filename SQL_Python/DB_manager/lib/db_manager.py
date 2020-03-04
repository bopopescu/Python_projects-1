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
        age_new = int(input("Enter your age: "))
        email_new = input("Enter your email: ")
        password_new = input("Enter your password: ")

        sql = "INSERT users (name, surname, age, email, password) VALUES (%s, %s, %s, %s, %s)"
        val = (name_new, surname_new, age_new, email_new, password_new)
        cursor.execute(sql, val)
        
        self.__db.commit()
        # result = cursor.fetchall()        
        # return result        

    def login_user(self):
        cursor = self.__db.cursor()
        email_ent = input("Enter your email: ")
        sql = "SELECT * FROM users WHERE email = %s"
        val = (email_ent,)
        checked_email = cursor.execute(sql, val)        
        return checked_email
        # if checked_email is None:
        #     result = False
        #     return result
        # else:
        #     password_ent = input("Enter your password: ")
        #     sql = "SELECT password FROM users WHERE email ='%s'"
        #     val = (password_ent,)
        #     checked_password = cursor.execute(sql, val)            
        #     if password_ent == checked_password:                
        #         result = True
        #         return result
            

    def show_users(self):
        cursor = self.__db.cursor()
        cursor.execute("SELECT name, surname, age, email, password FROM users")
        result = cursor.fetchall()
        return result

    def delete_user(self):
        cursor = self.__db.cursor()
        email_ent = input("Enter your email: ")
        sql = "DELETE FROM users WHERE email = %s"
        val = (email_ent,)
        cursor.execute(sql, val)
        self.__db.commit()
        result = cursor.fetchall()
        return result
        

