class Game:
    def __init__(self, players):
        self.gamers = list(players)


def start_game(self):
    print("Select the number of players (max of 4): ")
    num_players = input()
    while num_players < 0 or num_players > 4:
        print("Select the number of players (max of 4): ")
        num_players = input()
    for i in range(num_players):
        print("Select name for player {}".format(i+1))
        name = input()





