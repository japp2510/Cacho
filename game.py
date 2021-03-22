from player import Player
from die import Die


class Game:
    def __init__(self, participants):
        self.gamers = list(participants)
        self.dice = [Die(1), Die(2), Die(3), Die(4), Die(5)]

    def announce_winner(self):
        high_score = 0
        winner = None
        for gamer in self.gamers:
            if high_score < gamer.get_score():
                winner = gamer
                high_score = gamer.get_score()
        print("{gamer} is the winner with score of {score}".format(gamer=winner.get_name(), score=high_score))

    def start_game(self):
        finish = False
        while not finish:
            for gamer in self.gamers:
                print(gamer)
                gamer.play(self.dice)
            finish = not all([gamer.can_play() for gamer in self.gamers])
        self.announce_winner()


def prepare_game():
    participants = []
    num_players = 0
    while num_players <= 0 or num_players > 4:
        print("Select the number of players (max of 4): ")
        value = input()
        num_players = (int(value) if value.isnumeric() else 0)
    for i in range(num_players):
        print("Select name for player {}".format(i + 1))
        name = input()
        participants.append(Player(name))
    return participants


players = prepare_game()
game = Game(players)
game.start_game()
