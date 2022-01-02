import myFunctions as myfuncs
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
    print("\t1 - Sales")                        #   Sales Module
    if Active_user['usertype'] == 'admin':
        print("\t2 - Stock")                    #   Inventory Module

    #   ch: string variable which contains '1' if user wishes to sign in, '2' if user wishes to sign up.
    ch = input('\n\t\t')
    myfuncs.clearscr()

    if ch == '1':
        pass

    elif ch == '2':
        myfuncs.inventory()

    else:
        print("Enter appropriate input\n")
    

    
    