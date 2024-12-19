from datetime import datetime, time
from typing import List


class Seat():
    location: tuple

    def __init__(self, location):
        self.location = location
        self.available: bool = True
    
    def __str__(self):
        return f"Seat {self.location}"
    
    def getSeat(self) -> object:
        return self

    def updateAvailability(self, available):
        self.available = available


class Show():
    start_time: time
    end_time: time
    duration: time
    name: str
    
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.availableSeats: List[Seat] = []
    
    def addSeats(self, num_seats):
        for seat_n in range(num_seats):
            self.availableSeats.append(Seat(seat_n))
            
    def getAvailableSeats(self):
        seatsAvailable = []
        for seat in self.availableSeats:
            if seat.available==True:
                seatsAvailable.append(seat)
        return seatsAvailable

    def displayAvailableSeats(self):
        available_seats = self.getAvailableSeats()
        if available_seats:
            for seat in available_seats:
                print(seat)
        else:
            print("No seats available for the show '{}'.".format(self.name))
        
    def getSelectedSeats(self, selectedSeats) -> List[Seat]:
        return [seat for seat in self.availableSeats if seat.location in selectedSeats and seat.available]


class Movie():
    name: str
    duration: time

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
    