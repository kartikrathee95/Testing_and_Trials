from typing import List
from team import Team
from datetime import datetime
class Tournament:
    teams: List[Team]
    id:str
    match_schedule = dict()
    def __init__(self,id):
        self.id = id

    def add_team(self,team:Team):
        self.teams.append(team)
        
    def remove_team(self,team:Team):
        self.teams.remove(team)

    def updateSchedule(self,Datetime:datetime, teams: List[Team]):
        self.match_schedule[datetime].append((teams[0],teams[1]))
    
