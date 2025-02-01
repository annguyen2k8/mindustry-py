from mindustry.schematics import Schematics

if __name__ == "__main__":
    # with open("schem/debug-config.msch", "rb") as f:
    #     Schematics.read(f)
    Schematics.readBase64(input('>'))