class Person(object):
    def __init__(self, name, is_great=False):
        self.name = name
        self.is_great = is_great

    def __repr__(self):
        if self.is_great:
            return self.name + " is great"
        else:
            return self.name + " is okay, I suppose"

p1 = Person("Andrew")
p2 = Person("Mattia")

for p in [p1, p2]:
    print(str(p))

