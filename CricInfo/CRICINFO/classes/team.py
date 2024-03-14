import random
from typing import List,Dict
from models.player import Player

class Team:
    players: Dict(List[Player])
    name:str
    playing11: List[Player]
    playing_action: str
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def add_player(self,player:Player):
        if player.type_of_player== "Batsman":
            self.players["Batsmen"].append(player)
        elif player.type_of_player == "Bowler":
            self.players["Bowlers"].append(player)

    def remove_player(self,player:Player):
        self.players.remove(player)
    
    def chooseTossOutcome(self):
        choice = input("choose batting/bowling")
        if choice=="batting":
            self.playing_action = "batting"
        else:
            self.playing_action = "bowling"
    def change_playing_action(self):
        if self.playing_action=="batting":
            self.playing_action = "bowling"
        else:
            self.playing_action = "batting"
            
    def selectPlaying11(self,selection_algorithm = None):

        if selection_algorithm == None:
           self.playing11 = random.sample(self.players,11)
        else:
            for select_player in self.players:
                player_selected = input("Do you want to select {}, Yes/No".format(select_player))
                if player_selected =="Yes":
                    self.playing11.append(select_player)