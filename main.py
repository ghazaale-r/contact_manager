from database_manager import DatabaseManager
from model_manager import ModelManager
from models import User

import hashlib


db_config = {
    'dbname': 'm_110',
    'user' : 'maktab_user',
    'password' : '123',
    'host' : 'localhost'
}

db_manager_obj = DatabaseManager(db_config)
user_model_manager_obj = ModelManager(db_manager_obj, 'users', User)
users_obj = user_model_manager_obj.all()
for user in users_obj:
    user[0], user[1]

user_model_manager_obj.get(id)
user_model_manager_obj.filter(column, values)

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
    
    
# login 
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
   

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