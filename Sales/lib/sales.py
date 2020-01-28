if __name__ == "main":
    start()


def start(items):
    db_items = items
    exit = False
    while not exit:
        print("============Sales Manager v 1.0==========")
        choice = int(input("1. Show Items\n2. Add Items\n0. Exit\n"))
        print(choice)
        if choice == 1:
            show_items(db_items)
        elif choice == 2:
            add(db_items)

        elif choice == 0:
            exit = True
            print("By!")
        else:
            print("R.T.F.M")


def show_items(items):
    print(items)


def add(items):
    vendor = input("Enter vendor")
    model = input("Enter model")
    price = input("Enter price")
    new_item = {"vendor": vendor, "model": model, "price": price}
    return(){
        new_item
    }
    
