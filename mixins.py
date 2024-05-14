import pickle
from main import main_list

class   :
    def save_file(self, data):
        with open(self.file_name, 'wb') as f:
            pickle.dump(data, f)
            print(f"data saved to file {self.file_name}")
            
    def load_file(self):
        try:
            with open(self.file_name, 'rb') as f:
                data = pickle.load(f)
                print(f"data loaded from file {self.file_name}")
                return data
        except (FileNotFoundError, EOFError) as e:
            print(e.message)
        # except Exception as e:
        #     print(e.message)
        
# class FileHandlerMixin:
#     def save_file(self, data):
#         with open(self.file_name + self.extention, 'wb') as f:
#             pickle.dump(data, f)
#             print(f"data saved to file {self.file_name}")
            
#     def load_file(self, file_name):
#         try:
#             with open(file_name, 'rb') as f:
#                 data = pickle.load(f)
#                 print(f"data loaded from file {self.file_name}")
#                 return data
#         except (FileNotFoundError, EOFError) as e:
#             print(e.message)