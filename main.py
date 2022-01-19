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
    print("\t1 - Stock")                        #   Sales Module
    if Active_user['usertype'] == 'admin':
        print("\t2 - Sales")                    #   Inventory Module

    #   ch: string variable which contains '1' if user wishes to sign in, '2' if user wishes to sign up.
    ch = input('\n\t\t')
    myfuncs.clearscr()

    if ch == '1':
        pass

    elif ch == '2':

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
                    item, item_exists = myfuncs.findItem(itemid)
                    if not item_exists: 
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
                    
                    _, item_exists = myfuncs.findItem(newItem['itemid'])
                    if item_exists:
                        print('\nItem Id and Item name are candidate keys. Duplicate records are not accepted.')
                        input()
                        myfuncs.clearscr()
                        continue
                    
                    if newItem['itemid'] < 0 or newItem['Price'] < 0 or newItem['Quantity'] < 0:
                        print('\nEnter appropriate value.')
                        input()
                        myfuncs.clearscr()
                        continue

                    myfuncs.writeItem(newItem)
                    myfuncs.clearscr()
                    break

            elif action == '3':
                while 1:
                    itemid = input('Enter Item ID or Item Name:\t')
                    item, item_exists = myfuncs.findItem(itemid)
                    if not item_exists: 
                        print("Item does not exist. Please try again.")
                        input()
                        myfuncs.clearscr()
                        continue
                    print("Enter Attribute to be changed:\t")

                    for i in range(myfuncs.inventoryAttributes): print(f'{i+1} - {myfuncs.inventoryAttributes[i]}')

                    

    else:
        print("Enter appropriate input\n")
    

    
    