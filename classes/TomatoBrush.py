from classes.Tomato import Tomato


class TomatoBrush:

    def __init__(self, num_tomato):
        self.tomatoes = [Tomato(index) for index in range(0, num_tomato)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_tomatoes_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_all_harvesting(self):
        self.tomatoes = []
