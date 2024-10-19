from mindustry.game import *

if __name__ == "__main__":
    Schematics = Schematics()
    with open("file-test.msch", "rb") as f:
        Schematics.read(f)