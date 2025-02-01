from __future__ import annotations

from functools import singledispatchmethod
from typing import *

class Color:
    r:float
    g:float
    b:float
    a:float
    
    @singledispatchmethod
    def __init__(self, r:float, g:float, b:float, a:float=1):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        
        self.clamp()
    
    @__init__.register
    def _(self, rgba8888:int):
        self.r = ((rgba8888 & 0xff000000) >> 24) / 255
        self.g = ((rgba8888 & 0x00ff0000) >> 16) / 255
        self.b = ((rgba8888 & 0x0000ff00) >> 8) / 255
        self.a = ((rgba8888 & 0x000000ff)) / 255
        
        self.clamp()
    
    def clamp(self) -> None:
        if self.r < 0:
            self.r = 0
        elif self.r > 1:
            self.r = 1
        
        if self.g < 0:
            self.g = 0
        elif self.g > 1:
            self.g = 1
        
        if self.b < 0:
            self.b = 0
        elif self.b > 1:
            self.b = 1
            self.b = 1
        
        if self.a < 0:
            self.a = 0
        elif self.a > 1:
            self.a = 1
            self.a = 1
        return self
    
    @staticmethod
    def valueOf(code:str) -> Color:
        offset:int = 1 if code[0] == '#' else 0
        r:int = int(code[offset    :offset + 2], 16)
        g:int = int(code[offset + 2:offset + 4], 16)
        b:int = int(code[offset + 4:offset + 6], 16)
        a:int = 255 if len(code) - offset != 8 else Color.parseHex(code, offset + 6, offset + 8)
        return Color(r / 255, g / 255, b/255, a / 255)

class Colors:
    pwhite = Color(1, 1, 1, 1)
    lightGray = Color(0xbfbfbfff)
    gray = Color(0x7f7f7fff)
    darkGray = Color(0x3f3f3fff)
    black = Color(0, 0, 0, 1)
    clear = Color(0, 0, 0, 0)

    blue = Color(0, 0, 1, 1)
    navy = Color(0, 0, 0.5, 1)
    royal = Color(0x4169e1ff)
    slate = Color(0x708090ff)
    sky = Color(0x87ceebff)
    cyan = Color(0, 1, 1, 1)
    teal = Color(0, 0.5, 0.5, 1)

    green = Color(0x00ff00ff)
    acid = Color(0x7fff00ff)
    lime = Color(0x32cd32ff)
    forest = Color(0x228b22ff)
    olive = Color(0x6b8e23ff)

    yellow = Color(0xffff00ff)
    gold = Color(0xffd700ff)
    goldenrod = Color(0xdaa520ff)
    orange = Color(0xffa500ff)

    brown = Color(0x8b4513ff)
    tan = Color(0xd2b48cff)
    brick = Color(0xb22222ff)

    red = Color(0xff0000ff)
    scarlet = Color(0xff341cff)
    crimson = Color(0xdc143cff)
    coral = Color(0xff7f50ff)
    salmon = Color(0xfa8072ff)
    pink = Color(0xff69b4ff)
    magenta = Color(1, 0, 1, 1)

    purple = Color(0xa020f0ff)
    violet = Color(0xee82eeff)
    maroon = Color(0xb03060ff)


if __name__ == '__main__':
    c = Color.valueOf('#FF00FF80')
    print(c.r, c.b, c.g, c.a)