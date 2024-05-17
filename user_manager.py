from model_manager import ModelManager
from models import User

class UserManager(ModelManager):
    def __init__(self, db_manager_obj):
        super().__init__(db_manager_obj, 'Users', User)
        # ModelManager.db_manager = db_manager_obj
        # ModelManager.table_name = table_name
        # ModelManager.model_class = model_class
        
    def login_user(self, username, password):
        user_obj = self.get('username', username)
        if user_obj:
            if user_obj.check_password(password):
                return user_obj
        print("no username ")
        # raise ValueError("Invalid username or password")

    def register_user(self, username, password):
        # get user by username
        # q = "select * from users where username = %s"
        # with self.db_manager as db:
        #     db.cursor.execute(q, (username,))
        #     res = db.cursor.fetchone()
        #     if res :
        #         print(" user exists in database")
        #         return
            
        res = self.get('username', username)
        if res :
            raise ValueError(" Username already in database")
        # create new user
        # hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # new_user = User(username, hashed_password) 
        
        new_user = User(username, hashed_password) 
        new_user.password = password ### class setter method ( call hash method)
        # password : plain text --> _password
        # new_user = User(username) # password : plain text --> _password
        # new_user.password = password # call setter and hash password
        new_user.save()
        return new_user
