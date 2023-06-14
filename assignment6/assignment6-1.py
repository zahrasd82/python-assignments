from prettytable import PrettyTable


def read_from_database():
    file = open("database.txt")
    for product in file:
        product = product.split(",")
        product = {"Id":int(product[0]) , "Name":product[1] , "Price":int(product[2]) , "Count":int(product[3])}
        products.append(product)

def write_to_database():
    file = open("database.txt","w")
    for product in products:
        str = "{0},{1},{2},{3}".format(product["Id"],product["Name"],product["Price"],product["Count"])
        file.write(str + "\n")
    file.close()

def show_menu():
    print("1 - add")
    print("2 - edit")
    print("3 - delete")
    print("4 - buy")
    print("5 - show list")
    print("6 - search")
    print("7 - exit")

def add():
    user_input = input("enter id , name , price and count of the product : ").split(",")
    product = {"Id":int(user_input[0]) , "Name":user_input[1] , "Price":int(user_input[2]) , "Count":int(user_input[3])}
    products.append(product)
    print("new product added successfully!\n")

def edit():
    user_input_id = int(input("enter the product id to edit : "))
    index = get_index(user_input_id)
    if index[0]:
        product = products[index[1]]
        print("\n1 - Name \n2 - Price \n3 - Count\n")
        user_input_option = int(input("select a option : "))
        user_input_value = input("enter the new value : ")
        if user_input_option == 1:
            product["Name"] = user_input_value
        elif user_input_option == 2:
            product["Price"] = user_input_value
        elif user_input_option == 3:
            product["Count"] = user_input_value
        print("product edited successfully!\n")  

def delete():
    user_input_id = int(input("enter the product id to edit : "))
    index = get_index(user_input_id)
    if index[0]:
        del products[index[1]]
        print("the product was successfully deleted!\n")
    
def buy():
    while True:
        show_list()
        user_input_id = int(input("enter the product id to buy : "))
        index = get_index(user_input_id)
        if index[0]:
            user_input_count = int(input("how many do you want : "))
            if products[index[1]]["Count"] >= user_input_count:
                products[index[1]]["Count"] -= user_input_count
                for product in cart:
                    if product["Id"] == products[index[1]]["Id"]:
                        product["Count"] += user_input_count
                        break
                else:
                    add_to_cart = {"Id":products[index[1]]["Id"] , "Name":products[index[1]]["Name"] , "Price":products[index[1]]["Price"] , "Count":user_input_count}
                    cart.append(add_to_cart)
                    print("successfully added to cart!\n")
            else:
                print("the product number is not enough!\n")
        user_input = input("do you want to continue shopping (y/n) ?")
        if user_input != "y":
            myTable = PrettyTable(["Name", "Price", "Count"])
            total_price = 0
            print("\nfinal invoice :")
            for product in cart:
                myTable.add_row([product["Name"],product["Price"],product["Count"]])
                total_price += product["Price"] * product["Count"]
            print(myTable,"\ntotal price : ",total_price,"\n")
            break

def show_list():
    myTable = PrettyTable(["Id", "Name", "Price", "Count"])
    for product in products:
        myTable.add_row([product["Id"],product["Name"],product["Price"],product["Count"]])
    print(myTable,"\n")

def search():
    user_keyword = input("enter a keyword to search : ")
    for product in products:
        if str(product["Id"]) == user_keyword or product["Name"] == user_keyword:
            print("\nID : ",product["Id"],"\nName : ",product["Name"],"\nPrice : ",product["Price"],"\nCount : ",product["Count"],"\n")
            break
    else:
        print("there is no product with this Keyword!\n")

def get_index(id):
    for i in range(len(products)):
        if products[i]["Id"] == id:
            res = [True , i]
            return res
    print("there is no product with this ID!")
    res = [False , 0]
    return res

products = []
cart = []
read_from_database()

while True:
    show_menu()
    user_select = int(input("select a option : "))
    if user_select == 1:
        add()
    elif user_select == 2:
        edit()
    elif user_select == 3:
        delete()
    elif user_select == 4:
        buy()
    elif user_select == 5:
        show_list()
    elif user_select == 6:
        search()
    elif user_select == 7:
        write_to_database()
        exit()