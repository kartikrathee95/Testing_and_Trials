from datetime import datetime, time, timedelta
from typing import List
from movie import Movie, Seat, Show
from theatre import Theatre


class Controller():
    theatres: List[Theatre] = []
    usid: int = 0
    def __init__(self):
        self.usid+=1
    
    def addTheater(self, theatre:Theatre) -> None:
        self.theatres.append(theatre)
    
    def bookTicket(self, bookSeats):
        for seat in bookSeats:
            seat.available = False
        print(f"Booked seats {[seat.location for seat in bookSeats]}")

def main():
    controller = Controller()
    # create Theater and add halls
    theatre0 = Theatre()
    theatre0.addHall(100)
    theatre0.addHall(100)
    
    # create Movies and shows
    movie1 = Movie(name="movie1",duration = timedelta(hours=2, minutes=30))
    movie2 = Movie(name="movie2",duration = timedelta(hours=3, minutes=0))
    start_time = datetime.combine(datetime.today(),time(9,0,0))
    show1 = Show(movie1.name, start_time =start_time ,end_time = start_time+movie1.duration)
    show2 = Show(movie1.name, start_time = start_time+timedelta(hours=3),end_time = start_time+timedelta(hours=3)+movie1.duration)
    show3 = Show(movie2.name, start_time = start_time+timedelta(hours=1),end_time = start_time+timedelta(hours=1)+movie2.duration)
    show4 = Show(movie2.name, start_time = start_time+timedelta(hours=6),end_time = start_time+timedelta(hours=6)+movie2.duration)

    # add movies and shows
    hall0 = theatre0.getHall(0)
    hall1 = theatre0.getHall(1)
    hall0.addShow(show1, hall0.num_seats)
    hall0.addShow(show2, hall0.num_seats)
    hall1.addShow(show3, hall1.num_seats)
    hall1.addShow(show4, hall1.num_seats)

    # book ticket
    controller = Controller()
    selectHall = None
    selectShow = None
    print(f"Select the hall to book the ticket {theatre0.getHalls()}")
    selectHall = theatre0.getHall(int(input()))
    print(f"Select the show {selectHall.getShows()}",)
    show_input = input()
    movie_name = show_input[show_input.find("'")+1:show_input.find(",")-1]
    duration = datetime(*(list(map(int,show_input[show_input.find("datetime.datetime")+ len("datetime.datetime("):show_input.find(')')].split(',')))))

    show_input_parsed = (movie_name, duration)
    selectShow = selectHall.getShow(show_input_parsed)

    print(f"Choose your preferred seats from {selectShow.displayAvailableSeats()}")
    print("Enter -1 if you`ve finished seats selection")
    bookSeats = []
    while 1:
        seat = int(input())
        if seat==-1:
            break
        bookSeats.append(seat)
    try:
        controller.bookTicket(selectShow.getSelectedSeats(bookSeats))
        print("Tickets booked successfully")
        print(f"Updated available seats: {[seat.location for seat in selectShow.getAvailableSeats()]}")
    except Exception as exception:
        print(f"An error occurred {str(exception)}")



if __name__=='__main__':
    main()