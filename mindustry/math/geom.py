from __future__ import annotations

class Point2():
    def __init__(self, x:int, y:int):
        self.x, self.y = x, y
    
    @staticmethod
    def x(pos:int) -> int:
        return int(pos >> 16)
    
    @staticmethod
    def y(pos:int) -> int:
        return int(pos & 0xFFFF)

    @staticmethod
    def unpack(pos:int) -> Point2:
        return Point2(int(pos >> 16), int(pos & 0xFFFF))

class Vec2:
    x:float
    y:float
    
    def __init__(self, x:float, y:float):
        self.x, self.y = x, y
    