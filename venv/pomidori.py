class Tomato:
    states = {1:"зелёный",2:"почти",3:"спелый",4:"гнилой"}
    a = 0
    def __init__(self,_index):
        self._index = _index
        self.state = 0

    def grow(self):
        self.state += 1

    def is_ripe(self):
        if self.state == 3:
            print("Done")

class TomatoBush:

    def __init__(self,num):
        self.tomatoes=[Tomato(index) for index in range(num)]
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:

            if i in self.state == 3:
                a += 1
                if a == num:
                    return True
    def give_away_all(self):
        self.tomatoes = clear

class Gardener

    def __init__(self,name,_plant):
        self.name = name
        self._plant = Gardener.Tomato()

    def work(self):
        self.is_ripe()

    def harvest(self):
