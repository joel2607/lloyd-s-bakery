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
        print("\t1 - Stock")  #   Sales Module

        print("\t2 - Sales")  #   Inventory Module

        #   ch: string variable which contains '1' if user wishes to sign in, '2' if user wishes to sign up.
        ch = input('\n\t\t')
        myfuncs.clearscr()

    if Active_user['usertype'] == 'admin' and ch == '1':

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

                    item_found_by_id = myfuncs.findItem(newItem['Item Id'])
                    item_found_by_name = myfuncs.findItem(newItem['Item Name'])

                    if item_found_by_id is not None or item_found_by_name is not None:
                        print(
                            '\nItem Id and Item name are candidate keys. Duplicate records are not accepted.'
                        )
                        input()
                        myfuncs.clearscr()
                        continue

                    if int(newItem['Item Id']) < 0 or int(
                            newItem['Price']) < 0 or int(
                                newItem['Quantity']) < 0:
                        print('\nEnter appropriate value.')
                        input()
                        myfuncs.clearscr()
                        continue

                    myfuncs.writeItem(newItem)
                    myfuncs.clearscr()
                    print("Want to add more records? y/n")
                    if input() not in 'yY':
                        myfuncs.clearscr()
                        break

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

                    for i in range(len(myfuncs.inventoryAttributes)):
                        print(f'{i+1} - {myfuncs.inventoryAttributes[i]}')

                    try:
                        attribute_index = int(input('\t\t')) - 1
                    except TypeError:
                        print("Enter appropriate input")
                        myfuncs.clearscr()
                        continue
                        
                    if attribute_index not in range(
                            len(myfuncs.inventoryAttributes)):
                        print("Enter appropriate input")
                        myfuncs.clearscr()
                        continue

                    new_value = input("Enter modified value:\t")

                    myfuncs.modifyItem(
                        item, myfuncs.inventoryAttributes[attribute_index],
                        new_value)
                    print("Want to search for more records? y/n")
                    if input() in 'Nn':
                        myfuncs.clearscr()
                        break

            elif action == '4':
                while 1:
                    itemid = input('Enter Item ID or Item Name:\t')
                    item = myfuncs.findItem(itemid)
                    if item is None:
                        print("Item does not exist. Please try again.")
                        input()
                        myfuncs.clearscr()
                        continue
                    print('Are you sure you want to delete this item? y/n')
                    for attribute in item:
                        print(f'{attribute} : {item[attribute]}')
                    if input() not in 'Yy': continue

                    myfuncs.deleteItem(item)
                    print("Want to delete more records? y/n")
                    if input() in 'Nn':
                        myfuncs.clearscr()
                        break

                    myfuncs.clearscr()

            else:
                myfuncs.printInventory()

                input()
                myfuncs.clearscr()
                break

    elif Active_user['usertype'] == 'regular' or ch == "2":
        while 1:
            print(f"\t\t\tWelcome to Lloyds bakery, {Active_user['username']}")
            print("\n\n")
            print("\t1 - Display Inventory")
            print("\t2 - Buy Item")
            print("\t3 - Generate Sales Report")

            action = input('\n\t\t')
            myfuncs.clearscr()

            if action == '1':
                myfuncs.printInventory()

                input()
                myfuncs.clearscr()
                break

            elif action == "2":
                myfuncs.printInventory()
                while 1:
                    itemid = input('Enter Item ID or Item Name to be bought:\t')
                    item = myfuncs.findItem(itemid)
                    if item is None:
                        print("Item does not exist. Please try again.")
                        input()
                        
                        continue

                    quanity_purchased = int(input("Enter purchase quantity:\t"))

                    if quanity_purchased<=int(item['Quantity']):

                      myfuncs.modifyItem(item, 'Quantity', int(item['Quantity']) - quanity_purchased)
                      print("Want to buy additional items? y/n")

                      dict = {itemid, quanity_purchased}
                      myfuncs.writeItem_sales(dict)
                      
                        
                      if input() in 'Nn':
                        
                        
                            break
                    else:
                      print("Not enough stock is available for that item")
                      continue
            elif action =="3":
              myfuncs.printSales()

    else:
        myfuncs.clearscr()
        print("Enter appropriate input\n")
        continue
