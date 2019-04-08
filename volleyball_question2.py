# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from Supertool.py import *

#game_width=150
#game height=90
class attaque(Strategy):   #socceraction: cours ou shoot  #fait la passe+shoot
    def __init__(self):
        Strategy.__init__(self, "attaque")    
    
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s= SuperState(state, id_team, id_player)
       # print(s.state.strategies)    
        #shoot a la position dist ball(position a laquelle on veut qu'il soit de l'adversaire)-adversaire  
     
       #faire la passe la plus loin possible de l'adversaire
       
       