import mysql.connector

class Db_manager:

    test = 10
    
    def __init__(self, host: str, user: str, password: str, database: str):
        # self.__host = host
        # self.__user = user
        # self.__password = password
        # self.__database = database
    
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = db.cursor()
    def test_connection():
        self.cursor.execute("SHOW TABLES")


    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        self.__host = host

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, cursor):
        self.__cursor = cursor

    def register(self):


