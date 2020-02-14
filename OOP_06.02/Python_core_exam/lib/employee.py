from abc import ABC, abstractclassmethod


class Employee(ABC):
    __id = 0

    # @abstractclassmethod
    def __init__(self, name:str, surname:str, age:int, salary:int):
        # self.__id += 1
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__salary = salary

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def show_info(self):
        print("Name: ", self.__name, "\nSurname: ",  self.__surname,
              "\nAge: ",  self.__age, "\nSalary: ",  self.__salary)
