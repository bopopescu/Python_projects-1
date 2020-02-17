from lib.dev import Developer
from lib.tester import Tester
from lib.hr import HR
from lib.pm import PM
from lib.ba import BA
from lib.save import Save
import json

if __name__ == "main":
    hr_manager()

list_employees = []

def show_employees():
    i = 1
    print("List of employees: \n")
    for item in list_employees:
        print(f"{i}.ID: {item.id} \n  Name: {item.name} \n  Surname: {item.surname} \n  Age: {item.age} \n  Salary: {item.salary} \n  Skills:{item.skills} \n ")
        # Job: {item.__name__} \n
        i += 1         

def hr_manager():
    """ hr manager based on classes"""

    count = 0
    if type(list_employees) is not list:
        raise Exception("Type of list_global must be a list!")
    exit = False
    while not exit:
        print("=========== HR Manager ==========")
        choice = int(input(
            "1. Show all employees \n2. Add new employee \n3. Remove employee \n4. Write in file \n"
        ))
        if choice < 1 or choice > 4:
                raise Exception("Number of choice must be 1...4!")
        print("Your choice is: ",choice,"\n")
        if choice == 1:
            if len(list_employees) == 0:
                print("List employees is empty yet ")
            else:
                show_employees()
        elif choice == 2:
            job = int(input(
                "Enter a job of new employee: \n1. Developer \n2. Tester \n3. HR \n4. PM \n5. BA \n"))
            if job < 1 or job > 5:
                raise Exception("Number of job must be 1...5!")
            name_e = str(input("Enter a name of new employee: "))
            surname_e = str(input("Enter a surname of new employee: "))
            age_e = str(input("Enter an age of new employee: "))
            salary_e = str(input("Enter a salary of new employee: "))
            skills_e = str(input("Enter a skills of new employee: "))
            if job == 1:
                worker = Developer(name_e, surname_e, age_e,                  salary_e, skills_e)                    
                list_employees.append(worker)
                count += 1
            elif job == 2:
                worker = Tester(name_e, surname_e, age_e, salary_e, skills_e)
                list_employees.append(worker)
                count += 1
            elif job == 3:
                worker = HR(name_e, surname_e, age_e, salary_e, skills_e)
                list_employees.append(worker)
                count += 1
            elif job == 4:
                worker = PM(name_e, surname_e, age_e, salary_e, skills_e)
                list_employees.append(worker)
                count += 1
            elif job == 5:
                worker = BA(name_e, surname_e, age_e, salary_e, skills_e)
                list_employees.append(worker)
                count += 1
            else:
                print("Number must be 1...5!")
            worker.id = count
        elif choice == 3:
            input("To see an ID of worker to remove press Enter")
            show_employees()            
            it_to_del1 = remove_worker(list_employees)            
            list_employees.remove(it_to_del1)
            list_after_del = []
            list_after_del.extend(list_employees)
            print("New list:")
            show_employees()
        elif choice == 4: 
            file_name = str(input("Enter name of file: \n"))

            #  якщо хочемо в то замість file_name ставимо file_name_json            
            # file_name_json = file_name+".json"
            # print(list_employees)
            # print(json.dumps(list_employees))
                               
            save = Save(file_name, list_employees)
            save.save_in_file(file_name, list_employees)        
        


def remove_worker(list_employees):
    id_to_remove = int(input("Enter Id of worker to remove: "))
    for item in list_employees:        
        if item.id == id_to_remove:
            item_to_del = item
            return item_to_del


