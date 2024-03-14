import random
from typing import List
from classes.over import Over,Run,Extra,Wicket
from classes.team import Team,Player
from classes.tournament import Tournament
from datetime import datetime
from CRICINFO.commentary import Commentary

class MatchController():
    match_id:str
    teams : List[Team]
    innings_over: bool
    innings:int
    batting_firstlineup = List[Player]
    batting_secondlineup = List[Player]
    Batting_team: Team
    Bowling_team: Team 
    batting_counter_1 = 0
    batting_counter_2 = 1
    def __init__(self):
        self.innings = 1
        
    def TeamSelector(self,*args):
        for team in args:
            self.teams.append(team)
    
    def createLineup(self,team):
        if len(self.batting_firstlineup)==0:
            self.batting_firstlineup = random.sample(team,11)
        else:
            self.batting_secondlineup = random.sample(team,11)
    def toss(self,teams):
        success = [0,1]
        toss_execute = random.sample(success,1)
        return teams[toss_execute],teams[not toss_execute]
    
    def runMatch(self):
        self.teams = Tournament.match_schedule[datetime.now()]
        print("match = {} is started between {} and {}",
              self.match_id,self.teams[0],self.teams[1])
        toss_winner_team,toss_lost_team = self.toss(self.teams)
        toss_winner_team.chooseTossOutcome()
        if toss_winner_team.playing_action == "batting":
            self.Batting_team = toss_winner_team
            self.Bowling_team = toss_lost_team
        else:
            self.Batting_team = toss_lost_team
            self.Bowling_team = toss_winner_team

        # Create initial scoreboard
        self.createLineup(self.Batting_team)
        self.createLineup(self.Bowling_team)

        # choose playing 11 for both teams. playing11_1 and playing11_2
        while(True):
            if self.innings_over:
                action_to_change = self.teams[0].playing_action
                self.teams[0].playing_action = self.teams[1].playing_action
                self.teams[1].playing_action = action_to_change
                self.innings+=1
                self.batting_counter_1 = 0
                self.batting_counter_2 = 1

            bowlers = Team.players["Bowlers"]
            bowler = random.sample(bowlers,1)
            over = Over()
            bowler = over.assignBowler()
            print(" Bowler {} bowls his nall no. {} to {} ".format(bowler.name, over.delivery,over.on_strike.name ))
            extras = list(item.name for item in Extra)
            extra = random.sample(extras,1)
            ball = random.sample(["fair","fair","fair","fair",extra[0]],1)
            ball = ball[0]
            over.ball_type = ball
            runs = list(item.value for item in Run)
            run = random.sample(runs,1)
            if ball not in extras:
                print("this is a fair delivery")
                if self.innings==1:
                    self.batting_firstlineup[self.batting_counter_1].score+=int(run)
                else:
                    self.batting_secondlineup[self.batting_counter_1].score+=int(run)
            else:
                print("bolwer bowled a {}".format(extra))
                runs = list(item.name for item in Run)
                run = random.sample(runs,1)

        

            

                
            


            
