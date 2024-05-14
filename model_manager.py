from database_manager import DatabaseManager
from models import User

class ModelManager:
    def __init__(self, db_manager_obj, table_name, model_class):
        self.db_manager = db_manager_obj
        self.table_name = table_name
        self.model_class = model_class
        
    # all, get one, filter , save, update, delete
    def all(self):
        with self.db_manager as db:
            q = f"select * from {self.table_name}"
            db.execute_query(q)
            rows = db.fetch_all()
            
        # all_obj = []
        # for row in rows:
        #     inst_obj = self.model_class(*row)
        #     all_obj.append(inst_obj)
            
        return [self.model_class(*row) for row in rows]
    
    # all : select * from table;
    # get one by id : select * from table table_id = id ; filter by id
    # filter : select * from table where columns  = values
    
    
    
    
    # save : insert into table columns = values
    # update : updaet table set columns = 
    # delete by id : delete from table where table_id = id; 
    
    
        