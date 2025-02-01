from mindustry import Schematics

if __name__ == "__main__":
    Schematics = Schematics()
    with open("schem/file.msch", "rb") as f:
        Schematics.read(f)