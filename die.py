import random


class Die:
    def __init__(self):
        self.face = 5

    def get_face(self):
        return self.face

    def throw(self):
        self.face = random.randint(1, 6)

    def __repr__(self):
        representation = {
            1: """   \n * \n   """,
            2: """  *\n   \n*  """,
            3: """  *\n * \n*  """,
            4: """* *\n   \n* *""",
            5: """* *\n * \n* *""",
            6: """* *\n* *\n* *"""
        }
        return representation[self.face]