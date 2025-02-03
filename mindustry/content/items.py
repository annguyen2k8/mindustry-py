from __future__ import annotations
from typing import *

from ..type.item import *
from ..graphics import *

class Items:
    copper = Item('copper', Color.valueOf('d99d73'))
    copper.hardness = 1
    copper.cost = 0.5
    copper.alwaysUnlocked = True

    lead = Item('lead', Color.valueOf('8c7fa9'))
    lead.hardness = 1
    lead.cost = 0.7

    metaglass = Item('metaglass', Color.valueOf('ebeef5'))
    metaglass.cost = 1.5

    graphite = Item('graphite', Color.valueOf('b2c6d2'))
    graphite.cost = 1.0

    sand = Item('sand', Color.valueOf('f7cba4'))
    sand.lowPriority = True
    sand.buildable = False
    sand.alwaysUnlocked = True

    coal = Item('coal', Color.valueOf('272727'))
    coal.explosiveness = 0.2
    coal.flammability = 1.0
    coal.hardness = 2
    coal.buildable = False

    titanium = Item('titanium', Color.valueOf('8da1e3'))
    titanium.hardness = 3
    titanium.cost = 1.0

    thorium = Item('thorium', Color.valueOf('f9a3c7'))
    thorium.explosiveness = 0.2
    thorium.hardness = 4
    thorium.radioactivity = 1.0
    thorium.cost = 1.1
    thorium.healthScaling = 0.2

    scrap = Item('scrap', Color.valueOf('777777'))

    silicon = Item('silicon', Color.valueOf('53565c'))
    silicon.cost = 0.8

    plastanium = Item('plastanium', Color.valueOf('cbd97f'))
    plastanium.flammability = 0.1
    plastanium.explosiveness = 0.2
    plastanium.cost = 1.3
    plastanium.healthScaling = 0.1

    phaseFabric = Item('phase-fabric', Color.valueOf('f4ba6e'))
    phaseFabric.cost = 1.3
    phaseFabric.radioactivity = 0.6
    phaseFabric.healthScaling = 0.25

    surgeAlloy = Item('surge-alloy', Color.valueOf('f3e979'))
    surgeAlloy.cost = 1.2
    surgeAlloy.charge = 0.75
    surgeAlloy.healthScaling = 0.25

    sporePod = Item('spore-pod', Color.valueOf('7457ce'))
    sporePod.flammability = 1.15
    sporePod.buildable = False

    blastCompound = Item('blast-compound', Color.valueOf('ff795e'))
    blastCompound.flammability = 0.4
    blastCompound.explosiveness = 1.2
    blastCompound.buildable = False

    pyratite = Item('pyratite', Color.valueOf('ffaa5f'))
    pyratite.flammability = 1.4
    pyratite.explosiveness = 0.4
    pyratite.buildable = False

    beryllium = Item('beryllium', Color.valueOf('3a8f64'))
    beryllium.hardness = 3
    beryllium.cost = 1.2
    beryllium.healthScaling = 0.6

    tungsten = Item('tungsten', Color.valueOf('768a9a'))
    tungsten.hardness = 5
    tungsten.cost = 1.5
    tungsten.healthScaling = 0.8

    oxide = Item('oxide', Color.valueOf('e4ffd6'))
    oxide.cost = 1.2
    oxide.healthScaling = 0.5

    carbide = Item('carbide', Color.valueOf('89769a'))
    carbide.cost = 1.4
    carbide.healthScaling = 1.1

    fissileMatter = Item('fissile-matter', Color.valueOf('5e988d'))
    fissileMatter.radioactivity = 1.5
    fissileMatter.hidden = True

    dormantCyst = Item('dormant-cyst', Color.valueOf('df824d'))
    dormantCyst.flammability = 0.1
    dormantCyst.hidden = True

    serpuloItems:List[Item] = [
        scrap, copper, lead, graphite, coal, titanium, thorium, silicon, plastanium,
        phaseFabric, surgeAlloy, sporePod, sand, blastCompound, pyratite, metaglass
    ]
    
    erekirItems:List[Item] = [
        graphite, thorium, silicon, phaseFabric, surgeAlloy, sand,
        beryllium, tungsten, oxide, carbide, fissileMatter, dormantCyst
    ]
    
    erekirOnlyItems:List[Item] = []
    for item in erekirItems:
        if item not in serpuloItems:
            erekirOnlyItems.append(item)