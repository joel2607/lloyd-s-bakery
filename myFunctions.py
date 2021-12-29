import os, pickle, csv

#   Function used to clear screen. Takes no arguments. Returns None.
def clearscr():  
    if os.name == 'nt':         #   'nt' is os name for windows systems
        _ = os.system('cls') 
  
    else:                       #   other systems will use this
        _ = os.system('clear')

def initialize():
    if not os.path.exists("userinfo.dat"):
        with open("userinfo.dat","wb") as User_data_file_obj:
            Users = [
                {'username': 'testuser', 'password': 'testpassword', 'usertype':'admin'}
            ]
            pickle.dump(Users,User_data_file_obj)

"""
Users: 
    A list of dictionaries. Each dictionary contained in list is an individual user with 3 fields: username, password and usertype.
    Stored in a binary file called "userinfo.dat" using pickle serialization.

User_data_file_obj: 
    File object that stores "userinfo.dat"

username_already_exists():
    Function which returns True if username already exists. False if not.
    Defined in line 41.
    Parameters: 
        username: Mandatory paramater. The username to check. Type: str
        users: Optional. Type: List of dictionaries. default: Users

"""

def signup():
    with open("userinfo.dat","rb") as User_data_file_obj:
        Users = pickle.load(User_data_file_obj)
        

    def username_already_exists(username,users=Users):
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