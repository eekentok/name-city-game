# This class holds the functions and attributes of players.

class Player:

    def __init__(self, username, player_id, score):
        self.username = username
        self.player_id = player_id
        self.score = score

# Player samples
p1 = Player("ehemingway", 1, 0)
p2 = Player("szweig", 2, 0)

print(p1.username + " id = " + str(p1.player_id) + ". His score is " + str(p1.score))
print(p2.username + " id = " + str(p2.player_id) + ". His score is " + str(p2.score))