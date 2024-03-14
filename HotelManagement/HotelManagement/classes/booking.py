from typing import Dict,List
from inventory.room_inventory import Room_inventory,Room
from inventory.user_inventory import User_inventory,User

class Booking:
    id: str
    success: bool
    room_type:str
    user:User
    room:Room
    
    def __init__(self,id,user_id,room_type):
        self.id = id
        self.user = User_inventory.user_room_map[user_id]
        self.room_type = room_type
    
    def InitiateBooking(self):
        room_inventory_obj = Room_inventory()
        rooms = room_inventory_obj.show_available_rooms(self.room_type)
        rooms_id_list = [item.id for item in rooms]
        print(rooms)
        choose_room = str(input("Choose the room from following rooms {} ".format(rooms_id_list)))
        for room in rooms:
            if room.id == choose_room:
                self.room = room
        self.room.book_room()
        print("Pay amount {}".format(self.room.get_room_price()))
        print("Payment done successfully")
        self.success = True
        room_inventory_obj.change_room_availablity(self.room)
        User_inventory().add_booking(self.user.user_id,self.room)
        room_inventory_obj.add_booking(self.room,self.user)



        


    
