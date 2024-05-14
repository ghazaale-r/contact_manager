# store , lood , search user by name
# list user_obje -> one file , 
#  dict user_obje -> one_file
# user has own file 

from mixins import FileHandlerMixin
import os 

class UserFileManager(FileHandlerMixin):
    def __init__(self, base_dir):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        self.file_name = os.path.join(self.base_dir, 'user_list.user')
            
    def save_user_list(self, user_list):
        self.save_file(user_list)
    
    def load_user_list(self):
        # users_list = self.load_file()
        # return users_list
        return self.load_file()
        
    def search_user(self, name):
        # O(n)
        users_list = self.load_user_list()
        for user in users_list:
            if user.username == name:
                return user
        return None

class UserFileManager2(FileHandlerMixin):
    def __init__(self, base_dir):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        self.file_name = os.path.join(self.base_dir, 'user_dict.user')
            
    def save_user_dict(self, user_dict):
        self.save_file(user_dict)
    
    def load_user_dict(self):
        # users_dict = self.load_file()
        # return users_dict
        return self.load_file()
        
    def search_user(self, name):
        users_dict = self.load_user_dict()
        # O(1)
        if name in users_dict:
            return users_dict[name]
        return None
    
class UserFileManager3(FileHandlerMixin):
    def __init__(self, base_dir):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        self.extention = '.user'
            
    def save_user(self, user_obj):
        self.file_name =  os.path.join(self.base_dir, user_obj.__str__() + self.extention) 
        self.save_file(user_obj)
    
    def load_user(self):
        return self.load_file()
        
    def search_user(self, name):
        self.file_name =  os.path.join(self.base_dir, name + self.extention) 
        if os.path.exists(self.file_name):
            user_obj = self.load_user()
            return user_obj
    
    
    
# class UserManager:
    # login , register
    
# class ContactManager:
#     def __init__(self, user_object):
#         self.user = user_object
#     add contact
#     edit contact
    



