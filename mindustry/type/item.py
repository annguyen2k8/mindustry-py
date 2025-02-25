from mindustry.graphics import *
from mindustry.ctype import *

class Item(UnblockableContent):
    color:Color
    
    explosiveness:float = 0.0
    flammability:float = 0.0
    radioactivity:float
    charge:float = 0.0
    hardness:int = 0
    charge:float = 0.0
    cost:float = 1.0
    healthScaling:float = 0.0
    lowPriority:bool
    
    frames:int = 0
    transitionFrames:int = 0
    frameTime:float = 5.0
    
    buildAble:bool = True
    hidden:bool = False
    # public @Nullable Planet[] hiddenOnPlanets
    
    def __init__(self, name, color:Color=Colors.black) -> None:
        super().__init__(name)
        self.color = color
    
    def getContentType(self) -> ContentType:
        return ContentType.item