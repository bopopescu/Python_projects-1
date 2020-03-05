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
        email_ent = input("Enter your email: ")
        try:
            sql = "SELECT * FROM users WHERE email = %s"
            val = (email_ent,)
            cursor.execute(sql, val)
            results = cursor.fetchall()
            for row in results:
                # id = row[0]
                # name = row[1]
                # surname = row[2]
                # age = row[3]
                email = row[4]
            if email:
                adding = False
                return adding
        except:
            name_new = input("Enter your name: ")
            surname_new = input("Enter your surname: ")
            age_new = int(input("Enter your age: "))            
            password_new = input("Enter your password: ")
            sql = "INSERT users (name, surname, age, email, password) VALUES (%s, %s, %s, %s, %s)"
            val = (name_new, surname_new, age_new, email_ent, password_new)
            cursor.execute(sql, val)
            self.__db.commit()
            adding = True
            return adding  

    def login_user(self):        
        cursor = self.__db.cursor()
        email_ent = input("Enter your email: ")
        try:
            sql = "SELECT * FROM users WHERE email = %s"
            val = (email_ent,)
            cursor.execute(sql, val)
            results = cursor.fetchall()
            for row in results:                
                email = row[4]
                password = row[5]
            if email:
                try:
                    passw_ent = input("Enter your password: ")
                    if password == passw_ent:                        
                        logining = True
                        return logining 
                    else:
                        print("Password is incorrect!")
                        logining = False
                        return logining

                except Exception as e:
                    print("err => ", e) 

        except:
            print("This email not registered!")
            logining = False
            return logining
            

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
        
        

