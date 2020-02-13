from lib.empl import Employee


class Developer(Employee):
    def __init__(self, name, surname, age, salary, job):
        Employee.__init__(self, name, surname, age, salary)
        self.__job = job

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, job):
        self.__job = job

    def show_info(self):
        Employee.show_info(self)
        print("Job: ", self.job)

    # def save_in_file(self):
    #     with open("list.txt", "a") as our_list:
    #         our_list.write()
