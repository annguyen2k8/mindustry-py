from __future__ import annotations
from typing import *

from mindustry.content import *
from mindustry.ctype import *
from mindustry.type import *
from mindustry.world import *
from mindustry.vars import *

class ContentLoader:
    contentNameMap:Dict[str, MappableContent] = []
    contentMap:set[Content] = set()
    nameMap:Dict[str, MappableContent] = []
    temporaryMapper:List[List]
    
    lastAdded:Content = None

    def __init__(self):
        for contentType in ContentType:
            ContentLoader.contentMap[contentType.name] = set()
            ContentLoader.contentNameMap[contentType.name] = {}
    
    def createBaseContent(self):
        Item.load()
        Block.load()
        StatusEffects.load()
    
    def getByName(self, contentType:ContentType, name:str) -> MappableContent:
        mapContent = ContentLoader.contentMap.get(contentType)
        if mapContent == None:
            return None
        return mapContent.get(name)
    
    def handleContent(self, content:Content):
        self.lastAdded = content
        Content.contentMap[content.getContentType().name].add(content)
    
    def getBy(self, contentType:ContentType) -> Content:
        return ContentLoader.contentMap[contentType.name]
    
    def handleMappableContent(self, content:MappableContent):
        if content.name in ContentLoader.contentNameMap[content.getContentType().name]:
            listContent = ContentLoader.contentNameMap[content.getContentType().name]
            if len(listContent) > 0 and listContent[-1] == content:
                listContent.pop()
            else:
                raise Exception("Two content objects cannot have the same name! (issue: '" + content.name + "')")
        ContentLoader.contentNameMap[content.getContentType().name][content.name] = content
        # nameMap.put(content.name, content)