from .status_effects import *
from ..type import *
from ..graphics import *

class Liquids:
    water = Liquid('water', Color.valueOf('596ab8'))
    water.heatCapacity = 0.4
    water.effect = StatusEffects.wet
    water.boilPoint = 0.5
    water.gasColor = Color.grays(0.9)
    
    slag = Liquid('slag', Color.valueOf('ffa166'))
    slag.temperature = 1.0
    slag.viscosity = 0.7
    slag.effect = StatusEffects.melting
    slag.lightColor = Color.valueOf('f0511d').set_a(0.4)
    
    oil = Liquid('oil', Color.valueOf('313131'))
    oil.viscosity = 0.75
    oil.flammability = 1.2
    oil.explosiveness = 1.2
    oil.heatCapacity = 0.7
    oil.barColor = Color.valueOf('6b675f')
    oil.effect = StatusEffects.tarred
    oil.boilPoint = 0.65
    oil.gasColor = Color.grays(0.4)
    oil.canStayOn.add(water)
    
    cryofluid = Liquid('cryofluid', Color.valueOf('6ecdec'))
    cryofluid.heatCapacity = 0.9
    cryofluid.temperature = 0.25
    cryofluid.effect = StatusEffects.freezing
    cryofluid.lightColor = Color.valueOf('0097f5').set_a(0.2)
    cryofluid.boilPoint = 0.55
    cryofluid.gasColor = Color.valueOf('c1e8f5')
    
    neoplasm = CellLiquid('neoplasm', Color.valueOf('c33e2b'))
    neoplasm.heatCapacity = 0.4
    neoplasm.temperature = 0.54
    neoplasm.viscosity = 0.85
    neoplasm.flammability = 0
    neoplasm.capPuddles = False
    neoplasm.spreadTarget = water
    neoplasm.moveThroughBlocks = True
    neoplasm.incinerable = False
    neoplasm.blockReactive = False
    neoplasm.canStayOn.update([water, oil, cryofluid])
    
    neoplasm.colorFrom = Color.valueOf('e8803f')
    neoplasm.colorTo = Color.valueOf('8c1225')
    
    arkycite = Liquid('arkycite', Color.valueOf('84a94b'))
    arkycite.flammability = 0.4
    arkycite.viscosity = 0.7
    neoplasm.canStayOn.add(arkycite)
    
    gallium = Liquid('gallium', Color.valueOf('9a9dbf'))
    gallium.coolant = False
    gallium.hidden = True
    
    ozone = Liquid('ozone', Color.valueOf('fc81dd'))
    ozone.gas = True
    ozone.barColor = Color.valueOf('d699f0')
    ozone.explosiveness = 1.0
    ozone.flammability = 1.0
    
    hydrogen = Liquid('hydrogen', Color.valueOf('9eabf7'))
    hydrogen.gas = True
    hydrogen.flammability = 1.0
    
    nitrogen = Liquid('nitrogen', Color.valueOf('efe3ff'))
    nitrogen.gas = True
    
    cyanogen = Liquid('cyanogen', Color.valueOf('89e8b6'))
    cyanogen.gas = True
    cyanogen.flammability = 2.0