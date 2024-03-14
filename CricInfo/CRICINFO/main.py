from typing import List,Dict
from Matchcontroller import MatchController
from classes.over import Over
from classes.tournament import Tournament,Team
class main:
    tournament_mapper = Dict(str,Tournament)
    def __init__(self):
        pass
    
    def addTournament(self,tournament_id):
        tournament_ref = Tournament(tournament_id)
        self.tournament_mapper[tournament_id] = tournament_ref
        input = ("Enter the names of teams you want to add to tournament {}".format(tournament_id))
        while(True):

            team_name = input()
            if team_name== "exit":
                break
            team_id = len(tournament_ref.teams)
            tournament_ref.add_team(Team(team_id,team_name))

            print("enter exit when you are done adding teams")
        
    def run(self):
        input_args = input()
        