from lib.empl import Employee
from lib.dev import Developer

try:
    emp1 = Developer("Bill", "Gates", 44, 3000, "C++")
    print(emp1.name)

    # emp2 = Developer("Stive", "Gates", 34, 2000, "Java Script")
    # print(emp2.name)
    # test = Employee("tEST", "TEST2", 12, 2112)
    
    emp1.show_info()

except Exception as e:
    print("Error => ", e)
