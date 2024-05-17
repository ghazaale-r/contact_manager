from database_manager import DatabaseManager
from model_manager import ModelManager
from user_manager import UserManager
from models import User

import hashlib

with open("p.txt", "r") as f:
    password = f.read()
    
db_config = {
    'dbname': 'm_110',
    'user' : 'postgres',
    'password' : password,
    'host' : 'localhost'
}

db_manager_obj = DatabaseManager(db_config)

# User.manager = ModelManager(db_manager_obj, 'users', User) # old approach
# Contact.manager = ModelManager(db_manager_obj, 'Contacts', Contact) # old approach
### we need login and regoster 
# User.manager = UserManager(db_manager_obj, 'users', User) # X Wrong
User.manager = UserManager(db_manager_obj) # Correct
# show all users
# User.manager.all()
# for user in users_obj:
#     user[0], user[1]

# user_model_manager_obj.get(id)
# user_model_manager_obj.filter(column, values)

# show menu
def display_menu():
    print("1. Register new user")
    print("2. Login as user")
    print("3. Exit")
    return input("Enter your Choice: ")


# register
def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    new_user = User.manager.register_user(username, password)
    if new_user:
        print(" registration successful --------------------------------")
    
    
    
# login 
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    logged_user = User.manager.login_user(username, password)
    if not logged_user:
        print("login failed --------------------------------")
        return
    current_user_id  = logged_user.user_id
    print("login successful --------------------------------")
   

def main():
    while True:
        n = display_menu()
        if n == '1':
            register_user()
        elif n == '2':
            login()
        elif n == '3':
            print("Exiting...")
            break
        else:
            print("invalid input")
    db_manager_obj.close_connection()
    

if __name__ == '__main__':
    main()