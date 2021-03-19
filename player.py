from square import Square
from square import Stair
from square import Full
from square import Poker
from square import Big


class Player:
    def __init__(self, name):
        self.name = name
        self.board = self.set_board()

    def set_board(self):
        return [[Square(1), Stair(), Square(4)], [Square(2), Full(), Square(5)], [Square(3), Poker(), Square(6)],
                [Big(), Big()]]
