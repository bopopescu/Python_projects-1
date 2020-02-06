class Person:
    def __init__(self, name):
        self.__name = name
        print("person constructor", self.__name)

    def __show_person(self):
        print("hello", self.__name)

    def __del__(self):
        print("Person destructor", self.__name)
    
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        if self.__name == new_name:
            print("The same name")
        else:
            self.__name = new_name
        return self.__name

# Jack = Person("Jack")
# Jack.__show_person()
# Bobick = Person("Bobik")
# Bobick.__show_person()
Bill = Person("Bill")
print(Bill.get_name())
print(Bill.set_name("Nick"))


