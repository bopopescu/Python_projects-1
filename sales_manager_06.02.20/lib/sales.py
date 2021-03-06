from operator import itemgetter
if __name__ == "main":
    start()


def start(items):
    """ Sales Manager """
    print(type(items)) 
    # # так теж можна:  
    # if isinstance(items, tuple):
    #     raise Exception("Type of items must be a list, not a tuple!")
    if type(items) is not list:
        raise Exception("Type of items must be a list!")
    db_items = items
    sold_list_global = []
    exit = False
    while not exit:
        print("============Sales Manager v 1.0==========")
        choice = int(input(
            "1. Show Items \n2. Add Item  \n3. Delete Item \n4. Sort Items by price \n5. Sell Item \n6. Show sold Items \n0. Exit\n"))
        print("your choice is => ", choice)
        if choice == 1:
            show_items(db_items)
        elif choice == 2:
            new_item = add_item()
            db_items.insert(0, new_item)
            list_added = []
            list_added.extend(db_items)
            print("new list => \n", list_added)
        elif choice == 3:
            print("Whole list: => \n", db_items)
            it_to_del = dell_item(db_items)
            if it_to_del not in db_items:
                raise Exception("This item to delete is not in list")
            db_items.remove(it_to_del)
            list_after_del = []
            list_after_del.extend(db_items)
            print("new list => \n", list_after_del)
            
        elif choice == 4:
            sorted_list = sort_by_price(db_items)
            print("list, sorted by price => \n", sorted_list)
        elif choice == 5:
            result_it_soldList = sell_items(db_items)
            if result_it_soldList[0] not in db_items:
                raise Exception("This item to sell is not in list")
            db_items.remove(result_it_soldList[0])
            list_after_sell = []
            list_after_sell.extend(db_items)
            sold_list_global.extend(result_it_soldList[1])
            print("new list => \n", list_after_sell)
        elif choice == 6:
            if len(sold_list_global) == 0:
                raise Exception("There is no sold items yet! ")
            print("Sold list: \n", sold_list_global)
        elif choice == 0:
            exit = True
            print("By!")
        else:
            print("Please, enter a number from 1 to 6 or 0!")


def show_items(items):
    """ Show list of phones """
    print(items)


def add_item():
    
    """ Add a new phone """
    vendor = input("Enter vendor: ")
    model = input("Enter model: ")
    price = input("Enter price: ")
    id = input("Enter id: ")
    if vendor == "" or model == "" or price == "" or vendor == " " or model == " " or price == " ":
        raise Exception("Tomething is wrong with adding!")
    new_item = {"id": id, "vendor": vendor, "model": model, "price": price}
    return new_item
    

def dell_item(items):
    """ Delete a phone """
    id_to_del = input("Enter id of model to delete: ")
    for item in items:
        if item.get("id") == id_to_del:
            item_to_del = item
            return item_to_del


def sell_items(items):
    """ Sell a phone """
    id_to_sell = input("Enter id of model to sell: ")
    sold_list = []
    for item in items:
        if item.get("id") == id_to_sell:
            item_to_sell = item
            sold_list.append(item_to_sell)
            return item_to_sell, sold_list


def sort_by_price(items):
    """ Sorts a list of phones by price """
    sorted_list = sorted(items, key=itemgetter("price"))
    return sorted_list
