from models import User
from managers import UserFileManager, UserFileManager2, UserFileManager3

def main_list():
    user_object = User('ali', '123')
    user_object_2 = User('zahra', '123')
    users = [
        User('parsa', '1123'), 
        User('seyed', '134'), 
        User('maryam', '1143'),
        user_object,
        user_object_2
    ]

    user_file_obj = UserFileManager('data')
    user_file_obj.save_user_list(users) 
    maryam_obj = user_file_obj.search_user('maryam') 
    print(maryam_obj.username)
    print(maryam_obj.password)
    
def main_dict():
    user_object = User('ali', '123')
    user_object_2 = User('zahra', '123')
    users = {
        'parsa' :User('parsa', '1123'), 
        'seyed': User('seyed', '134'), 
        'maryam' :User('maryam', '1143'),
        user_object.username : user_object,
        user_object_2.username : user_object_2
    }

    user_file_obj = UserFileManager2('data')
    user_file_obj.save_user_dict(users) 
    maryam_obj = user_file_obj.search_user('maryam') 
    print(maryam_obj.username)
    print(maryam_obj.password)

def main():
    user_object = User('ali', '123')
    user_object_2 = User('zahra', '123')
    
    user_file_obj = UserFileManager3('users')
    user_file_obj.save_user(user_object) 
    user_file_obj.save_user(user_object_2) 
    user_file_obj.save_user(User('parsa', '1123')) 
    user_file_obj.save_user(User('seyed', '134') ) 
    user_file_obj.save_user(User('maryam', '1143')) 
    user_file_obj.save_user(User('maryam', '22222')) 
    
    maryam_obj = user_file_obj.search_user('maryam') 
    print(maryam_obj.username)
    print(maryam_obj.password)
    


if __name__ == '__main__':
    main_list()
    print('################################')
    main_dict()
    print('################################')
    main()