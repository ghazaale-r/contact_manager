from database_manager import DatabaseManager
from models import User

class ModelManager:
    def __init__(self, db_manager_obj, table_name, model_class):
        self.db_manager = db_manager_obj
        self.table_name = table_name
        self.model_class = model_class
        
    # all, get one, filter , save, update, delete
    # all : select * from table;
    def all(self):
        with self.db_manager as db:
            q = f"select * from {self.table_name}"
            db.execute_query(q)
            rows = db.fetch_all()
        if rows:
            q = f"Select * FROM {self.table_name} LIMIT 0"
            # اتصال به دیتابیس
            with self.db_manager as db:
                # اجرای کویری
                db.execute_query(q)
                # گرفتن نام های ستون های جدول بصورت لیست
                colnames = [desc[0] for desc in db.cursor.description] # ('user_id', 'username', 'password')
                
        return [self.model_class(**dict(zip(colnames, row))) for row in rows]
        # return [self.model_class(*row) for row in rows]
    
    
    # get one by id : select * from table table_id = id ; filter by id
    # second approad get one by one condition like username not only id cloumn 
    def get(self, column, value):
        q = f"select * from {self.table_name} where {column} = %s"
        params = (value,)
        with self.db_manager as db:
            db.execute_query(q, params)
            row = db.fetch_one() # row = ('3', 'a', '123')
            
        # apprach No.1 
        # راه حل اول یک مشکلی دارد اینکه ترتیب مقادیر دریافت شده از دیتابیس
        # با اتریبیوت های کلاس ما یکسان نیست 
        # دیتابیس = ('user_id', 'username', 'password')
        # کلاس یوزر = username, password, user_id
        # return self.model_class(*row) 
        # User('3', 'a', '123') username = 3, password = a, user_id  =123 X WRONG
            
    
        # apprach No.2
        # ستون های دیتابیس را بگیریم و یک دیکشنری از نام ستون و مقدار ستون ایجاد کینم 
        # بعنوان مثال ما برای کلاس User در نظر میگیرم
        if row:
            # کویری گرفتن نام ستون های جدول
            q = f"Select * FROM {self.table_name} LIMIT 0"
            # اتصال به دیتابیس
            with self.db_manager as db:
                # اجرای کویری
                db.execute_query(q)
                # گرفتن نام های ستون های جدول بصورت لیست
                colnames = [desc[0] for desc in db.cursor.description] # ('user_id', 'username', 'password')
                
            return self.model_class(**dict(zip(colnames, row)))
         
            # متد zip چکونه کار میکند
            # v = (1,2,3)
            # c = ('A','B','C')
            # x = list(zip(c, v))
            # y = dict(zip(c, v))
            # ("A", 1), ...
            
            # column_names = ('user_id', 'username', 'password')
            # {
            #     'user_id' : '3',
            #     'username' : 'a',
            #     'password' : '123'
            # }
            # User(**{
            #     'user_id' : '3',
            #     'username' : 'a',
            #     'password' : '123'
            # })
            # User(user_id='3', username = 'a', password =  '123')
            # User()
            
            
            # User('a', '123', '3')
            
            # class User(AbstractUser):
            #     manager = None
                
                
                # def __init__(self, username, password, user_id=None):
                # def __init__(self, user_id=None, username, password):
            
        
        
        
        
    # filter : select * from table where columns  = values
    def filter(self, **kwargs):
        # key_value={'name':'ali'}
        # key_value={'email':'ali@yahoo.com', 'phone_number': '01912234'}
        
        base_query = f"Select * from {self.table_name} where "
        conditional_query = " and ".join([f"{key} = %s" for key in kwargs.keys()])
        query = base_query + conditional_query
        params = tuple(kwargs.values())
        with self.db_manager as db:
            db.execute_query(query, params)
            rows = db.fetch_all()
        
        if rows:
            q = f"Select * FROM {self.table_name} LIMIT 0"
            # اتصال به دیتابیس
            with self.db_manager as db:
                # اجرای کویری
                db.execute_query(q)
                # گرفتن نام های ستون های جدول بصورت لیست
                colnames = [desc[0] for desc in db.cursor.description] # ('user_id', 'username', 'password')
            
            # models_list = []
            # for row in rows :
            #     models_list.append(self.model_class(**dict(zip(colnames, row))))
                
        return [self.model_class(**dict(zip(colnames, row))) for row in rows]
        
        # query = f"select * from {self.table_name} where username = %s and password = %s"
        # x = ['username = %s', 'password = %s'] 
        # ' and '.join(x)
        
        # query = f"select * from {self.table_name} where name = %s "
        # x = ['name = %s'] 
        # ' and '.join(x)
        
        # query = f"select * from {self.table_name} where name = %s and email=%s"
        
        # query = f"select * from {self.table_name} where phone=%s"
        
        # use traditional approach
        
        # list_of_conditions = []
        # for key in kwargs.keys():
        #     condition_q = f"{key} = %s"
        #     list_of_conditions.append(condition_q)
        # " and ".join(list_of_conditions)
        
        # list comprehension
        
        # " and ".join([f"{key} = %s" for key in kwargs.keys()])
            
        # q = f"Select * from {self.table_name} where username = %s and password = %s"
        # q = f"Select * from {self.table_name} where name = %s and email = %s and phone_number = %s and address = %s"
        # q = f"Select * from {self.table_name} where name = %s and phone_number = %s"
        # params = (value)
        # with self.db_manager as db:
        #     db.execute_query(q, params)
        #     rows = db.fetch_all()
    
    
    
        