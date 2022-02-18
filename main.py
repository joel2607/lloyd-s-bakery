import myFunctions as myfuncs
import datetime


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

        print("\t3 - Back")

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
            print("\t6 - Back")

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
                    if input() in 'Nn': 
                        myfuncs.clearscr()
                        break
                    myfuncs.clearscr()

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
                    myfuncs.clearscr()

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
                    myfuncs.clearscr()

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
            
            elif action == '5':
                myfuncs.printInventory()
                input()
                myfuncs.clearscr()
                break

            elif action == '6':
                myfuncs.clearscr()
                break

            else:
                print('Enter appropriate output')
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
            print('\t4 - Back')

            action = input('\n\t\t')
            myfuncs.clearscr()

            if action == '1':
                myfuncs.printInventory()

                input()
                myfuncs.clearscr()
                break

            elif action == "2":
                
                while 1:
                    myfuncs.printInventory()
                    itemid = input('Enter Item ID or Item Name to be bought:\t')
                    item = myfuncs.findItem(itemid)
                    if item is None:
                        print("Item does not exist. Please try again.")
                        input()
                        myfuncs.clearscr()
                        continue

                    try: quantity_purchased = int(input("Enter purchase quantity:\t"))
                    except ValueError: 
                        print('Enter appropriate value.')
                        input()
                        myfuncs.clearscr()
                        continue

                    if quantity_purchased<=int(item['Quantity']):
                        myfuncs.modifyItem(item, 'Quantity', int(item['Quantity']) - quantity_purchased)
                        
                        item_name = item["Item Name"]
                        item_id = item["Item Id"]
                        item_price = item["Price"]
                        current_timestamp = datetime.datetime.now()
                        current_timestamp_modded = current_timestamp.replace(microsecond = 0)
                        
                        sales_update = {
                            "Item ID":item_id, 
                            "Item Name":item_name, 
                            "Quantity":quantity_purchased,
                            "Price":item_price, 
                            'Amount': float(item_price)*quantity_purchased,
                            "Timestamp":str(current_timestamp_modded)
                            }
                        myfuncs.writeTransaction(sales_update)

                      
                        ch = input('Would you like to continue your shopping? y/n') 
                        if ch in 'Nn':
                            myfuncs.clearscr()
                            break
                        myfuncs.clearscr()
                    else:
                        print("Not enough stock is available for that item")
                        input()
                        myfuncs.clearscr()
                        continue
                      
            elif action =="3":
                myfuncs.showSales()
                print(f'Total sales: {myfuncs.totalFinder()}')
                input()
                myfuncs.clearscr()
                
            elif action == '4':
                myfuncs.clearscr()
                break
    
    elif ch == '3':
        myfuncs.clearscr()
        break

    else:
        myfuncs.clearscr()
        print("Enter appropriate input\n")
        continue
