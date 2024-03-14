from classes.user import User
from classes.room import Room
from typing import Dict,List

class User_inventory:
    user_map = {}
    user_room_map = {}

    def add_user(self,user:User):
        if user.user_id not in self.user_map:
            self.user_room_map.update({user.user_id:user})
            print("user with user_id = {} is added".format(user.user_id))
    
    def add_booking(self,user_id,room):
        self.user_room_map[user_id].append(room)
    
    def remove_booking(self,user_id,room):
        self.user_room_map[user_id].remove(room)



