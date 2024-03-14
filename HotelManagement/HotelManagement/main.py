from classes import booking,room,user
from inventory import room_inventory, user_inventory


class main:
  print("Welcome to Hotel Booking portal")
  def run(self):
    while(True):
        input_args = str(input())
        input_args = input_args.split(' ')
        if input_args[0] == "createuser":
            if len(input_args)!=5:
                print("please input again, API error")
                continue
            else:
                user1 = user.User(input_args[1],
                                  input_args[2],
                                  input_args[3],
                                  input_args[4])
                user_inventory.User_inventory().add_user(user1)
        elif input_args[0] == "addroom":
            room1 = None
            if input_args[2] == "standard":
                room1 = room.Standard(input_args[1])
            elif input_args[2] == "deluxe":
                room1 = room.Deluxe(input_args[1])
            else:
                room1 = room.familysuite(input_args[1])
            room_inventory.Room_inventory().add_room(room1)
            
        elif input_args[0]== "bookroom":
            if len(input_args)!=4:
                print("API request error, please request again")
                continue
            else:
                booking1 = booking.Booking(input_args[1],
                                                  input_args[2],
                                                  input_args[3])
                
                booking1.InitiateBooking()
        elif input_args[0]== "displayroomusers":
            print(room_inventory.Room_inventory().displayroomusers(input_args[1]))
        
        else:
            break

    print("task is done")



main().run()