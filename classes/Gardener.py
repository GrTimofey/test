class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Finish')

    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_tomatoes_are_ripe():
            self._plant.give_all_harvesting()
            print('Harvesting is end')
        else:
            print('Too early')