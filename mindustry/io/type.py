from typing import *

from .stream import *
from ..math.geom import *

class Type:
    @staticmethod
    def readObject(stream:Stream, box:bool=False) -> Any:
        # byte type = read.b();
        _type = stream.readByte()
        # print(f'{_type=}')
        match _type:
            case 0: 
                return None
            case 1: 
                return stream.readInt()
            case 2: 
                return stream.readLong()
            case 3:
                return stream.readFloat()
            case 4:
                return Type.readString(stream)
            case 5:
                # return content.getByID(ContentType.all[read.b()], read.s())
                stream.readByte(); stream.readShort()
                return None
            case 6:
                length:int = stream.readShort()
                arr:List[int] = []
                for i in range(length):
                    arr.append(stream.readInt())
                return arr
            case 7:
                return Point2(stream.readInt(), stream.readInt())
            case 8:
                length:int = stream.readByte()
                out:List[Point2] = []
                for i in range(length):
                    p = Point2.unpack(stream.readInt())
                    out.append(p)
                return out
            case 9:
                # return content.<UnlockableContent>getByID(ContentType.all[read.b()], read.s()).techNode
                stream.readByte(); stream.readShort()
                return None
            case 10:
                return stream.readBool()
            case 11:
                return stream.readDouble()
            case 12:
                # return !box ? world.build(read.i()) : new BuildingBox(read.i())
                stream.readInt()
                return None
            case 13:
                # return LAccess.all[read.s()]
                stream.readShort()
                return None
            case 14:
                # int blen = read.i();
                # byte[] bytes = new byte[blen];
                # read.b(bytes);
                # yield bytes;
                blen:int = stream.readInt()
                out:List[bytes] = []
                for i in range(blen):
                    out.append(stream.readByte())
                return out
            
            # unit command
            
            case 15:
                stream.readByte()
                return None
            case 16:
                boollen:int = stream.readInt()
                bools:List[bool] = []
                for i in range(boollen):
                    bools.append(stream.readBool())
                return bools
            case 17:
                # return !box ? Groups.unit.getByID(read.i()) : new UnitBox(read.i());
                stream.readInt()
                return None
            case 18:
                length:int = stream.readInt()
                out:List[Vec2] = Vec2
                for i in range(length):
                    out.append(Vec2(stream.readFloat(), stream.readFloat()))
                return out
            case 19:
                return Vec2(stream.readFloat(), stream.readFloat())
            case 20:
                    # return Team.all[read.ub()]
                    stream.readUnsignedByte()
                    return None
            case 21:
                return Type.readInts(stream)
            case 22:
                objlen = stream.readShort()
                objs:List[object] = []
                for i in range(objlen):
                    objs.append(Type.readObject(stream, box))
                return objs
            case 23:
                # return UnitCommand.all.get(read.us())
                stream.readUnsignedShort()
                return None
            case _:
                raise Exception("Unknown object type:", _type)
    
    @staticmethod
    def readInts(stream: Stream) -> List[int]:
        length = stream.readShort()
        out:List[int] = []
        for i in range(length):
            out.append(stream.readInt())
        return out
    
    @staticmethod
    def readString(stream: Stream) -> str:
        exists = stream.readByte()
        if exists != 0:
            return stream.readUTF()
        return None