from player import Player
from die import Die


class Game:
    def __init__(self, players):
        self.gamers = list(players)
        self.dice = [Die(1), Die(2), Die(3), Die(4), Die(5)]

    def announce_winner(self):
        high_score = 0
        winner = None
        for gamer in self.gamers:
            if high_score < gamer.get_score():
                winner = gamer
                high_score = gamer.get_score()
        print("{gamer} is the winner with score of {score}".format(gamer=winner, score=high_score))

    def start_game(self):
        finish = False
        while not finish:
            for gamer in self.gamers:
                print(gamer)
                gamer.play(self.dice)
            finish = not all([gamer.can_play() for gamer in self.gamers])
            print(finish)
        self.announce_winner()


def prepare_game():
    players = []
    print("Select the number of players (max of 4): ")
    num_players = int(input())
    while num_players < 0 or num_players > 4:
        print("Select the number of players (max of 4): ")
        num_players = input()
    for i in range(num_players):
        print("Select name for player {}".format(i + 1))
        name = input()
        players.append(Player(name))
    return players


players = prepare_game()
game = Game(players)
game.start_game()