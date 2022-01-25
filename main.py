import myFunctions as myfuncs
import csv
print('\n')
while 1:
    print("\t\t\tWelcome to Lloyds bakery.")
    print("\n\n")
    print("\t1 - Have an account already? Sign in")
    print("\t2 - Don't have an account? Sign up")
    #   ch: string variable which contains '1' if user wishes to sign in, '2' if user wishes to sign up.
    ch = input('\n\t\t')
    myfuncs.clearscr()

    
    myfuncs.initialize()

    #   Signin
    if ch == '1':
        Active_user = myfuncs.signin()
        break

    #   Signup
    elif ch == '2':        
        myfuncs.signup()
    
    else:
        print("Enter appropriate input\n")

while 1:
    print(f"\t\t\tWelcome to Lloyds bakery, {Active_user['username']}")
    print("\n\n")
    if Active_user['usertype'] == 'admin':
        print("\t1 - Stock")                        #   Sales Module
    
        print("\t2 - Sales")                    #   Inventory Module

        #   ch: string variable which contains '1' if user wishes to sign in, '2' if user wishes to sign up.
        ch = input('\n\t\t')
        myfuncs.clearscr()

    if ch == '1' and Active_user['usertype'] == 'admin':

        while 1:
            print(f"\t\t\tWelcome to Lloyds bakery, {Active_user['username']}")
            print("\n\n")
            print("\t1 - Search for item") 
            print("\t2 - Create new item")
            print("\t3 - Modify existing item")
            print("\t4 - Delete existing item")
            print("\t5 - Display Inventory")   

            action = input('\n\t\t')
            myfuncs.clearscr()

            if action == '1':
                while 1:
                    itemid = input('Enter Item ID or Item Name:\t')
                    item = myfuncs.findItem(itemid)
                    if item is None: 
                        print("Item does not exist. Please try again.")
                        input()
                        myfuncs.clearscr()
                        continue
                    # would be nice if this was a little more organised with table borders and all
                    for attribute in item:
                        print(f'{attribute} : {item[attribute]}')
                    print("Want to search for more records? y/n")
                    if input() in 'Nn': break


            elif action == '2':
                while 1:
                    newItem = dict()
                    for attribute in myfuncs.inventoryAttributes:
                        newItem[attribute] = input(f'Enter {attribute}: \t')
                    
                    item = myfuncs.findItem(newItem['Item Id'])
                    if item is not None:
                        print('\nItem Id and Item name are candidate keys. Duplicate records are not accepted.')
                        input()
                        myfuncs.clearscr()
                        continue
                    
                    if int(newItem['Item Id']) < 0 or int(newItem['Price']) < 0 or int(newItem['Quantity']) < 0:
                        print('\nEnter appropriate value.')
                        input()
                        myfuncs.clearscr()
                        continue

                    myfuncs.writeItem(newItem)
                    myfuncs.clearscr()
                    print("Want to add more records? y/n")
                    myfuncs.clearscr()
                    if input() in 'Nn': break

            elif action == '3':
                while 1:
                    itemid = input('Enter Item ID or Item Name:\t')
                    item = myfuncs.findItem(itemid)
                    if item is None: 
                        print("Item does not exist. Please try again.")
                        input()
                        myfuncs.clearscr()
                        continue
                    print("Enter Attribute to be changed:\t")

                    for i in range(myfuncs.inventoryAttributes): print(f'{i+1} - {myfuncs.inventoryAttributes[i]}')

                    attribute_index = input('\t\t') - 1

                    new_value = input("Enter modified value:\t")

                    myfuncs.modifyItem(item, myfuncs.inventoryAttributes[attribute_index], new_value)
                    print("Want to search for more records? y/n")
                    if input() in 'Nn': break

            elif action == '4':
                while 1:
                    itemid = input('Enter Item ID or Item Name:\t')
                    item = myfuncs.findItem(itemid)
                    if item is not None: 
                        print("Item does not exist. Please try again.")
                        input()
                        myfuncs.clearscr()
                        continue
                    print('Are you sure you want to delete this item? y/n')
                    for attribute in item:
                        print(f'{attribute} : {item[attribute]}')
                    if input() not in 'Yy': continue
                    
                    
                    myfuncs.deleteItem(item)
                    print("Want to search for more records? y/n")
                    if input() in 'Nn': break

            else:
                with open('inventory.csv', 'r') as inventoryFileObj:
                    Inventory = csv.DictReader(inventoryFileObj, fieldnames=myfuncs.inventoryAttributes)
                    for item in Inventory:
                        print(*item.items())

    elif Active_user['usertype'] == 'regular' or ch == 2:
        pass

    else:
        myfuncs.clearscr()
        print("Enter appropriate input\n")
        continue