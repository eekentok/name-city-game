# This class holds the functions and attributes of game rules, time control and scoring. 
import Player as p

player_list = []

class Game:

    def __init__(self):
        self.number_of_players = int(input("Enter the number of players: "))
        self.number_of_rounds = int(input("Enter the number of rounds: "))
        self.game_type = input("Enter the type of game: ")
        self.time_limit = 30
    
    def addPlayers(self):
        for i in range(self.number_of_players):
            name = input("Enter your username: ")
            player_list.append(p.Player(name, i,0))

Game().addPlayers()

'''
    def __init__(self, number_of_players, number_of_rounds, game_type, time_limit):
        self.number_of_players = number_of_players
        self.number_of_rounds = number_of_rounds
        self.game_type = game_type
        self.time_limit = time_limit

        
    def createGame(self):
        size = input("Enter the number of players: ")
        length =  input("Enter the number of rounds: ")
        mode = input("Enter the type of game: ")
        limit = 30
        return Game(size, length, mode, limit)
'''