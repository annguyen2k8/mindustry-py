from .content import Content

class MappableContent(Content):
    name:str
    def __init__(self, name:str) -> None:
        self.name = name
        # this.name = Vars.content.transformName(name);
        # Vars.content.handleMappableContent(this);
        ...