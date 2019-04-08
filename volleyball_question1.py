# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from Supertool.py import *

#game_width=150
#game height=90

class Echauffement(Strategy):   #socceraction: cours ou shoot  #fait la passe+shoot
    def __init__(self):
        Strategy.__init__(self, "echauffement")    
    
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s= SuperState(state, id_team, id_player)
       # print(s.state.strategies)    
       
       return SoccerAction(shoot=(s.renvoie_ball_a_adversaire))
       
       
    
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Echauffement())  # Random strategy
team2.add("Player 2", Echauffement())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
    
    
        

           