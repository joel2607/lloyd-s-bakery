from myFunctions import *
print('\n')
while 1:
    print("\t\t\tWelcome to Lloyds bakery.")
    print("\n\n")
    print("\t1 - Have an account already? Sign in")
    print("\t2 - Don't have an account? Sign up")
    #   ch: string variable which contains '1' if user wishes to sign in, '2' if user wishes to sign up.
    ch = input('\n\t\t')
    clearscr()

    #   Checking if userinfo.dat exists, and if it doesn't, initializing it with starting values.
    initialize()

    #   Signin
    if ch == '1':
        signin()
        break

    #   Signup
    elif ch == '2':        
        signup()
    
    else:
        print("Enter appropriate input\n")