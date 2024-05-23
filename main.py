from database_manager import DatabaseManager
from model_manager import ModelManager
from user_manager import UserManager
from contact_manager import ContactManager
from models import User,Contact

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
Contact.manager = ContactManager(db_manager_obj)
# show all users
# User.manager.all()
# for user in users_obj:
#     user[0], user[1]

# user_model_manager_obj.get(id)
# user_model_manager_obj.filter(column, values)

# show menu
def display_menu():
    print("\n===== Main Menu =====")
    print("1. Register new user")
    print("2. Login as user")
    print("3. Exit")
    return input("Enter your Choice: ")

def  display_contact_menu() -> int:
    print("\n===== Contact Menu =====")
    print("1. add contact")
    print("2. edit contact")
    print("3. delete contact")
    print("4. back to main menu")
    return input('Enter your choice:')

def add_contact(logged_user_obj):
    while True:
        name =  input("Enter your name")
        if name:
            break
         
    email = input("Enter your email")
    while not email:
        email = input("Enter your email again")

    # ContactManager.add_contact(logged_user_obj.user_id, name, email)
    Contact.manager.add_contact(logged_user_obj.user_id, name, email)

def edit_contact(logged_user_obj):
    pass

def delete_contact(logged_user_obj):
    pass

# logged menu
def contact_main(logged_user_obj):
    while True:
        n = display_contact_menu()
        if n == '1':
            add_contact(logged_user_obj)
        elif n == '2':
            edit_contact(logged_user_obj)
        elif n == '3':
            delete_contact(logged_user_obj)
        elif n == '4':
            print("backing to main menu...")
            break
        else:
            print("invalid input")



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
    logged_user_obj = User.manager.login_user(username, password)
    if not logged_user_obj:
        print("login failed --------------------------------")
        return
    print("login successful --------------------------------")
    contact_main(logged_user_obj)

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