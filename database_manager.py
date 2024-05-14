import psycopg2

class DatabaseManager:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = psycopg2.connect(**self.db_config)
        # self.connection.auto_commit = True
        self.cursor = None
        print('connecting is started')
    
    def __enter__(self):
        print('cursor is starting ...')
        self.cursor = self.connection.cursor()
        return self
        
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        # exc  exceptiom 
        if exc_type or exc_value or exc_traceback:
            print(exc_value)
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        
    def close_connection(self):
        self.connection.close()
        
    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)

    def fetch_one(self):
        return self.cursor.fetchone()
    
    def fetch_all(self):
        return self.cursor.fetchall()
    
    def save_user(self, username, password):
        query =  """
                insert into users (username, password) values (%s, %s)
                """
        params = (username, password)
        self.execute_query(query, params)
        
    def save_contact(self, name, email):
        query =  """
                insert into contact (username, password) values (%s, %s)
                """
        params = (username, password)
        self.execute_query(query, params)
            


