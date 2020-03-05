import mysql.connector
import requests

if __name__ == "__main__":
    pass


class Dbf_manager:
    def __init__(self, host:str, user:str, passwd:str):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()    

    def create_db_table(self):        
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS privat_bank")
        self.__cursor.execute("USE privat_bank")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS  bankomats (id INT AUTO_INCREMENT PRIMARY KEY, address VARCHAR(255), city VARCHAR(255), latitude VARCHAR(255), longitude VARCHAR(255))")

    def get_data_by_city(self):
        city = input("Enter city for inserting: ")
        URL = f"https://api.privatbank.ua/p24api/infrastructure?json&tso&address=&city={city}"
        response = requests.get(URL)      
        data = response.json()
        # print(data)
        return data

    def insert_data_into_db(self):
        self.create_db_table()
        data = self.get_data_by_city()

        for item in data["devices"]:
            address = item["fullAddressEn"]
            city = item["cityEN"]
            latitude = item["latitude"]
            longitude = item["longitude"]

            sql = "INSERT INTO bankomats (address, city, latitude, longitude) VALUES (%s, %s, %s, %s)"
            val = (address, city, latitude, longitude)
            self.__cursor.execute(sql, val)
            self.__db.commit()

    def select_by_city(self):
        self.__cursor.execute("USE privat_bank")
        city_for_select = input("Enter city for select: \n")
        sql = "SELECT * FROM bankomats WHERE city = %s"
        val = (city_for_select,)
        self.__cursor.execute(sql, val)
        result = self.__cursor.fetchall()
        return result

    def select_by_street(self):
        self.__cursor.execute("USE privat_bank")
        street_for_select = input("Enter street for select: \n")
        # sql = "SELECT * FROM bankomats WHERE address LIKE '%(%s)%'"
        # val = (street_for_select,)
        # self.__cursor.execute(sql, val)
        self.__cursor.execute(f"SELECT * FROM bankomats WHERE address LIKE '%{street_for_select}%' ORDER BY address")        
        result = self.__cursor.fetchall()
        return result

    def delete_by_city(self):
        db_exist = True
        if db_exist:
            try:
                self.__cursor.execute("USE privat_bank")
                city_for_delete = input("Enter city for delete: \n")
                # sql = "DELETE FROM bankomats WHERE city = '%s'"
                # val = (city_for_delete,)
                # self.__cursor.execute(sql, val)
                self.__cursor.execute(f"DELETE FROM bankomats WHERE city = '{city_for_delete}'")
                
                self.__db.commit()
            except Exception as e:
                print("deleting err ==> ", e)
        else:
            print("db is not exist..")






        
            





            