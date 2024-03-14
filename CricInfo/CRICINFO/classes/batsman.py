from models.player import Player
class Batsman(Player):
    name:str
    type_of_player = None

    def __init__(self,name,type_of_player):
        super().__init__(self,name,type_of_player="Batsman")
    