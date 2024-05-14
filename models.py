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
    
    
         

class User(AbstractUser):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.contacts = [] # Contact object , append

    def len_contacts(self):
        return len(self.contacts)
  
    def __str__(self):
        return f"{self.username}_{self.len_contacts()}"
        

        
class Address:
    def __init__(self, city, state, street, zip_code):
        self.city = city
        self.state = state
        self.street = street
        self.zip_code = zip_code
        
    def display(self):
        print(f"{self.city}, {self.state}, {self.street}, {self.zip_code}")
    
    def __str__(self):
        return f"{self.city}, {self.state}, {self.street}, {self.zip_code}"
    
class Contact:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email
        self.phone = {}
        self.address_list = [] # city, state, street, zip_code
       
        self.phone_label_counter = 0
        self.default_label = ['home', 'work', 'mobile']
        
    def add_phone(self, phone_number, label=None):
        if not label:
            # generate label
            if self.default_label:
                label = self.default_label.pop()
            else:
                self.phone_label_counter += 1
                label = f"phone_{self.phone_label_counter}"
        self.phone[label] = phone_number
        
    def delete_phone(self, label):
        del self.phone[label]
       
    # address methods
    def add_address(self, city, state, street, zip_code):
        addr_obj = Address(city, state, street, zip_code)
        # self.address_list.append(addr_obj)
        self.add_address_obj(addr_obj)
    
    def add_address_obj(self, addr_obj):
        self.address_list.append(addr_obj)
        
    def show_address(self):
        for idx, addr in enumerate(self.address_list):
            print(f"{idx + 1}. {addr}")
            
    def remove_address_by_index(self, index):
        if index in range(len(self.address_list)):
            # self.address_list.pop(index)
            del self.address_list[index]
            
    def remove_address(self):
        self.show_address()
        n = int(input("Enter address id to remove"))
        n -= 1
        self.remove_address_by_index(n)