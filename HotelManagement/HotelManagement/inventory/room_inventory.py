from enum import Enum
from typing import List,Dict
from classes.user import User
from classes.room import Room

class Availability(Enum):
    available = "available"
    unavailable = "unavailable"

class Room_inventory:
    room_mapper_with_availability = {}
    room_mapper_with_type = {}
    room_to_user_mapping = {}

    def add_room(self,room):
        if len(self.room_mapper_with_availability)==0:
            self.room_mapper_with_availability.update({"available":[]})
            self.room_mapper_with_availability.update({"unavailable":[]})
        if room not in self.room_mapper_with_availability["available"]:
            self.room_mapper_with_availability["available"].append(room)
        
        if room.type not in self.room_mapper_with_type:
            self.room_mapper_with_type.update({room.type:[room]})
        else:
            self.room_mapper_with_type[room.type].append(room)
        
    def change_room_availablity(self,room):
        if room.available:
            room.available = False
            self.room_mapper_with_availability[Availability.available].remove(room)
            self.room_mapper_with_availability[Availability.unavailable].add(room)
        else:
            room.available = True
            self.room_mapper_with_availability[Availability.unavailable].remove(room)
            self.room_mapper_with_availability[Availability.available].add(room)
    
    def show_available_rooms(self,type_of_room):
        rooms_of_type = self.room_mapper_with_type[type_of_room]
        print(rooms_of_type,self.room_mapper_with_availability["available"])
        rooms_available = []
        for room in rooms_of_type:
            if room in self.room_mapper_with_availability["available"]:
                rooms_available.append(room)
        return rooms_available        
   
    def add_booking(self,room:Room, user:User):
        self.room_to_user_mapping[room] = user
    
    def displayroomusers(self,room_id):
        room = None
        for id, rooms in self.room_mapper_with_availability.items():
            for room_ in rooms:
                if room_.id == room_id:
                    room = room_
        return self.room_to_user_mapping[room]