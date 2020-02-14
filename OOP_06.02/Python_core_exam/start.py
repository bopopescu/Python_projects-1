from lib.employee import Employee
from lib.dev import Developer
# from lib.save import save
from lib.main import hr_manager

try:
    # emp1 = Developer("Bill", "Gates", 44, 3000, "C++")    
    # emp1.show_info()
    hr_manager()

except Exception as e:
    print("Error => ", e)
