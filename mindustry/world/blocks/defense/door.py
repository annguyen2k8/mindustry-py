from .wall import Wall

class Door(Wall):
    def __init__(self, name):
        super().__init__(name)
        self.solid = False
        self.solidifes = True
        self.consumesTap = True