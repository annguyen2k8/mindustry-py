from mindustry.graphics import *
from mindustry.type import *

class Liquids:
    water:Liquid
    slag:Liquid
    oil:Liquid
    cryofluid:Liquid
    neoplasm:CellLiquid
    arkycite:Liquid
    gallium:Liquid
    ozone:Liquid
    hydrogen:Liquid
    nitrogen:Liquid
    cyanogen:Liquid

    @staticmethod
    def load():
        Liquids.water = Liquid('water', Color.valueOf('596ab8'))
        Liquids.water.heatCapacity = 0.4
        Liquids.water.effect = StatusEffects.wet
        Liquids.water.boilPoint = 0.5
        Liquids.water.gasColor = Color.grays(0.9)

        Liquids.slag = Liquid('slag', Color.valueOf('ffa166'))
        Liquids.slag.temperature = 1.0
        Liquids.slag.viscosity = 0.7
        Liquids.slag.effect = StatusEffects.melting
        Liquids.slag.lightColor = Color.valueOf('f0511d').cpy().set_a(0.4)

        Liquids.oil = Liquid('oil', Color.valueOf('313131'))
        Liquids.oil.viscosity = 0.75
        Liquids.oil.flammability = 1.2
        Liquids.oil.explosiveness = 1.2
        Liquids.oil.heatCapacity = 0.7
        Liquids.oil.barColor = Color.valueOf('6b675f')
        Liquids.oil.effect = StatusEffects.tarred
        Liquids.oil.boilPoint = 0.65
        Liquids.oil.gasColor = Color.grays(0.4)
        Liquids.oil.canStayOn.add(Liquids.water)

        Liquids.cryofluid = Liquid('cryofluid', Color.valueOf('6ecdec'))
        Liquids.cryofluid.heatCapacity = 0.9
        Liquids.cryofluid.temperature = 0.25
        Liquids.cryofluid.effect = StatusEffects.freezing
        Liquids.cryofluid.lightColor = Color.valueOf('0097f5').cpy().set_a(0.2)
        Liquids.cryofluid.boilPoint = 0.55
        Liquids.cryofluid.gasColor = Color.valueOf('c1e8f5')

        Liquids.neoplasm = CellLiquid('neoplasm', Color.valueOf('c33e2b'))
        Liquids.neoplasm.heatCapacity = 0.4
        Liquids.neoplasm.temperature = 0.54
        Liquids.neoplasm.viscosity = 0.85
        Liquids.neoplasm.flammability = 0
        Liquids.neoplasm.capPuddles = False
        Liquids.neoplasm.spreadTarget = Liquids.water
        Liquids.neoplasm.moveThroughBlocks = True
        Liquids.neoplasm.incinerable = False
        Liquids.neoplasm.blockReactive = False
        Liquids.neoplasm.canStayOn.update([Liquids.water, Liquids.oil, Liquids.cryofluid])
        Liquids.neoplasm.colorFrom = Color.valueOf('e8803f')
        Liquids.neoplasm.colorTo = Color.valueOf('8c1225')

        Liquids.arkycite = Liquid('arkycite', Color.valueOf('84a94b'))
        Liquids.arkycite.flammability = 0.4
        Liquids.arkycite.viscosity = 0.7
        Liquids.neoplasm.canStayOn.add(Liquids.arkycite)

        Liquids.gallium = Liquid('gallium', Color.valueOf('9a9dbf'))
        Liquids.gallium.coolant = False
        Liquids.gallium.hidden = True

        Liquids.ozone = Liquid('ozone', Color.valueOf('fc81dd'))
        Liquids.ozone.gas = True
        Liquids.ozone.barColor = Color.valueOf('d699f0')
        Liquids.ozone.explosiveness = 1.0
        Liquids.ozone.flammability = 1.0

        Liquids.hydrogen = Liquid('hydrogen', Color.valueOf('9eabf7'))
        Liquids.hydrogen.gas = True
        Liquids.hydrogen.flammability = 1.0

        Liquids.nitrogen = Liquid('nitrogen', Color.valueOf('efe3ff'))
        Liquids.nitrogen.gas = True

        Liquids.cyanogen = Liquid('cyanogen', Color.valueOf('89e8b6'))
        Liquids.cyanogen.gas = True
        Liquids.cyanogen.flammability = 2.0