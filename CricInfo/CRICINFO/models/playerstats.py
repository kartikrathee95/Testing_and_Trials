from abc import ABC, abstractmethod
from typing import Dict, List
from player import Player
from classes.batsman import Batsman
from classes.bowler import Bowler


class CareerStats():
    player:Player
    runs:int
    wickets:int
    catches:int
    hundreds:int
    fifties: int
    five_wicket_innings: int

    def update(self,player):
        self.player = player
        




class TournamentStats():
    runs:int
    wickets:int
    catches:int
    hundreds:int
    fifties: int
    five_wicket_innings: int


class MatchStats():
    runs:int
    wickets:int
    catches:int
    hundreds:int
    fifties: int
    five_wicket_innings: int
    tournament_data: Dict[TournamentStats


    