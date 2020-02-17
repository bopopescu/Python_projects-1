import json
class Save:    
    def __init__(self, file_name:str, list1:list):
        self.__file_name:str = file_name 
        self.__list1:str = list1      

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        self.__file_name = file_name

    @property
    def list1(self):
        return self.__list1

    @list1.setter
    def list1(self, list1):
        self.__list1 = list1

    # Error =>  write() argument must be str, not list:
    # def save_in_file(self, file_name, list1):               
    #     with open(self.file_name, "a") as write_file:
    #         write_file.write(list1)    

    # Error =>  Object of type Tester is not JSON serializable:
    #   def save_in_file(self, file_name, list1):               
    #     with open(self.file_name, "a", encoding="utf-8") as write_file:
    #         json.dump(list1, write_file)

    def save_in_file(self, file_name, list1):               
        with open(self.file_name, "a") as write_file:            
            print(*list1, file = write_file, sep="\n")