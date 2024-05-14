from database_manager import DatabaseManager
import hashlib


db_config = {
    'dbname': 'm_110',
    'user' : 'maktab_user',
    'password' : '123',
    'host' : 'localhost'
}

db_manager_obj = DatabaseManager(db_config)
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
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with db_manager_obj as db_manager:
        query = "select * from users where username=%s"
        params = (username,)
        db_manager.execute_query(query, params)
        # result = db_manager.cursor.fetchone()
        result = db_manager.fetch_one() # cursor.fetchone()
        if not result :        
            query =  "insert into users (username, password) values (%s, %s)"
            params = (username, hashed_password)
            db_manager.execute_query(query, params)
            print('user registered successfully')
        else:
            print(f'this username : {username} exists')
        # these lines are the same (up, down)
        # db_manager.cursor.execute(query, params)
        
        #  cursor closed
    
    
    
# login 
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    with db_manager_obj as db_manager:
        query = """
            select * from users
            where username = %s and password = %s
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        params = (username, hashed_password)
        db_manager.execute_query(query, params)
        user_obj = db_manager.fetch_one()
        if user_obj:
            print(f"your logged in as {username}")
        else :
            print("username or password is incorrect")
    

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