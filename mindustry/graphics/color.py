from __future__ import annotations

class Color:
    r: float
    g: float
    b: float
    a: float
    def __init__(self, r: float, g: float, b: float, a: float = 1.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.clamp()

    @staticmethod
    def fromRgba8888(rgba8888: int):
        r = ((rgba8888 & 0xff000000) >> 24) / 255.0
        g = ((rgba8888 & 0x00ff0000) >> 16) / 255.0
        b = ((rgba8888 & 0x0000ff00) >> 8) / 255.0
        a = (rgba8888 & 0x000000ff) / 255.0
        return Color(r, g, b, a)

    def clamp(self):
        self.r = max(0.0, min(1.0, self.r))
        self.g = max(0.0, min(1.0, self.g))
        self.b = max(0.0, min(1.0, self.b))
        self.a = max(0.0, min(1.0, self.a))

    @staticmethod
    def valueOf(code: str) -> Color:
        offset: int = 1 if code[0] == '#' else 0
        r: int = int(code[offset:offset + 2], 16)
        g: int = int(code[offset + 2:offset + 4], 16)
        b: int = int(code[offset + 4:offset + 6], 16)
        a: int = 255 if len(code) - offset != 8 else int(code[offset + 6:offset + 8], 16)
        return Color(r / 255.0, g / 255.0, b / 255.0, a / 255.0)
    
    @staticmethod
    def grays(value:float) -> Color:
        return Color(value, value, value)
    
    def set_a(self, value:float) -> Color:
        self.a = value
        return self

    def mul(self, value:float) -> Color:
        self.r *= value
        self.b *= value
        self.g *= value
        self.a *= value
        return self

class Colors:
    white = Color(1, 1, 1, 1)
    lightGray = Color.fromRgba8888(0xbfbfbfff)
    gray = Color.fromRgba8888(0x7f7f7fff)
    darkGray = Color.fromRgba8888(0x3f3f3fff)
    black = Color(0, 0, 0, 1)
    clear = Color(0, 0, 0, 0)

    blue = Color(0, 0, 1, 1)
    navy = Color(0, 0, 0.5, 1)
    royal = Color.fromRgba8888(0x4169e1ff)
    slate = Color.fromRgba8888(0x708090ff)
    sky = Color.fromRgba8888(0x87ceebff)
    cyan = Color(0, 1, 1, 1)
    teal = Color(0, 0.5, 0.5, 1)

    green = Color.fromRgba8888(0x00ff00ff)
    acid = Color.fromRgba8888(0x7fff00ff)
    lime = Color.fromRgba8888(0x32cd32ff)
    forest = Color.fromRgba8888(0x228b22ff)
    olive = Color.fromRgba8888(0x6b8e23ff)

    yellow = Color.fromRgba8888(0xffff00ff)
    gold = Color.fromRgba8888(0xffd700ff)
    goldenrod = Color.fromRgba8888(0xdaa520ff)
    orange = Color.fromRgba8888(0xffa500ff)

    brown = Color.fromRgba8888(0x8b4513ff)
    tan = Color.fromRgba8888(0xd2b48cff)
    brick = Color.fromRgba8888(0xb22222ff)

    red = Color.fromRgba8888(0xff0000ff)
    scarlet = Color.fromRgba8888(0xff341cff)
    crimson = Color.fromRgba8888(0xdc143cff)
    coral = Color.fromRgba8888(0xff7f50ff)
    salmon = Color.fromRgba8888(0xfa8072ff)
    pink = Color.fromRgba8888(0xff69b4ff)
    magenta = Color(1, 0, 1, 1)

    purple = Color.fromRgba8888(0xa020f0ff)
    violet = Color.fromRgba8888(0xee82eeff)
    maroon = Color.fromRgba8888(0xb03060ff)

if __name__ == '__main__':
    c = Color.valueOf('#FF00FF80')
    print(c.r, c.g, c.b, c.a)