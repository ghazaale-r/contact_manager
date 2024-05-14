from abc import ABC, abstractmethod
import hashlib

class AbstractUser(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password # plain text 
        # self._password = self.hash_password(password) # hashed
        # self._password = None
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, entered_password):
        return self._password == hashlib.sha256(entered_password.encode()).hexdigest()
    
    @property
    def password(self):
        # getter _password
        return self._password
    
    @password.setter
    def password(self, new_password):
        # setter _password
        self._password = self.hash_password(new_password)
    
from database_manager import DatabaseManager

class User(AbstractUser):
    def __init__(self, username, password, user_id=None):
        super().__init__(username, password)
        user_id = user_id
  
    def __str__(self):
        return f"{self.username}_{self.len_contacts()}"
        
    def save(self):
        if self.user_id: # update
            query = "update users set password=%s where user_id=%s"
            params = (self.password, self.user_id)
        else: # create save
            query =  """
                    insert into users (username, password) values (%s, %s)
                    """
            params = (self.username, self.password)
            
        with db_manager_obj as db:
            db.execute_query(query, params)
            # get id , self.user_id = id
            # 1 , query , returning lastid
            # 2 , q, select lastval 
            # 3 , q get by usename , id
            
            
    
    def delete(self):
        if self.user_id:
            with db_manager_obj as db:
                query = "delete from users where user_id = %s"
                params = (self.user_id,)
                db.execute_query(query, params)
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class Address:
    def __init__(self, contact_id, city, state, street, zip_code, addr_id=None):
        self.contact_id = contact_id
        self.addr_id = addr_id

        self.city = city
        self.state = state
        self.street = street
        self.zip_code = zip_code
        
    def display(self):
        print(f"{self.city}, {self.state}, {self.street}, {self.zip_code}")
    
    def __str__(self):
        return f"{self.city}, {self.state}, {self.street}, {self.zip_code}"
    
class Phone:
    def __init__(self, contact_id, phone_num, label=None, phone_id=None):
        self.phone_id = phone_id
        self.contact_id = contact_id
        
        self.phone_num = phone_num
        
        self.phone_label_counter = 0
        self.default_label = ['home', 'work', 'mobile']
        if label:
            self.label = label
        else:
            self.set_label(label)
        
    def set_label(self, label=None):
        if self.default_label:
            self.label = self.default_label.pop()
        else:
            self.phone_label_counter += 1
            self.label = f"phone_{self.phone_label_counter}"

        
    # def delete_phone(self, label):
    #     del self.phone[label]
   
class Contact:
    def __init__(self, user_id, name, email=None, contact_id=None):
        self.user_id = user_id
        self.contact_id = contact_id
        
        self.name = name
        self.email = email
