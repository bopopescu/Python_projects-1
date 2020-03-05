import mysql.connector
import requests
from lib.db_connector import Db_connector


if __name__ == "__main__":
    dbc_manager()


def dbc_manager():
   
    Db_connector("localhost", "root", "")
    db = Db_connector.db
    cursor = db.cursor()      
    # cursor.execute("CREATE DATABASE IF NOT EXISTS bank_c")

    check = Dbc_connector.test
    if check:
        print("Yes!")

    
