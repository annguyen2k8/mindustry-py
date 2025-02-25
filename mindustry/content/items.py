from __future__ import annotations
from typing import *

from mindustry.graphics import *
from mindustry.type import *

class Items:
    scrap:Item
    copper:Item
    lead:Item
    graphite:Item
    coal:Item
    titanium:Item
    thorium:Item
    silicon:Item
    plastanium:Item

    phaseFabric:Item
    surgeAlloy:Item
    sporePod:Item
    sand:Item
    blastCompound:Item
    pyratite:Item
    metaglass:Item

    beryllium:Item
    tungsten:Item
    oxide:Item
    carbide:Item
    fissileMatter:Item
    dormantCyst:Item
    
    @staticmethod
    def load():
        Items.copper = Item('copper', Color.valueOf('d99d73'))
        Items.copper.hardness = 1
        Items.copper.cost = 0.5
        Items.copper.alwaysUnlocked = True

        Items.lead = Item('lead', Color.valueOf('8c7fa9'))
        Items.lead.hardness = 1
        Items.lead.cost = 0.7

        Items.metaglass = Item('metaglass', Color.valueOf('ebeef5'))
        Items.metaglass.cost = 1.5

        Items.graphite = Item('graphite', Color.valueOf('b2c6d2'))
        Items.graphite.cost = 1.0

        Items.sand = Item('sand', Color.valueOf('f7cba4'))
        Items.sand.lowPriority = True
        Items.sand.buildable = False
        Items.sand.alwaysUnlocked = True
        Items.coal = Item('coal', Color.valueOf('272727'))
        Items.coal.explosiveness = 0.2
        Items.coal.flammability = 1.0
        Items.coal.hardness = 2
        Items.coal.buildable = False

        Items.titanium = Item('titanium', Color.valueOf('8da1e3'))
        Items.titanium.hardness = 3
        Items.titanium.cost = 1.0

        Items.thorium = Item('thorium', Color.valueOf('f9a3c7'))
        Items.thorium.explosiveness = 0.2
        Items.thorium.hardness = 4
        Items.thorium.radioactivity = 1.0
        Items.thorium.cost = 1.1
        Items.thorium.healthScaling = 0.2

        Items.scrap = Item('scrap', Color.valueOf('777777'))

        Items.silicon = Item('silicon', Color.valueOf('53565c'))
        Items.silicon.cost = 0.8

        Items.plastanium = Item('plastanium', Color.valueOf('cbd97f'))
        Items.plastanium.flammability = 0.1
        Items.plastanium.explosiveness = 0.2
        Items.plastanium.cost = 1.3
        Items.plastanium.healthScaling = 0.1

        Items.phaseFabric = Item('phase-fabric', Color.valueOf('f4ba6e'))
        Items.phaseFabric.cost = 1.3
        Items.phaseFabric.radioactivity = 0.6
        Items.phaseFabric.healthScaling = 0.25

        Items.surgeAlloy = Item('surge-alloy', Color.valueOf('f3e979'))
        Items.surgeAlloy.cost = 1.2
        Items.surgeAlloy.charge = 0.75
        Items.surgeAlloy.healthScaling = 0.25

        Items.sporePod = Item('spore-pod', Color.valueOf('7457ce'))
        Items.sporePod.flammability = 1.15
        Items.sporePod.buildable = False

        Items.blastCompound = Item('blast-compound', Color.valueOf('ff795e'))
        Items.blastCompound.flammability = 0.4
        Items.blastCompound.explosiveness = 1.2
        Items.blastCompound.buildable = False

        Items.pyratite = Item('pyratite', Color.valueOf('ffaa5f'))
        Items.pyratite.flammability = 1.4
        Items.pyratite.explosiveness = 0.4
        Items.pyratite.buildable = False

        Items.beryllium = Item('beryllium', Color.valueOf('3a8f64'))
        Items.beryllium.hardness = 3
        Items.beryllium.cost = 1.2
        Items.beryllium.healthScaling = 0.6

        Items.tungsten = Item('tungsten', Color.valueOf('768a9a'))
        Items.tungsten.hardness = 5
        Items.tungsten.cost = 1.5
        Items.tungsten.healthScaling = 0.8

        Items.oxide = Item('oxide', Color.valueOf('e4ffd6'))
        Items.oxide.cost = 1.2
        Items.oxide.healthScaling = 0.5

        Items.carbide = Item('carbide', Color.valueOf('89769a'))
        Items.carbide.cost = 1.4
        Items.carbide.healthScaling = 1.1

        Items.fissileMatter = Item('fissile-matter', Color.valueOf('5e988d'))
        Items.fissileMatter.radioactivity = 1.5
        Items.fissileMatter.hidden = True

        Items.dormantCyst = Item('dormant-cyst', Color.valueOf('df824d'))
        Items.dormantCyst.flammability = 0.1
        Items.dormantCyst.hidden = True
        
        Items.coal = Item('coal', Color.valueOf('272727'))
        Items.coal.explosiveness = 0.2
        Items.coal.flammability = 1.0
        Items.coal.hardness = 2
        Items.coal.buildable = False

        Items.titanium = Item('titanium', Color.valueOf('8da1e3'))
        Items.titanium.hardness = 3
        Items.titanium.cost = 1.0

        Items.thorium = Item('thorium', Color.valueOf('f9a3c7'))
        Items.thorium.explosiveness = 0.2
        Items.thorium.hardness = 4
        Items.thorium.radioactivity = 1.0
        Items.thorium.cost = 1.1
        Items.thorium.healthScaling = 0.2

        Items.scrap = Item('scrap', Color.valueOf('777777'))

        Items.silicon = Item('silicon', Color.valueOf('53565c'))
        Items.silicon.cost = 0.8

        Items.plastanium = Item('plastanium', Color.valueOf('cbd97f'))
        Items.plastanium.flammability = 0.1
        Items.plastanium.explosiveness = 0.2
        Items.plastanium.cost = 1.3
        Items.plastanium.healthScaling = 0.1

        Items.phaseFabric = Item('phase-fabric', Color.valueOf('f4ba6e'))
        Items.phaseFabric.cost = 1.3
        Items.phaseFabric.radioactivity = 0.6
        Items.phaseFabric.healthScaling = 0.25

        Items.surgeAlloy = Item('surge-alloy', Color.valueOf('f3e979'))
        Items.surgeAlloy.cost = 1.2
        Items.surgeAlloy.charge = 0.75
        Items.surgeAlloy.healthScaling = 0.25

        Items.sporePod = Item('spore-pod', Color.valueOf('7457ce'))
        Items.sporePod.flammability = 1.15
        Items.sporePod.buildable = False

        Items.blastCompound = Item('blast-compound', Color.valueOf('ff795e'))
        Items.blastCompound.flammability = 0.4
        Items.blastCompound.explosiveness = 1.2
        Items.blastCompound.buildable = False

        Items.pyratite = Item('pyratite', Color.valueOf('ffaa5f'))
        Items.pyratite.flammability = 1.4
        Items.pyratite.explosiveness = 0.4
        Items.pyratite.buildable = False

        Items.beryllium = Item('beryllium', Color.valueOf('3a8f64'))
        Items.beryllium.hardness = 3
        Items.beryllium.cost = 1.2
        Items.beryllium.healthScaling = 0.6

        Items.tungsten = Item('tungsten', Color.valueOf('768a9a'))
        Items.tungsten.hardness = 5
        Items.tungsten.cost = 1.5
        Items.tungsten.healthScaling = 0.8

        Items.oxide = Item('oxide', Color.valueOf('e4ffd6'))
        Items.oxide.cost = 1.2
        Items.oxide.healthScaling = 0.5

        Items.carbide = Item('carbide', Color.valueOf('89769a'))
        Items.carbide.cost = 1.4
        Items.carbide.healthScaling = 1.1

        Items.fissileMatter = Item('fissile-matter', Color.valueOf('5e988d'))
        Items.fissileMatter.radioactivity = 1.5
        Items.fissileMatter.hidden = True

        Items.dormantCyst = Item('dormant-cyst', Color.valueOf('df824d'))
        Items.dormantCyst.flammability = 0.1
        Items.dormantCyst.hidden = True

        serpuloItems:List[Item] = [
            Items.scrap, Items.copper, Items.lead, Items.graphite, Items.coal, Items.titanium, Items.thorium, Items.silicon, Items.plastanium,
            Items.phaseFabric, Items.surgeAlloy, Items.sporePod, Items.sand, Items.blastCompound, Items.pyratite, Items.metaglass
        ]
        
        erekirItems:List[Item] = [
            Items.graphite, Items.thorium, Items.silicon, Items.phaseFabric, Items.surgeAlloy, Items.sand,
            Items.beryllium, Items.tungsten, Items.oxide, Items.carbide, Items.fissileMatter, Items.dormantCyst
        ]
        
        erekirOnlyItems:List[Item] = []
        for item in erekirItems:
            if item not in serpuloItems:
                erekirOnlyItems.append(item)