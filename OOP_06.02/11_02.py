class Person:

    def __init__(self, name:str,  surname:str, age:int):
        self.__name: str = name
        self.__surname: str = surname
        self.__age: int = age

    def show_person_info(self):
        print("name: ", self.__name, "\nsurname: ",
              self.__surname, "\nage: ", self.__age, "\nPosition: ", self.__position, "\nSkills: ", self.__skills)    

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        self.__name = new_name    

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

# gvido = Person("Gvido", "Van Rossum", 47)
# gvido.show_person_info()
# print("-------------")
# print("property before", gvido.name)
# gvido.name = "Petya"
# gvido.show_person_info()
# print("property after", gvido.name)
bill = Person("Bill", "Geitch", 55)
bill.show_person_info()
print(bill.name, "\n")

class Junior(Person):
    def __init__(self, name:str,  surname:str, age:int, skills:str, position:str):
        
        Person.__init__(self, name, surname, age)
        self.__skills = skills
        self.__position = position

    def show_person_info(self):
        print("Name: ", self.name, "\nSurname: ", self.surname, "\nAge: ", self.age, "\nPosition: ", self.__position, "\nSkills: ", self.__skills)

jun = Junior("Adam", "Dobson", 23, "write code using Stake Owerflow", "Full stack Overflow Developer")
jun.show_person_info()
jun.name = "Adamus"
jun.surname = "Dobsunos"
jun.age = 24
jun.show_person_info()
    


