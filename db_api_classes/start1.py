import requests
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE IF NOT EXISTS bank")


mycursor.execute("USE bank")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS  bankomats (id INT AUTO_INCREMENT PRIMARY KEY, address VARCHAR(255), city VARCHAR(255), latitude VARCHAR(255), longitude VARCHAR(255))")


URL = "https://api.privatbank.ua/p24api/infrastructure?json&tso&address=&city=Rivne"
response = requests.get(URL)
# print("res Result = {0}, response")
data = response.json()

for item in data["devices"]:
    address_new = item["fullAddressEn"]
    city_new = item["cityEN"]
    latitude_new = item["latitude"]
    longitude_new = item["longitude"]

    sql = "INSERT INTO bankomats (address, city, latitude, longitude) VALUES (%s, %s, %s, %s)"
    val = (address_new, city_new, latitude_new, longitude_new)
    mycursor.execute(sql, val)
    mydb.commit()

#     print(item["fullAddressEn"] + "\n" + item["latitude"]+ "\n" + item["longitude"] + "\n")
# print("----------------------->")


# print(mydb)
