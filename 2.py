# --------------Ex1-----------------
def part_of_day():
    hour=int(input("Enter a hour from 0 to 24\n"))

    if hour>=6 and hour<12:
        print("Good morning!")        
    elif hour>=12 and hour<18:
        print("Good day!")        
    elif hour>=18 and hour<22:
        print("Good evening!")        
    elif hour>=22 and hour<=24: 
    #and hour>=0 and hour<6:
        print("Good night!")        
    elif hour>=0 and hour<6:
        print("Good night!")        
    else:
        print("Enter a number from 0 to 24")         
part_of_day() 

# --------------Ex2-----------------
def connverter():
    print("\n Hello! What do you want to convert?\n Enter 1, 2 or 3 \n")
    print("1. Convert inch to sm")
    print("2. Convert sm to inch")
    print("3. Quit \n")    
    try:
        choice=int(input("Enter choice: "))
        if choice==1:
            inch_to_sm()
            exit                
        elif choice==2:
            inch_to_sm()
            exit                
        elif choice==3:
            exit            
        else:
            print("Invalid choice. Enter 1-3 \n")
            exit            
    except ValueError:
        print("Invalid choice. Enter 1-3 \n")
        exit
    
def inch_to_sm():
    inch=int(input("Enter inch: "))
    result=round(inch*2.54, 1)
    print(result, " sm \n")

def inch_to_sm():
    sm=int(input("Enter sm: "))
    result=round(sm/2.54, 1)
    print(result, "inch \n") 

connverter()

