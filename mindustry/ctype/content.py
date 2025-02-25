from . import *

from mindustry.core import *

class Content:
    id:int
    # public ModContentInfo minfo = new ModContentInfo();
    def __init__(self):
        self.id = Vars.content.getBy(self.getContentType()).size
        Vars.content.handleContent(self)
    
    def getContentType(self) -> ContentType: pass