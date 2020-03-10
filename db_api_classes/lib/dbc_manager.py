import mysql.connector
import requests
from lib.db_connector import Db_connector


if __name__ == "__main__":
    dbc_manager()


def dbc_manager():
   
    test = Db_connector("localhost", "root", "")
    db = test.db
    cursor = db.cursor()      
    cursor.execute("CREATE DATABASE IF NOT EXISTS bank_c")

    # check = Dbc_connector.test
    # if check:
    #     print("Yes!")

    
