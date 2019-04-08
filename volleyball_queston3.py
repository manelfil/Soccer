# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from Supertool.py import *

#game_width=150
#game height=90
class defense(Strategy):   #socceraction: cours ou shoot  #fait la passe+shoot
    def __init__(self):
        Strategy.__init__(self, "defense")    
    
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s= SuperState(state, id_team, id_player)
        
        #des que la balle va sur le terrain le defenseur court vers la ball
        action1= SoccerAction(acceleration=s.court_vers_balle_anticipe)
        
        # shoot vers le camp adverse
        action2= SoccerAction(shoot=s.fait_la_passe_loin)
        
        return action1+action2
    

    
    
