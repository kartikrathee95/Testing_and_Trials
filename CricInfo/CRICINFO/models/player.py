class Player:
    name:str
    type_of_player:str
    score:int
    wickets:int
    catches:int
    def __init__(self,name,type_of_player):
        self.name = name
        self.type_of_player = type_of_player
        self.score = 0
        self.wickets = 0
        self.catches = 0
    
    