from lib.employee import Employee


class HR (Employee):
    def __init__(self, name:str, surname:str, age, salary, skills:str):
        Employee.__init__(self, name, surname, age, salary)
        self.__skills = skills
        
    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, skills):
        self.__skills = skills

    def show_info(self):
        Employee.show_info(self)
        print("Skills: ", self.__skills)