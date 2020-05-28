# This class holds the functions and attributes of game rules, time control and scoring. 
import Player as p
import random, string

player_list = []

class Game:
    
    def __init__(self):
        self.time_limit = 30

    def initGame(self, number_of_players, number_of_rounds, game_type):
        self.number_of_players = number_of_players
        self.number_of_rounds = number_of_rounds
        self.game_type = game_type

    def addPlayers(self):
        for i in range(self.number_of_players):
            name = input("Enter the player # " + str(i+1) + " username: ")
            player_list.append(p.Player(name, i,0))

    def letterRandomizer(self):
        return random.choice(string.ascii_uppercase)
    
    def gameIntro(self):
        print("Welcome to the Name-City Game")
        print("-----------------------------")
        print("Before game starts you will be demanded following information:")
        print("1. # of Players")
        print("2. # of Rounds")
        print("3. Game Mode [0:Classic, 1:Music, 2:Sports]")
        print("4. Time Limit per Round")
        print("Enjoy the game :)")
        print("-----------------------------")

game = Game()
game.gameIntro()

number_of_players = int(input("Enter the number of players: "))
number_of_rounds = int(input("Enter the number of rounds: "))
game_type = int(input("Enter the type of game: "))

game.initGame(number_of_players, number_of_rounds, game_type)
game.addPlayers()
print("Random letter is to be decided...")
print(game.letterRandomizer())