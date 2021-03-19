from die import Die


class Square:
    def __init__(self, value):
        self.value = value
        self.quantity = 0
        self.score = 0
        self.selected = False

    def calculate_score(self, dice):
        if not self.selected:
            for die in dice:
                if die.get_face() == self.value:
                    self.quantity += 1
            self.score = self.quantity * self.value
            self.selected = True

    def get_score(self):
        return self.score

    def __repr__(self):
        return str(self.score)


class Stair:
    def __init__(self):
        self.score = 0
        self.selected = False

    def calculate_score(self, dice, first=False):
        if not self.selected:
            condition = [False] * 5
            for die in dice:
                index = die.get_face() - 1 if die.get_face() < 6 else 0
                if not condition[index]:
                    condition[index] = True
                else:
                    break
            self.score = (20 + (5 if first else 0)) if all(condition) else 0
            self.selected = True

    def get_score(self):
        return self.score

    def __repr__(self):
        if self.score == 0:
            return str(0)
        elif self.score == 20:
            return "()"
        elif self.score == 25:
            return "$"


class Full:
    def __init__(self):
        self.score = 0
        self.selected = False
        self.x = {'face': 0, 'cant': 0}
        self.y = {'face': 0, 'cant': 0}

    def is_full(self):
        return ((self.x['cant'] + self.y['cant']) == 5) & (self.x['cant'] == 2 or self.y['cant'] == 2)

    def calculate_score(self, dice, first=False):
        if not self.selected:
            for die in dice:
                if self.x['face'] == 0 or self.x['face'] == die.get_face():
                    self.x['face'] = die.get_face()
                    self.x['cant'] += 1
                elif self.y['face'] == 0 or self.y['face'] == die.get_face():
                    self.y['face'] = die.get_face()
                    self.y['cant'] += 1
                else:
                    break
            condition = self.is_full()
            print(condition)
            self.score = (30 + (5 if first else 0)) if condition else 0
            self.selected = True

    def get_score(self):
        return self.score

    def __repr__(self):
        if self.score == 0:
            return str(0)
        elif self.score == 30:
            return "()"
        elif self.score == 35:
            return "$"


dice = [Die(2), Die(1), Die(3), Die(3), Die(3)]

full = Full()
for die in dice:
    die.throw()
    print("---")
    print(die)
    print("\n")

full.calculate_score(dice)
print(full)
