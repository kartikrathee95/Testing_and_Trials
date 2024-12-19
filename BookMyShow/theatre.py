import datetime
from typing import List
from movie import Show


class Hall():

    def __init__(self, num_seats):
        self.shows: List[Show] = []
        self.num_seats = num_seats

    def addShow(self, show, num_seats):
        show.addSeats(num_seats)
        self.shows.append(show)

    def getShows(self):
        allShows = []
        for show in self.shows:
            allShows.append((show.name, show.start_time))
        return allShows
    
    def getShow(self, show_details):
        for show in self.shows:
            if show.name==show_details[0] and show.start_time==show_details[1]:
                return show
        return None


class Theatre():
    halls: List[Hall] = []

    def addHall(self, num_seats):
        self.halls.append(Hall(num_seats=num_seats))

    def getHalls(self) -> List:
        return [i for i in range(len(self.halls))]
    
    def getHall(self, hallId):
        return self.halls[hallId]
