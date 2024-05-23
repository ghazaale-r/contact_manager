from model_manager import ModelManager
from models import Contact

class ContactManager(ModelManager):
    def __init__(self, db_manager_obj):
        super().__init__(db_manager_obj,"Contacts",Contact)
    
    def display_contact_list(self, logged_in_user_id):
        """
            display all contacts of specific user(logged in user)
        """
        # query='select * from contacts where user_id = %s'
        # params =(logged_in_user_id,)
        
        ## ap.1
        # params={'user_id':logged_in_user_id}
        # self.filter(**params)
        
        ## ap.2
        ## res is list of contact object of logged in user
        res=self.filter(user_id=logged_in_user_id)
        ## TODO: implement sorting contact_ids
        for obj in res:
            # 1. ali :: ali@yahoo.com 
            print(f"{obj.contact_id}. {obj.name} :: {obj.email}")
        
        return int(input("Choose contact_id:"))

        ## ap.3
        # self.filter(**{'user_id':logged_in_user_id})



    def add_contact(self, user_id, entered_name, entered_email):
        """
            get contact attribute from cli 
            create new object from contact class
            call save method of contact object
        """        
        contact_obj = Contact(user_id, entered_name, entered_email)
        contact_obj.save() # insert into , create new contact
        # print('your contact created successfully')

    def edit_contact(self, user_id, entered_name=None, entered_email=None):
    # def edit_contact(self, user_id, entered_name, entered_email):
        """
            get contact_id from cli
            get contact attribute from cli 
            update contact object from contact class
            call save method of contact object            
        """
        contact_id = self.display_contact_list(user_id)
        contact_obj = self.get(contact_id=contact_id)

        ## ap.1 use default value none
        if entered_email:
            contact_obj.email=entered_email
        if entered_name:
            contact_obj.name=entered_name
        contact_obj.save() # update set , update existing contact
        

    def delete_contact(self):
        """
            get contact_id from cli
            call delete method of contact object            
        """
        contact_id = self.display_contact_list()
        contact_obj = self.get(contact_id=contact_id)
        contact_obj.delete()

        

    # def add_contact(self, user_obj:object ,name:str, email:str) -> None:
    #     res = self.get('name', name)
    #     if res:
    #         raise ValueError("This contact already exists")
    #     contact=Contact(user_obj.user_id, name, email)
    #     contact.save()        
