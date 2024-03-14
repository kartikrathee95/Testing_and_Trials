from typing import Dict, List

class Room:
    id:str
    type:str
    available:bool
    price:int
    count_members:int

    def __init__(self,id,type):
        self.id = id
        self.type = type
        self.available = True
    
    def get_room_availablity(self):
        return self.available
    def get_room_price(self,price):
        pass
    def get_room_type(self,type):
        pass
    def get_members_count(self,count):
        pass
    def get_room(self,id):
        pass
    def book_room(self):
        self.available = False
        print("room no {} is booked successfully".format(self.id))

class Standard(Room):
    def __init__(self,id):
        super().__init__(id=id,type="standard")

    def get_room_price(self):
        return super().get_room_price(1000)
    def get_room_type(self):
        return super().get_room_type("standard")
    def get_members_count(self):
        return super().get_members_count(2)

class Deluxe(Room):
    def __init__(self,id):
        super().__init__(id=id,type="deluxe")

    def get_room_price(self):
        return super().get_room_price(5000)
    def get_room_type(self):
        return super().get_room_type("Deluxe")
    def get_members_count(self):
        return super().get_members_count(2)

class FamilySuite(Room):
    def __init__(self,id):
        super().__init__(id=id,type="familysuite")

    def get_room_price(self):
        return super().get_room_price()
    def get_room_type(self):
        return super().get_room_type("Family Suite")
    def get_members_count(self):
        return super().get_members_count(4)
