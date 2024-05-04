import random
class Dise:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second


dise=Dise()
print(dise.roll())