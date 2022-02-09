import os, pickle, csv

inventoryAttributes = ['Item Id', 'Item Name', 'Price', 'Quantity']

def clearscr():  

    """Function used to clear screen. Takes no arguments. Returns None."""

    if os.name == 'nt':         #   'nt' is os name for windows systems
        _ = os.system('cls') 
  
    else:                       #   other systems will use this
        _ = os.system('clear')

def initialize():
    """
      Checking if userinfo.dat exists, and if it doesn't, initializing it with starting values. Returns None.
    """
    if not os.path.exists("userinfo.dat"):
        with open("userinfo.dat","wb") as User_data_file_obj:
            Users = [
                {'username': 'testuser', 'password': 'testpassword', 'usertype':'admin'}
            ]
            pickle.dump(Users,User_data_file_obj)

    if not os.path.exists("inventory.csv"):
        with open("inventory.csv","w") as inventoryFileObj:
            inventory = csv.DictWriter(inventoryFileObj, fieldnames=inventoryAttributes)
            inventory.writeheader()

"""
Users: 
    A list of dictionaries. Each dictionary contained in list is an individual user with 3 fields: username, password and usertype.
    Stored in a binary file called "userinfo.dat" using pickle serialization.

User_data_file_obj: 
    File object that stores "userinfo.dat"
"""

def signup():
    """
    Returns None. Displays signup screen and appends data to userinfo.dat
    """
    with open("userinfo.dat","rb") as User_data_file_obj:
        Users = pickle.load(User_data_file_obj)
        

    def username_already_exists(username,users=Users):

        """
        Function which returns True if username already exists. False if not.
        Defined in line 41.
        Parameters: 
            username: Mandatory paramater. The username to check. Type: str
            users: Optional. Type: List of dictionaries. default: Users
        """

        for user in users:
            if user['username'] == username:
                return True
        return False
    print()
    
    while 1:
        print('\t\t\tSign Up\n\n')
        New_user = dict()
        New_user['username'] = input('Username:\t')

        if username_already_exists(New_user['username']):
            clearscr()
            print("Username already exists.\n")
            continue
            #   Restarts loop and asks for username again

        New_user['password'] = input('Password:\t')
        confirm_password = input('Confirm Password:\t')

        if New_user['password'] != confirm_password:
            clearscr()
            print("Passwords dont match.\n")
            continue
            #   Restarts loop and asks for username again
        
        print("\t1 - Admin User")
        print("\t2 - Regular User")
        #   user_type_ch: string variable which contains '1' for admin user, '2' for normal user.
        user_type_ch = input('\n\t\t')

        if user_type_ch == '1':
            New_user['usertype'] = 'admin'
        elif user_type_ch == '2':
            New_user['usertype'] = 'regular'
        else:
            if user_type_ch == '':              #   Exit signup screen if empty input
                New_user = dict()
                clearscr()
                break

            clearscr()
            print("Enter valid input.\n")
            continue
            #   Restarts loop and asks for username again
        
        Users.append(New_user)

        with open("userinfo.dat","wb") as User_data_file_obj:
            pickle.dump(Users,User_data_file_obj)
        #   Users rewritten into userinfo.dat file.
        #   New user gets appended to the Users list.
        clearscr()
        print("Sucessfully created account. Press enter to continue")
        
        input()
        clearscr()
        break

def signin():
    """
    Asks user for username and password. Logs in if username and password are correct. Returns dictionary of user 
    """
    with open("userinfo.dat","rb") as User_data_file_obj:
        Users = pickle.load(User_data_file_obj)
        

    def findUser(username,users=Users):
        for user in users:
            if user['username'] == username:
                return user

    while 1:
        print("\t\t\tSign In\n\n")
        username = input('Username:\t')
        if username == '':              #   Exit login screen if empty input
            clearscr()
            break
        User = findUser(username)

        if (User is None):              #   User does not exist, findUser() returns None
            clearscr()
            print("Username does not exist\n")
            continue
            #   Restarts loop and asks for username again

        password = input('Password:\t')
        
        if password == '':              #   Exit login screen if empty input
            clearscr()
            break

        if password != User['password']:    #   Password incorrect
            clearscr()
            print("Incorrect password.\n")
            continue
            #   Restarts loop and asks for username again
        
        clearscr()
        print("Sucessfully logged in. Press enter to continue")
        
        input()
        clearscr()
        return User

def findItem(userid):
    with open('inventory.csv', 'r') as inventoryFileObj:
        Inventory = csv.DictReader(inventoryFileObj, fieldnames=inventoryAttributes)
        for item in Inventory:
            if item['Item Id'] == userid or item['Item Name'] == userid:
                return item
        else:
            return None

def writeItem(Item, mode = 'a'):
    with open('inventory.csv', mode) as inventoryFileObj:
        Inventory = csv.DictWriter(inventoryFileObj, fieldnames=inventoryAttributes)
        Inventory.writerow(Item)   
    
def deleteItem(del_item):
    with open('inventory.csv', 'r') as inventoryFileObj:
        Inventory = csv.DictReader(inventoryFileObj, fieldnames=inventoryAttributes)
        Inventory_contents = []
        for item in Inventory: Inventory_contents.append(item)

    with open("inventory.csv","w") as inventoryFileObj:
        inventory = csv.DictWriter(inventoryFileObj, fieldnames=inventoryAttributes)    #   clears contents of file and writes header
    

    for index in range(len(Inventory_contents)):
        item = Inventory_contents[index]
        if del_item['Item Id'] == item['Item Id']:
            continue
        writeItem(item)

def modifyItem(item, attribute, value):
    deleteItem(item)
    item[attribute] = value
    writeItem(item)

def printInventory():
    with open('inventory.csv', 'r') as inventoryFileObj:
        Inventory = csv.DictReader(
            inventoryFileObj,
            fieldnames=inventoryAttributes)
        print('\n' + (21*len(inventoryAttributes)+1) * '-')
        for item in Inventory:
            print('|', end='')
            for attribute in item:
                print(item[attribute],
                        end=((20 - len(item[attribute])) * ' ' +
                            '|'))
            print('\n' + (21*len(inventoryAttributes)+1) * '-')


#SALES FROM NOW ONWARDS
def printSales():
  with open('sales.csv', 'r') as inventoryFileObj:
        Inventory = csv.DictReader(
            inventoryFileObj,
            fieldnames=inventoryAttributes)
        print('\n' + (21*len(inventoryAttributes)+1) * '-')
        for item in Inventory:
            print('|', end='')
            for attribute in item:
                print(item[attribute],
                        end=((20 - len(item[attribute])) * ' ' +
                            '|'))
            print('\n' + (21*len(inventoryAttributes)+1) * '-')

def writeItem_sales(Item, mode = 'a'):
    with open('sales.csv', mode) as inventoryFileObj:
        Inventory = csv.DictWriter(inventoryFileObj, fieldnames=inventoryAttributes)
        Inventory.writerow(Item)

def deleteItem_sales(del_item):
    with open('sales.csv', 'r') as inventoryFileObj:
        Inventory = csv.DictReader(inventoryFileObj, fieldnames=inventoryAttributes)
        Inventory_contents = []
        for item in Inventory: Inventory_contents.append(item)

    with open("inventory.csv","w") as inventoryFileObj:
        inventory = csv.DictWriter(inventoryFileObj, fieldnames=inventoryAttributes)

def modifyItem_sales(item, attribute, value):
    deleteItem_sales(item)
    item[attribute] = value
    writeItem_sales(item)