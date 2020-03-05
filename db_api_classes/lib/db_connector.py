import requests
import mysql.connector

if __name__ == "__main__":
    pass

class Db_connector:

    def __init__(self, host:str, user:str, passwd:str):
        # self.__host = host
        # self.__user = user
        # self.__passwd = passwd
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
    @property
    def db(self):
        return self.__db

    # @property
    # def host(self):
    #     return self.__host

    # @host.setter
    # def host(self, host):
    #     self.__host = host

    # @property
    # def user(self):
    #     return self.__user

    # @user.setter
    # def user(self, user):
    #     self.__user = user

    # @property
    # def passwd(self):
    #     return self.__passwd 

    # @passwd.setter
    # def passwd(self, passwd):
    #     self.__passwd = passwd

    # def connection(self):
    #     self.__db.cursor()

    def test(self):
        a = True
        return a





