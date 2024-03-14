from classes.bowler import Bowler
from classes.batsman import Batsman
from team import Team
from enum import Enum
from typing import List



class Run(Enum):
    dot = 0
    single = 1
    double = 2
    triple = 3
    four = 4
    six = 6

class Extra(Enum):
    wide = "W"
    noball = "Nb"
    bye = "B"
    legbye = "LB"


class Wicket(Enum):
    BOLD = "bold"
    CAUGHT = "caught"
    STUMPED = "stumped"
    RUNOUT = "runout"
    LBW = "lbw"
    RETIRED_HURT = "retired_hurt"
    HIT_WICKET = "hit_wicket"
    OBSTRUCTING = "obstructing"



class Over:
    over_number = 0
    delivery = 0
    bowler: List[Bowler]
    batsman: List[Batsman]
    on_strike:Batsman
    over_container = dict()
    ball_type: str
    def __init__(self):
        self.over_number+=1

    def assignBowler(self,bowler):
        self.bowler = bowler
    
    def updateBatsman(self,players:List[Batsman], gotout = None):
        if gotout:
            self.batsman.remove(gotout)
           
        if len(players)>1:
            self.batsman.clear()
            for player in players:
                self.batsman.append(player)
        else:
            self.batsman.append(players[0])
            

    def changeStrike(self):
        if self.on_strike==self.batsman[0]:
            self.on_strike = self.batsman[1]
        else:
            self.on_strike = self.batsman[0]
    
    def updateOver(self,run:Run,ball,wicket=0):
        
    
        if ball =="F":
                self.delivery+=1
                if wicket:
                    self.over_container[self.over_number].append(Wicket.wicket)
                else: self.over_container[self.over_number].append(Run.run)

        else:
            self.over_container[self. over_number].append(str(Run.run)+ str(Ball.ball))

        if self.delivery == 6:
            