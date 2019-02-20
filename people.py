class Person(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
            return self.name + " exists"

p1 = Person("Andrew")
p2 = Person("Mattia")

for p in [p1, p2]:
    print(str(p))
