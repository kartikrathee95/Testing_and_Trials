from typing import Dict,List

class User:
    user_id: str
    user_name:str
    email:str
    phone_no: str
    def __init__(self,id,name,email,phone_no):
        self.user_id = id
        self.user_name = name
        self.email = email
        self.phone_no = phone_no
        
    def get_id(self):
        return self.user_id
    
    