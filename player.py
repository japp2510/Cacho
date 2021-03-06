from square import Big
from square import Full
from square import Poker
from square import Square
from square import Stair


def correct_input():
    choices = ["1", "2", "3", "4", "5"]
    response = ""
    while response == "":
        print("Introduce the dices you wanna throw (exp : 12345 or 245) 0 if you wanna score dice: \n")
        dice_throw = input("")
        if dice_throw[0] == "0":
            return "0"
        for character in dice_throw:
            if character in choices:
                response += character
    print("Throwing dices : {}".format(list(response)))
    return response


def set_board():
    return [[Square(1), Stair(), Square(4)], [Square(2), Full(), Square(5)], [Square(3), Poker(), Square(6)],
            [Big(), Big()]]


class Player:
    def __init__(self, name):
        self.name = name
        self.board = set_board()
        self.max_turn = 11
        self.play_turn = 0
        self.score = 0

    def get_name(self):
        return self.name

    def can_play(self):
        return self.play_turn < self.max_turn

    def get_score(self):
        self.score = 0
        for row in self.board:
            for box in row:
                self.score += box.get_score()
        return self.score

    def __repr__(self):
        representation = "\n\n{}\n".format(self.name)
        self.score = 0
        for row in self.board:
            for box in row:
                self.score += box.get_score()
                representation += str(box) + " |"
            representation += "\n"
        representation += "Score : {}\n".format(self.score)
        return representation

    def get_square(self, choices_board):
        box = None
        while box is None:
            print("Select which square in board you want to select : ")
            print(choices_board)
            square = input()
            for i, lst in enumerate(choices_board):
                for j, letter in enumerate(lst):
                    if letter == square or letter.capitalize() == square:
                        if self.board[i][j].selected:
                            print("Square was already selected please choose another one")
                        else:
                            box = self.board[i][j]
        return box

    def play(self, dice):
        choices_board = [["1", "S", "4"], ["2", "F", "5"], ["3", "P", "6"], ["B", "G"]]
        turn = 0
        dice_throw = "12345"
        while turn < 3:
            for index in dice_throw:
                i = int(index) - 1
                dice[i].throw()
            print("Turn {}:".format(turn + 1))
            print(dice)
            if turn != 2:
                dice_throw = correct_input()
                if dice_throw == "0":
                    break
            turn += 1
        square = self.get_square(choices_board)
        square.calculate_score(dice, turn == 0)
        self.play_turn += 1
        print("Turn ended!")
