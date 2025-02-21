from ...block import Block

class HeatConductor(Block):
    visualMaxHeat:float = 15.0
    # public DrawBlock drawer = new DrawDefault();
    splitHeat:bool = False
    
    def __init__(self, name):
        super().__init__(name)
        self.update = True
        self.solid = True
        self.rotate = True
        self.rotateDraw = True
        self.size = 3