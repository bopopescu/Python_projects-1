x = int(input("Enter start x: "))
y = int(input("Enter start y: "))
class Point:
    """Point"""
    def __init__(self, x, y):
        self.x = x  
        self.y = y 
        
    def show_coordinate(self):
        print("Now coordinates are: \n")
        print("x = ", self.x)
        print("y = ", self.y)
exit = False
while not exit:
    print("=========== Coordinates manager ==========")
    print("Enter a number from 1 to 3 or 0")
    choice = int(input(
        "1. Enter X:  \n2. Enter Y:  \n3. Show coordinate: \n0. Exit\n"))    
    try:
        if choice == 1:
            x = int(input("Enter x: "))
            print("x = ", x)
        elif choice == 2:
            y = int(input("Enter y: "))
            print("y = ", y)
        elif choice == 3:
            NewPoint = Point(x,y)
            NewPoint.show_coordinate()
        elif choice == 0:
            exit = True
            print("By! See you soon!")
        else:
            print("Please, enter a number from 1 to 3 or 0!")
    except Exception as error:
        print("Error => ", error)









