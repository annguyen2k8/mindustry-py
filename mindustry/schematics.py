import io
import base64

from .io import *

from .math import *

from .schematic import *
from .content import *

class Schematics:
    @staticmethod
    def readBase64(schematic:str) -> Schematic:
        return Schematics.read(io.BytesIO(base64.b64decode(schematic)))
    
    @staticmethod
    def read(_input:io.BytesIO) -> Schematic:
        for b in  b"msch" :
            if (b != _input.read(1)[0]):
                raise Exception("Not a schematic file (missing header).")
        
        ver = ord(_input.read(1))
        
        stream = Stream(_input)
        width, height = stream.readShort(), stream.readShort()
        print(f'{width=}')
        print(f'{height=}')
        
        if (width > 128 and height > 128):
            raise Exception("Invalid schematic: Too large (max possible size is 128x128)")
        tags:dict[str] = {}
        
        for i in range(stream.readUnsignedByte()):
            name = stream.readUTF()
            value = stream.readUTF()
            tags[name] = value
        
        blocks:dict[int, str] = {}
        length:bytes = stream.readByte()
        for i in range(length):
            # Block block = Vars.content.getByName(ContentType.block, SaveFileReader.fallback.get(name, name));
            # blocks.put(i, block == null || block instanceof LegacyBlock ? Blocks.air : block);
            name:str = stream.readUTF()
            blocks[i] = name
        print(f'{blocks=}')

        labels:str = [label for label in tags.get('labels', "[]")[1:-1].split(',') if label]
        print(f'{labels=}')
        
        total = stream.readInt()
        if (total > 128 * 128):
            raise Exception("Invalid schematic: Too many blocks.");
        print(f'{total=}')
        
        tiles:list[Stile] = []
        for i in range(total):
            i = stream.readUnsignedByte()
            block:str = blocks.get(i)
            position:int = stream.readInt()
            config:object = Schematics.mapConfig(block, stream.readByte(), position) if ver == 0 else Type.readObject(stream)
            rotation:bytes = stream.readByte()
            tiles.append(Stile(block, Point2.x(position), Point2.y(position), config, rotation))
            
            print(f'{block=}, {i=}', end=' ')
            print(f'position={Point2.x(position), Point2.y(position)}', end=' ')
            print(f'{rotation=}', end=' ')
            print()

        out:Schematic = Schematic(tiles, tags, width, height)
        if labels != None:
            out.labels.extend(labels)
        return out

    @staticmethod
    def mapConfig(block, value, position) -> object:
        # if(block instanceof Sorter || block instanceof Unloader || block instanceof ItemSource) return content.item(value);
        # if(block instanceof LiquidSource) return content.liquid(value);
        # if(block instanceof MassDriver || block instanceof ItemBridge) return Point2.unpack(value).sub(Point2.x(position), Point2.y(position));
        # if(block instanceof LightBlock) return value;
        return None