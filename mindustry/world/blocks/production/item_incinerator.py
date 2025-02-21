from ... import Block

class ItemIncinerator(Block):
    # public Effect effect = Fx.incinerateSlag;
    effectChance:float = 0.2
    
    def __init__(self, name):
        super().__init__(name)
        self.update = True
        self.solid = True