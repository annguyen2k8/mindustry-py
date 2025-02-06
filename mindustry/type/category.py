from enum import Enum

class Category(Enum):
    turret = 1
    production = 2
    distribution = 3
    liquid = 4
    power = 5
    defense = 6
    crafting = 7
    units = 8
    effect = 9
    logic = 10

    @classmethod
    def all(cls):
        return list(cls)

    def prev(self):
        all_categories = self.all()
        return all_categories[(self.value - 2) % len(all_categories)]

    def next(self):
        all_categories = self.all()
        return all_categories[self.value % len(all_categories)]