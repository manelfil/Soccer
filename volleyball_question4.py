from mondepot import volleyball_question1.py, volleyball_question2.py, volleyball_question3.py
from soccersimulator import SoccerTeam

team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", attaque())  # Random strategy
team2.add("Player 2", defense())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
    