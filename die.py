import random


class Die:
    def __init__(self, value=5):
        self.face = value

    def get_face(self):
        return self.face

    def throw(self):
        self.face = random.randint(1, 6)

    def __repr__(self):
        return str(self.face)
