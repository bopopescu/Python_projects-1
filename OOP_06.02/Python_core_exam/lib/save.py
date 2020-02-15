class Save:
    file_name = str(input("Enter name of file in format 'name.extension': \n"))
    def __init__(self, file_name:str):
        self.__file_name:str = file_name

    # @property
    # def file_name(self):
    #     return self.__file_name

    # @file_name.setter
    # def file_name(self, file_name):
    #     self.__file_name = file_name

    def save_in_file(self):        
        with open(self.__file_name, "a") as our_list:
            our_list.write()