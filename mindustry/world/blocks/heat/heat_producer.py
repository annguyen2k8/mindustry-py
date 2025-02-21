from ..production import GenericCrafter

class HeatProducer(GenericCrafter):
    heatOutput:float = 10.0
    warmupRate:float = 0.15
    
    def __init__(self, name):
        super().__init__(name)
        # drawer = new DrawMulti(new DrawDefault(), new DrawHeatOutput());
        self.rotateDraw = False
        self.rotate = True
        self.canOverdrive = False
        self.drawArrow = True