from mindustry.world.consumer import *
from mindustry.world.blocks import *
from mindustry.world.meta import *
from mindustry.graphics import *
from mindustry.type import *
from mindustry.vars import *

from mindustry.type.liquid_stack import LiquidStack
from mindustry.type.item_stack import ItemStack


# from mindustry.world.block import Block

class Blocks:
    air: Block = None
    spawn: Block = None
    removeWall: Block = None
    removeOre: Block = None
    cliff: Block = None
    deepwater: Block = None
    water: Block = None
    taintedWater: Block = None
    deepTaintedWater: Block = None
    tar: Block = None
    slag: Block = None
    cryofluid: Block = None
    stone: Block = None
    craters: Block = None
    charr: Block = None
    sand: Block = None
    darksand: Block = None
    dirt: Block = None
    mud: Block = None
    ice: Block = None
    snow: Block = None
    darksandTaintedWater: Block = None
    space: Block = None
    empty: Block = None
    dacite: Block = None
    rhyolite: Block = None
    rhyoliteCrater: Block = None
    roughRhyolite: Block = None
    regolith: Block = None
    yellowStone: Block = None
    redIce: Block = None
    redStone: Block = None
    denseRedStone: Block = None
    arkyciteFloor: Block = None
    arkyicStone: Block = None
    redmat: Block = None
    bluemat: Block = None
    stoneWall: Block = None
    dirtWall: Block = None
    sporeWall: Block = None
    iceWall: Block = None
    daciteWall: Block = None
    sporePine: Block = None
    snowPine: Block = None
    pine: Block = None
    shrubs: Block = None
    whiteTree: Block = None
    whiteTreeDead: Block = None
    sporeCluster: Block = None
    redweed: Block = None
    purbush: Block = None
    yellowCoral: Block = None
    rhyoliteVent: Block = None
    carbonVent: Block = None
    arkyicVent: Block = None
    yellowStoneVent: Block = None
    redStoneVent: Block = None
    crystallineVent: Block = None
    regolithWall: Block = None
    yellowStoneWall: Block = None
    rhyoliteWall: Block = None
    carbonWall: Block = None
    redIceWall: Block = None
    ferricStoneWall: Block = None
    beryllicStoneWall: Block = None
    arkyicWall: Block = None
    crystallineStoneWall: Block = None
    redStoneWall: Block = None
    redDiamondWall: Block = None
    ferricStone: Block = None
    ferricCraters: Block = None
    carbonStone: Block = None
    beryllicStone: Block = None
    crystallineStone: Block = None
    crystalFloor: Block = None
    yellowStonePlates: Block = None
    iceSnow: Block = None
    sandWater: Block = None
    darksandWater: Block = None
    duneWall: Block = None
    sandWall: Block = None
    moss: Block = None
    sporeMoss: Block = None
    shale: Block = None
    shaleWall: Block = None
    grass: Block = None
    salt: Block = None
    coreZone: Block = None
    shaleBoulder: Block = None
    sandBoulder: Block = None
    daciteBoulder: Block = None
    boulder: Block = None
    snowBoulder: Block = None
    basaltBoulder: Block = None
    carbonBoulder: Block = None
    ferricBoulder: Block = None
    beryllicBoulder: Block = None
    yellowStoneBoulder: Block = None
    arkyicBoulder: Block = None
    crystalCluster: Block = None
    vibrantCrystalCluster: Block = None
    crystalBlocks: Block = None
    crystalOrbs: Block = None
    crystallineBoulder: Block = None
    redIceBoulder: Block = None
    rhyoliteBoulder: Block = None
    redStoneBoulder: Block = None
    metalFloor: Block = None
    metalFloorDamaged: Block = None
    metalFloor2: Block = None
    metalFloor3: Block = None
    metalFloor4: Block = None
    metalFloor5: Block = None
    basalt: Block = None
    magmarock: Block = None
    hotrock: Block = None
    snowWall: Block = None
    saltWall: Block = None
    darkPanel1: Block = None
    darkPanel2: Block = None
    darkPanel3: Block = None
    darkPanel4: Block = None
    darkPanel5: Block = None
    darkPanel6: Block = None
    darkMetal: Block = None
    pebbles: Block = None
    tendrils: Block = None
    oreCopper: Block = None
    oreLead: Block = None
    oreScrap: Block = None
    oreCoal: Block = None
    oreTitanium: Block = None
    oreThorium: Block = None
    oreBeryllium: Block = None
    oreTungsten: Block = None
    oreCrystalThorium: Block = None
    wallOreThorium: Block = None
    wallOreBeryllium: Block = None
    graphiticWall: Block = None
    wallOreTungsten: Block = None
    siliconSmelter: Block = None
    siliconCrucible: Block = None
    kiln: Block = None
    graphitePress: Block = None
    plastaniumCompressor: Block = None
    multiPress: Block = None
    phaseWeaver: Block = None
    surgeSmelter: Block = None
    pyratiteMixer: Block = None
    blastMixer: Block = None
    cryofluidMixer: Block = None
    melter: Block = None
    separator: Block = None
    disassembler: Block = None
    sporePress: Block = None
    pulverizer: Block = None
    incinerator: Block = None
    coalCentrifuge: Block = None
    siliconArcFurnace: Block = None
    electrolyzer: Block = None
    oxidationChamber: Block = None
    atmosphericConcentrator: Block = None
    electricHeater: Block = None
    slagHeater: Block = None
    phaseHeater: Block = None
    heatRedirector: Block = None
    smallHeatRedirector: Block = None
    heatRouter: Block = None
    slagIncinerator: Block = None
    carbideCrucible: Block = None
    slagCentrifuge: Block = None
    surgeCrucible: Block = None
    cyanogenSynthesizer: Block = None
    phaseSynthesizer: Block = None
    heatReactor: Block = None
    powerSource: Block = None
    powerVoid: Block = None
    itemSource: Block = None
    itemVoid: Block = None
    liquidSource: Block = None
    liquidVoid: Block = None
    payloadSource: Block = None
    payloadVoid: Block = None
    illuminator: Block = None
    heatSource: Block = None
    copperWall: Block = None
    copperWallLarge: Block = None
    titaniumWall: Block = None
    titaniumWallLarge: Block = None
    plastaniumWall: Block = None
    plastaniumWallLarge: Block = None
    thoriumWall: Block = None
    thoriumWallLarge: Block = None
    door: Block = None
    doorLarge: Block = None
    phaseWall: Block = None
    phaseWallLarge: Block = None
    surgeWall: Block = None
    surgeWallLarge: Block = None
    berylliumWall: Block = None
    berylliumWallLarge: Block = None
    tungstenWall: Block = None
    tungstenWallLarge: Block = None
    blastDoor: Block = None
    reinforcedSurgeWall: Block = None
    reinforcedSurgeWallLarge: Block = None
    carbideWall: Block = None
    carbideWallLarge: Block = None
    shieldedWall: Block = None
    mender: Block = None
    mendProjector: Block = None
    overdriveProjector: Block = None
    overdriveDome: Block = None
    forceProjector: Block = None
    shockMine: Block = None
    scrapWall: Block = None
    scrapWallLarge: Block = None
    scrapWallHuge: Block = None
    scrapWallGigantic: Block = None
    thruster: Block = None
    radar: Block = None
    buildTower: Block = None
    regenProjector: Block = None
    barrierProjector: Block = None
    shockwaveTower: Block = None
    shieldProjector: Block = None
    largeShieldProjector: Block = None
    shieldBreaker: Block = None
    conveyor: Block = None
    titaniumConveyor: Block = None
    plastaniumConveyor: Block = None
    armoredConveyor: Block = None
    distributor: Block = None
    junction: Block = None
    itemBridge: Block = None
    phaseConveyor: Block = None
    sorter: Block = None
    invertedSorter: Block = None
    router: Block = None
    overflowGate: Block = None
    underflowGate: Block = None
    massDriver: Block = None
    duct: Block = None
    armoredDuct: Block = None
    ductRouter: Block = None
    overflowDuct: Block = None
    underflowDuct: Block = None
    ductBridge: Block = None
    ductUnloader: Block = None
    surgeConveyor: Block = None
    surgeRouter: Block = None
    unitCargoLoader: Block = None
    unitCargoUnloadPoint: Block = None
    mechanicalPump: Block = None
    rotaryPump: Block = None
    impulsePump: Block = None
    conduit: Block = None
    pulseConduit: Block = None
    platedConduit: Block = None
    liquidRouter: Block = None
    liquidContainer: Block = None
    liquidTank: Block = None
    liquidJunction: Block = None
    bridgeConduit: Block = None
    phaseConduit: Block = None
    reinforcedPump: Block = None
    reinforcedConduit: Block = None
    reinforcedLiquidJunction: Block = None
    reinforcedBridgeConduit: Block = None
    reinforcedLiquidRouter: Block = None
    reinforcedLiquidContainer: Block = None
    reinforcedLiquidTank: Block = None
    combustionGenerator: Block = None
    thermalGenerator: Block = None
    steamGenerator: Block = None
    differentialGenerator: Block = None
    rtgGenerator: Block = None
    solarPanel: Block = None
    largeSolarPanel: Block = None
    thoriumReactor: Block = None
    impactReactor: Block = None
    battery: Block = None
    batteryLarge: Block = None
    powerNode: Block = None
    powerNodeLarge: Block = None
    surgeTower: Block = None
    diode: Block = None
    turbineCondenser: Block = None
    ventCondenser: Block = None
    chemicalCombustionChamber: Block = None
    pyrolysisGenerator: Block = None
    fluxReactor: Block = None
    neoplasiaReactor: Block = None
    beamNode: Block = None
    beamTower: Block = None
    beamLink: Block = None
    mechanicalDrill: Block = None
    pneumaticDrill: Block = None
    laserDrill: Block = None
    blastDrill: Block = None
    waterExtractor: Block = None
    oilExtractor: Block = None
    cultivator: Block = None
    cliffCrusher: Block = None
    largeCliffCrusher: Block = None
    plasmaBore: Block = None
    largePlasmaBore: Block = None
    impactDrill: Block = None
    eruptionDrill: Block = None
    coreShard: Block = None
    coreFoundation: Block = None
    coreNucleus: Block = None
    vault: Block = None
    container: Block = None
    unloader: Block = None
    coreBastion: Block = None
    coreCitadel: Block = None
    coreAcropolis: Block = None
    reinforcedContainer: Block = None
    reinforcedVault: Block = None
    duo: Block = None
    scatter: Block = None
    scorch: Block = None
    hail: Block = None
    arc: Block = None
    wave: Block = None
    lancer: Block = None
    swarmer: Block = None
    salvo: Block = None
    fuse: Block = None
    ripple: Block = None
    cyclone: Block = None
    foreshadow: Block = None
    spectre: Block = None
    meltdown: Block = None
    segment: Block = None
    parallax: Block = None
    tsunami: Block = None
    breach: Block = None
    diffuse: Block = None
    sublimate: Block = None
    titan: Block = None
    disperse: Block = None
    afflict: Block = None
    lustre: Block = None
    scathe: Block = None
    smite: Block = None
    malign: Block = None
    groundFactory: Block = None
    airFactory: Block = None
    navalFactory: Block = None
    additiveReconstructor: Block = None
    multiplicativeReconstructor: Block = None
    exponentialReconstructor: Block = None
    tetrativeReconstructor: Block = None
    repairPoint: Block = None
    repairTurret: Block = None
    tankFabricator: Block = None
    shipFabricator: Block = None
    mechFabricator: Block = None
    tankRefabricator: Block = None
    shipRefabricator: Block = None
    mechRefabricator: Block = None
    primeRefabricator: Block = None
    tankAssembler: Block = None
    shipAssembler: Block = None
    mechAssembler: Block = None
    basicAssemblerModule: Block = None
    unitRepairTower: Block = None
    payloadConveyor: Block = None
    payloadRouter: Block = None
    reinforcedPayloadConveyor: Block = None
    reinforcedPayloadRouter: Block = None
    payloadMassDriver: Block = None
    largePayloadMassDriver: Block = None
    smallDeconstructor: Block = None
    deconstructor: Block = None
    constructor: Block = None
    largeConstructor: Block = None
    payloadLoader: Block = None
    payloadUnloader: Block = None
    message: Block = None
    switchBlock: Block = None
    microProcessor: Block = None
    logicProcessor: Block = None
    hyperProcessor: Block = None
    largeLogicDisplay: Block = None
    logicDisplay: Block = None
    memoryCell: Block = None
    memoryBank: Block = None
    canvas: Block = None
    reinforcedMessage: Block = None
    worldProcessor: Block = None
    worldCell: Block = None
    worldMessage: Block = None
    worldSwitch: Block = None
    launchPad: Block = None
    interplanetaryAccelerator: Block = None
    
    @staticmethod
    def load():
        
        # region environment
        Blocks.air
        Blocks.air = AirBlock('air')
        Blocks.spawn = SpawnBlock('spawn')
        Blocks.removeWall = RemoveWall('remove-wall')
        Blocks.removeOre = RemoveOre('remove-ore')
        Blocks.cliff = Cliff('cliff')
        Blocks.cliff.inEdition = False
        Blocks.cliff.saveData = True
        
        # registers build blocks
        # no reference is needed here since they can be looked up by name later
        for i in range(1, Vars.maxBlockSize + 1):
            ConstructBlock(i)
        
        Blocks.deepwater = Floor("deep-water")
        Blocks.deepwater.speedMultiplier = 0.2
        Blocks.deepwater.variants = 0
        Blocks.deepwater.liquidDrop = Liquids.water
        Blocks.deepwater.liquidMultiplier = 1.5
        Blocks.deepwater.isLiquid = True
        Blocks.deepwater.status = StatusEffects.wet
        Blocks.deepwater.statusDuration = 120.0
        Blocks.deepwater.drownTime = 200.0
        Blocks.deepwater.cacheLayer = CacheLayer.water
        Blocks.deepwater.albedo = 0.9
        Blocks.deepwater.supportsOverlay = True
        
        Blocks.water = Floor("shallow-water")
        Blocks.water.speedMultiplier = 0.5
        Blocks.water.variants = 0
        Blocks.water.status = StatusEffects.wet
        Blocks.water.statusDuration = 90.0
        Blocks.water.liquidDrop = Liquids.water
        Blocks.water.isLiquid = True
        Blocks.water.cacheLayer = CacheLayer.water
        Blocks.water.albedo = 0.9
        Blocks.water.supportsOverlay = True
        
        Blocks.taintedWater = Floor("tainted-water")
        Blocks.taintedWater.speedMultiplier = 0.5
        Blocks.taintedWater.variants = 0
        Blocks.taintedWater.status = StatusEffects.wet
        Blocks.taintedWater.statusDuration = 90.0
        Blocks.taintedWater.liquidDrop = Liquids.water
        Blocks.taintedWater.isLiquid = True
        Blocks.taintedWater.cacheLayer = CacheLayer.water
        Blocks.taintedWater.albedo = 0.9
        Blocks.taintedWater.attributes.set(Attribute.spores, 0.15)
        Blocks.taintedWater.supportsOverlay = True
        
        Blocks.deepTaintedWater = ShallowLiquid("deep-tainted-water")
        Blocks.deepTaintedWater.speedMultiplier = 0.18
        Blocks.deepTaintedWater.variants = 0
        Blocks.deepTaintedWater.status = StatusEffects.wet
        Blocks.deepTaintedWater.statusDuration = 140.0
        Blocks.deepTaintedWater.drownTime = 200.0
        Blocks.deepTaintedWater.liquidDrop = Liquids.water
        Blocks.deepTaintedWater.isLiquid = True
        Blocks.deepTaintedWater.cacheLayer = CacheLayer.water
        Blocks.deepTaintedWater.albedo = 0.9
        Blocks.deepTaintedWater.attributes.set(Attribute.spores, 0.15)
        Blocks.deepTaintedWater.supportsOverlay = True
        
        Blocks.darksandTaintedWater = ShallowLiquid("darksand-tainted-water")
        Blocks.darksandTaintedWater.speedMultiplier = 0.75
        Blocks.darksandTaintedWater.statusDuration = 60.0
        Blocks.darksandTaintedWater.albedo = 0.9
        Blocks.darksandTaintedWater.attributes.set(Attribute.spores, 0.1)
        Blocks.darksandTaintedWater.supportsOverlay = True
        
        Blocks.sandWater = ShallowLiquid("sand-water")
        Blocks.sandWater.speedMultiplier = 0.8
        Blocks.sandWater.statusDuration = 50.0
        Blocks.sandWater.albedo = 0.9
        Blocks.sandWater.supportsOverlay = True
        
        Blocks.darksandWater = ShallowLiquid("darksand-water")
        Blocks.darksandWater.speedMultiplier = 0.8
        Blocks.darksandWater.statusDuration = 50.0
        Blocks.darksandWater.albedo = 0.9
        Blocks.darksandWater.supportsOverlay = True

        Blocks.tar = Floor("tar")
        Blocks.tar.drownTime = 230.0
        Blocks.tar.status = StatusEffects.tarred
        Blocks.tar.statusDuration = 240.0
        Blocks.tar.speedMultiplier = 0.19
        Blocks.tar.variants = 0
        Blocks.tar.liquidDrop = Liquids.oil
        Blocks.tar.isLiquid = True
        Blocks.tar.cacheLayer = CacheLayer.tar

        Blocks.cryofluid = Floor("pooled-cryofluid")
        Blocks.cryofluid.drownTime = 150.0
        Blocks.cryofluid.status = StatusEffects.freezing
        Blocks.cryofluid.statusDuration = 240.0
        Blocks.cryofluid.speedMultiplier = 0.5
        Blocks.cryofluid.variants = 0
        Blocks.cryofluid.liquidDrop = Liquids.cryofluid
        Blocks.cryofluid.liquidMultiplier = 0.5
        Blocks.cryofluid.isLiquid = True
        Blocks.cryofluid.cacheLayer = CacheLayer.cryofluid
        Blocks.cryofluid.emitLight = True
        Blocks.cryofluid.lightRadius = 25.0
        Blocks.cryofluid.lightColor = Colors.cyan.cpy().set_a(0.19)
        
        Blocks.slag = Floor("molten-slag")
        Blocks.slag.drownTime = 230.0
        Blocks.slag.status = StatusEffects.melting
        Blocks.slag.statusDuration = 240.0
        Blocks.slag.speedMultiplier = 0.19
        Blocks.slag.variants = 0
        Blocks.slag.liquidDrop = Liquids.slag
        Blocks.slag.isLiquid = True
        Blocks.slag.cacheLayer = CacheLayer.slag
        Blocks.slag.attributes.set(Attribute.heat, 0.85)
        Blocks.slag.emitLight = True
        Blocks.slag.lightRadius = 40.0
        Blocks.slag.lightColor = Colors.orange.cpy().set_a(0.38)

        Blocks.space = Floor("space")
        Blocks.space.cacheLayer = CacheLayer.space
        Blocks.space.placeableOn = False
        Blocks.space.solid = True
        Blocks.space.variants = 0
        Blocks.space.canShadow = False
        
        Blocks.empty = EmptyFloor("empty")

        Blocks.stone = Floor("stone")

        Blocks.craters = Floor("crater-stone")
        Blocks.craters.variants = 3
        Blocks.craters.blendGroup = Blocks.stone

        Blocks.charr = Floor("char")
        Blocks.charr.blendGroup = Blocks.stone

        Blocks.basalt = Floor("basalt")
        Blocks.basalt.attributes.set(Attribute.water, -0.25)

        Blocks.hotrock = Floor("hotrock")
        Blocks.hotrock.attributes.set(Attribute.heat, 0.5)
        Blocks.hotrock.attributes.set(Attribute.water, -0.5)
        Blocks.hotrock.blendGroup = Blocks.basalt
        Blocks.hotrock.emitLight = True
        Blocks.hotrock.lightRadius = 30.0
        Blocks.hotrock.lightColor = Colors.orange.cpy().set_a(0.15)

        Blocks.magmarock = Floor("magmarock")
        Blocks.magmarock.attributes.set(Attribute.heat, 0.75)
        Blocks.magmarock.attributes.set(Attribute.water, -0.75)
        Blocks.magmarock.blendGroup = Blocks.basalt
        Blocks.magmarock.emitLight = True
        Blocks.magmarock.lightRadius = 50.0
        Blocks.magmarock.lightColor = Colors.orange.cpy().set_a(0.3)

        Blocks.sand = Floor("sand-floor")
        Blocks.sand.itemDrop = Items.sand
        Blocks.sand.playerUnmineable = True
        Blocks.sand.attributes.set(Attribute.oil, 0.7)

        Blocks.darksand = Floor("darksand")
        Blocks.darksand.itemDrop = Items.sand
        Blocks.darksand.playerUnmineable = True
        Blocks.darksand.attributes.set(Attribute.oil, 1.5)

        Blocks.dirt = Floor("dirt")

        Blocks.mud = Floor("mud")
        Blocks.mud.speedMultiplier = 0.6
        Blocks.mud.variants = 3
        Blocks.mud.status = StatusEffects.muddy
        Blocks.mud.statusDuration = 30.0
        Blocks.mud.attributes.set(Attribute.water, 1.0)
        Blocks.mud.cacheLayer = CacheLayer.mud
        # Blocks.mud.walkSound = Sounds.mud
        # Blocks.mud.walkSoundVolume = 0.08
        # Blocks.mud.walkSoundPitchMin = 0.4
        # Blocks.mud.walkSoundPitchMax = 0.5

        Blocks.darksandTaintedWater.set_base(Blocks.taintedWater, Blocks.darksand)
        Blocks.sandWater.set_base(Blocks.water, Blocks.sand)
        Blocks.darksandWater.set_base(Blocks.water, Blocks.darksand)

        Blocks.dacite = Floor("dacite")

        Blocks.rhyolite = Floor("rhyolite")
        Blocks.rhyolite.attributes.set(Attribute.water, -1.0)

        Blocks.rhyoliteCrater = Floor("rhyolite-crater")
        Blocks.rhyoliteCrater.attributes.set(Attribute.water, -1.0)
        Blocks.rhyoliteCrater.blendGroup = Blocks.rhyolite

        Blocks.roughRhyolite = Floor("rough-rhyolite")
        Blocks.roughRhyolite.attributes.set(Attribute.water, -1.0)
        Blocks.roughRhyolite.variants = 3

        Blocks.regolith = Floor("regolith")
        Blocks.regolith.attributes.set(Attribute.water, -1.0)

        Blocks.yellowStone = Floor("yellow-stone")
        Blocks.yellowStone.attributes.set(Attribute.water, -1.0)

        Blocks.carbonStone = Floor("carbon-stone")
        Blocks.carbonStone.attributes.set(Attribute.water, -1.0)
        Blocks.carbonStone.variants = 4

        Blocks.ferricStone = Floor("ferric-stone")
        Blocks.ferricStone.attributes.set(Attribute.water, -1.0)

        Blocks.ferricCraters = Floor("ferric-craters")
        Blocks.ferricCraters.variants = 3
        Blocks.ferricCraters.attributes.set(Attribute.water, -1.0)
        Blocks.ferricCraters.blendGroup = Blocks.ferricStone

        Blocks.beryllicStone = Floor("beryllic-stone")
        Blocks.beryllicStone.variants = 4

        Blocks.crystallineStone = Floor("crystalline-stone")
        Blocks.crystallineStone.variants = 5

        Blocks.crystalFloor = Floor("crystal-floor")
        Blocks.crystalFloor.variants = 4

        Blocks.yellowStonePlates = Floor("yellow-stone-plates")
        Blocks.yellowStonePlates.variants = 3

        Blocks.redStone = Floor("red-stone")
        Blocks.redStone.attributes.set(Attribute.water, -1.0)
        Blocks.redStone.variants = 4

        Blocks.denseRedStone = Floor("dense-red-stone")
        Blocks.denseRedStone.attributes.set(Attribute.water, -1.0)
        Blocks.denseRedStone.variants = 4

        Blocks.redIce = Floor("red-ice")
        Blocks.redIce.dragMultiplier = 0.4
        Blocks.redIce.speedMultiplier = 0.9
        Blocks.redIce.attributes.set(Attribute.water, 0.4)

        Blocks.arkyciteFloor = Floor("arkycite-floor")
        Blocks.arkyciteFloor.speedMultiplier = 0.3
        Blocks.arkyciteFloor.variants = 0
        Blocks.arkyciteFloor.liquidDrop = Liquids.arkycite
        Blocks.arkyciteFloor.isLiquid = True
        # TODO no status for now
        # status = StatusEffects.slow;
        # statusDuration = 120f;
        Blocks.arkyciteFloor.drownTime = 200.0
        Blocks.arkyciteFloor.cacheLayer = CacheLayer.arkycite
        Blocks.arkyciteFloor.albedo = 0.9

        Blocks.arkyicStone = Floor("arkyic-stone")
        Blocks.arkyicStone.variants = 3
        
        Blocks.rhyoliteVent = SteamVent("rhyolite-vent")
        Blocks.rhyoliteVent.parent = Blocks.rhyolite
        Blocks.rhyoliteVent.blendGroup = Blocks.rhyolite
        Blocks.rhyoliteVent.attributes.set(Attribute.steam, 1.0)
        
        Blocks.carbonVent = SteamVent("carbon-vent")
        Blocks.carbonVent.parent = Blocks.carbonStone
        Blocks.carbonVent.blendGroup = Blocks.carbonStone
        Blocks.carbonVent.attributes.set(Attribute.steam, 1.0)

        Blocks.arkyicVent = SteamVent("arkyic-vent")
        Blocks.arkyicVent.parent = Blocks.arkyicStone
        Blocks.arkyicVent.blendGroup = Blocks.arkyicStone
        Blocks.arkyicVent.attributes.set(Attribute.steam, 1.0)

        Blocks.yellowStoneVent = SteamVent("yellow-stone-vent")
        Blocks.yellowStoneVent.parent = Blocks.yellowStone
        Blocks.yellowStoneVent.blendGroup = Blocks.yellowStone
        Blocks.yellowStoneVent.attributes.set(Attribute.steam, 1.0)

        Blocks.redStoneVent = SteamVent("red-stone-vent")
        Blocks.redStoneVent.parent = Blocks.denseRedStone
        Blocks.redStoneVent.blendGroup = Blocks.denseRedStone
        Blocks.redStoneVent.attributes.set(Attribute.steam, 1.0)

        Blocks.crystallineVent = SteamVent("crystalline-vent")
        Blocks.crystallineVent.parent = Blocks.crystallineStone
        Blocks.crystallineVent.blendGroup = Blocks.crystallineStone
        Blocks.crystallineVent.attributes.set(Attribute.steam, 1.0)

        Blocks.redmat = Floor("redmat")
        Blocks.bluemat = Floor("bluemat")

        Blocks.grass = Floor("grass")
        # TODO grass needs a bush? classic had grass bushes.
        Blocks.grass.attributes.set(Attribute.water, 0.1)
        
        Blocks.salt = Floor("salt")
        Blocks.salt.variants = 0
        Blocks.salt.attributes.set(Attribute.water, -0.3)
        Blocks.salt.attributes.set(Attribute.oil, 0.3)

        Blocks.snow = Floor("snow")
        Blocks.snow.attributes.set(Attribute.water, 0.2)
        Blocks.snow.albedo = 0.7

        Blocks.ice = Floor("ice")
        Blocks.ice.dragMultiplier = 0.35
        Blocks.ice.speedMultiplier = 0.9
        Blocks.ice.attributes.set(Attribute.water, 0.4)
        Blocks.ice.albedo = 0.65

        Blocks.iceSnow = Floor("ice-snow")
        Blocks.iceSnow.dragMultiplier = 0.6
        Blocks.iceSnow.variants = 3
        Blocks.iceSnow.attributes.set(Attribute.water, 0.3)
        Blocks.iceSnow.albedo = 0.6

        Blocks.shale = Floor("shale")
        Blocks.shale.variants = 3
        Blocks.shale.attributes.set(Attribute.oil, 1.6)

        Blocks.moss = Floor("moss")
        Blocks.moss.variants = 3
        Blocks.moss.attributes.set(Attribute.spores, 0.15)

        Blocks.coreZone = Floor("core-zone")
        Blocks.coreZone.variants = 0
        Blocks.coreZone.allowCorePlacement = True

        Blocks.sporeMoss = Floor("spore-moss")
        Blocks.sporeMoss.variants = 3
        Blocks.sporeMoss.attributes.set(Attribute.spores, 0.3)
        
        Blocks.stoneWall = StaticWall("stone-wall")
        Blocks.stoneWall.attributes.set(Attribute.sand, 1.0)

        Blocks.sporeWall = StaticWall("spore-wall")
        Blocks.taintedWater.asFloor().wall = Blocks.deepTaintedWater.asFloor().wall = Blocks.sporeMoss.asFloor().wall = Blocks.sporeWall

        Blocks.dirtWall = StaticWall("dirt-wall")

        Blocks.daciteWall = StaticWall("dacite-wall")

        Blocks.iceWall = StaticWall("ice-wall")
        Blocks.iceSnow.asFloor().wall = Blocks.iceWall
        Blocks.iceWall.albedo = 0.6

        Blocks.snowWall = StaticWall("snow-wall")

        Blocks.duneWall = StaticWall("dune-wall")
        Blocks.hotrock.asFloor().wall = Blocks.magmarock.asFloor().wall = Blocks.basalt.asFloor().wall = Blocks.darksandWater.asFloor().wall = Blocks.darksandTaintedWater.asFloor().wall = Blocks.duneWall
        Blocks.duneWall.attributes.set(Attribute.sand, 2.0)

        Blocks.regolithWall = StaticWall("regolith-wall")
        Blocks.regolith.asFloor().wall = Blocks.regolithWall
        Blocks.regolithWall.attributes.set(Attribute.sand, 1.0)

        Blocks.yellowStoneWall = StaticWall("yellow-stone-wall")
        Blocks.yellowStone.asFloor().wall = Blocks.slag.asFloor().wall = Blocks.yellowStonePlates.asFloor().wall = Blocks.yellowStoneWall
        Blocks.yellowStoneWall.attributes.set(Attribute.sand, 1.5)

        Blocks.rhyoliteWall = StaticWall("rhyolite-wall")
        Blocks.rhyolite.asFloor().wall = Blocks.rhyoliteCrater.asFloor().wall = Blocks.roughRhyolite.asFloor().wall = Blocks.rhyoliteWall
        Blocks.rhyoliteWall.attributes.set(Attribute.sand, 1.0)

        Blocks.carbonWall = StaticWall("carbon-wall")
        Blocks.carbonStone.asFloor().wall = Blocks.carbonWall
        Blocks.carbonWall.attributes.set(Attribute.sand, 0.7)

        Blocks.ferricStoneWall = StaticWall("ferric-stone-wall")
        Blocks.ferricStone.asFloor().wall = Blocks.ferricStoneWall
        Blocks.ferricStoneWall.attributes.set(Attribute.sand, 0.5)

        Blocks.beryllicStoneWall = StaticWall("beryllic-stone-wall")
        Blocks.beryllicStone.asFloor().wall = Blocks.beryllicStoneWall
        Blocks.beryllicStoneWall.attributes.set(Attribute.sand, 1.2)

        Blocks.arkyicWall = StaticWall("arkyic-wall")
        Blocks.arkyicWall.variants = 3
        Blocks.arkyciteFloor.asFloor().wall = Blocks.arkyicStone.asFloor().wall = Blocks.arkyicWall

        Blocks.crystallineStoneWall = StaticWall("crystalline-stone-wall")
        Blocks.crystallineStoneWall.variants = 4
        Blocks.crystallineStone.asFloor().wall = Blocks.crystalFloor.asFloor().wall = Blocks.crystallineStoneWall

        Blocks.redIceWall = StaticWall("red-ice-wall")
        Blocks.redIce.asFloor().wall = Blocks.redIceWall

        Blocks.redStoneWall = StaticWall("red-stone-wall")
        Blocks.redStone.asFloor().wall = Blocks.denseRedStone.asFloor().wall = Blocks.redStoneWall
        Blocks.redStoneWall.attributes.set(Attribute.sand, 1.5)

        Blocks.redDiamondWall = StaticTree("red-diamond-wall")
        Blocks.redDiamondWall.variants = 3

        Blocks.sandWall = StaticWall("sand-wall")
        Blocks.sandWater.asFloor().wall = Blocks.water.asFloor().wall = Blocks.deepwater.asFloor().wall = Blocks.sand.asFloor().wall = Blocks.sandWall
        Blocks.sandWall.attributes.set(Attribute.sand, 2.0)

        Blocks.saltWall = StaticWall("salt-wall")

        Blocks.shrubs = StaticWall("shrubs")

        Blocks.shaleWall = StaticWall("shale-wall")
        
        Blocks.sporePine = StaticTree("spore-pine")
        Blocks.moss.asFloor().wall = Blocks.sporePine

        Blocks.snowPine = StaticTree("snow-pine")

        Blocks.pine = StaticTree("pine")

        Blocks.whiteTreeDead = TreeBlock("white-tree-dead")

        Blocks.whiteTree = TreeBlock("white-tree")

        Blocks.sporeCluster = Prop("spore-cluster")
        Blocks.sporeCluster.variants = 3

        Blocks.redweed = Seaweed("redweed")
        Blocks.redweed.variants = 3
        Blocks.redmat.asFloor().decoration = Blocks.redweed

        Blocks.purbush = SeaBush("pur-bush")
        Blocks.bluemat.asFloor().decoration = Blocks.purbush

        Blocks.yellowCoral = SeaBush("yellowcoral")
        Blocks.yellowCoral.lobesMin = 2
        Blocks.yellowCoral.lobesMax = 3
        Blocks.yellowCoral.magMax = 8.0
        Blocks.yellowCoral.magMin = 2.0
        Blocks.yellowCoral.origin = 0.3
        Blocks.yellowCoral.spread = 40.0
        Blocks.yellowCoral.sclMin = 60.0
        Blocks.yellowCoral.sclMax = 100.0

        Blocks.boulder = Prop("boulder")
        Blocks.boulder.variants = 2
        Blocks.stone.asFloor().decoration = Blocks.craters.asFloor().decoration = Blocks.charr.asFloor().decoration = Blocks.boulder

        Blocks.snowBoulder = Prop("snow-boulder")
        Blocks.snowBoulder.variants = 2
        Blocks.snow.asFloor().decoration = Blocks.ice.asFloor().decoration = Blocks.iceSnow.asFloor().decoration = Blocks.salt.asFloor().decoration = Blocks.snowBoulder

        Blocks.shaleBoulder = Prop("shale-boulder")
        Blocks.shaleBoulder.variants = 2
        Blocks.shale.asFloor().decoration = Blocks.shaleBoulder

        Blocks.sandBoulder = Prop("sand-boulder")
        Blocks.sandBoulder.variants = 2
        Blocks.sand.asFloor().decoration = Blocks.sandBoulder

        Blocks.daciteBoulder = Prop("dacite-boulder")
        Blocks.daciteBoulder.variants = 2
        Blocks.dacite.asFloor().decoration = Blocks.daciteBoulder

        Blocks.basaltBoulder = Prop("basalt-boulder")
        Blocks.basaltBoulder.variants = 2
        Blocks.basalt.asFloor().decoration = Blocks.hotrock.asFloor().decoration = Blocks.darksand.asFloor().decoration = Blocks.magmarock.asFloor().decoration = Blocks.basaltBoulder

        Blocks.carbonBoulder = Prop("carbon-boulder")
        Blocks.carbonBoulder.variants = 2
        Blocks.carbonStone.asFloor().decoration = Blocks.carbonBoulder

        Blocks.ferricBoulder = Prop("ferric-boulder")
        Blocks.ferricBoulder.variants = 2
        Blocks.ferricStone.asFloor().decoration = Blocks.ferricCraters.asFloor().decoration = Blocks.ferricBoulder

        Blocks.beryllicBoulder = Prop("beryllic-boulder")
        Blocks.beryllicBoulder.variants = 2
        Blocks.beryllicStone.asFloor().decoration = Blocks.beryllicBoulder

        Blocks.yellowStoneBoulder = Prop("yellow-stone-boulder")
        Blocks.yellowStoneBoulder.variants = 2
        Blocks.yellowStone.asFloor().decoration = Blocks.regolith.asFloor().decoration = Blocks.yellowStonePlates.asFloor().decoration = Blocks.yellowStoneBoulder

        Blocks.arkyicBoulder = Prop("arkyic-boulder")
        Blocks.arkyicBoulder.variants = 3
        Blocks.arkyicBoulder.customShadow = True
        Blocks.arkyicStone.asFloor().decoration = Blocks.arkyicBoulder
        
        Blocks.crystalCluster = TallBlock("crystal-cluster")
        Blocks.crystalCluster.variants = 3
        Blocks.crystalCluster.clipSize = 128.0

        Blocks.vibrantCrystalCluster = TallBlock("vibrant-crystal-cluster")
        Blocks.vibrantCrystalCluster.variants = 3
        Blocks.vibrantCrystalCluster.clipSize = 128.0

        Blocks.crystalBlocks = TallBlock("crystal-blocks")
        Blocks.crystalBlocks.variants = 3
        Blocks.crystalBlocks.clipSize = 128.0
        Blocks.crystalBlocks.shadowAlpha = 0.5
        Blocks.crystalBlocks.shadowOffset = -2.5

        Blocks.crystalOrbs = TallBlock("crystal-orbs")
        Blocks.crystalOrbs.variants = 3
        Blocks.crystalOrbs.clipSize = 128.0
        Blocks.crystalOrbs.shadowAlpha = 0.5
        Blocks.crystalOrbs.shadowOffset = -2.5

        Blocks.crystallineBoulder = Prop("crystalline-boulder")
        Blocks.crystallineBoulder.variants = 2
        Blocks.crystallineStone.asFloor().decoration = Blocks.crystallineBoulder

        Blocks.redIceBoulder = Prop("red-ice-boulder")
        Blocks.redIceBoulder.variants = 3
        Blocks.redIce.asFloor().decoration = Blocks.redIceBoulder

        Blocks.rhyoliteBoulder = Prop("rhyolite-boulder")
        Blocks.rhyoliteBoulder.variants = 3
        Blocks.rhyolite.asFloor().decoration = Blocks.roughRhyolite.asFloor().decoration = Blocks.rhyoliteBoulder

        Blocks.redStoneBoulder = Prop("red-stone-boulder")
        Blocks.redStoneBoulder.variants = 4
        Blocks.denseRedStone.asFloor().decoration = Blocks.redStone.asFloor().decoration = Blocks.redStoneBoulder

        Blocks.metalFloor = Floor("metal-floor", 0)
        Blocks.metalFloorDamaged = Floor("metal-floor-damaged", 3)

        Blocks.metalFloor2 = Floor("metal-floor-2", 0)
        Blocks.metalFloor3 = Floor("metal-floor-3", 0)
        Blocks.metalFloor4 = Floor("metal-floor-4", 0)
        Blocks.metalFloor5 = Floor("metal-floor-5", 0)

        Blocks.darkPanel1 = Floor("dark-panel-1", 0)
        Blocks.darkPanel2 = Floor("dark-panel-2", 0)
        Blocks.darkPanel3 = Floor("dark-panel-3", 0)
        Blocks.darkPanel4 = Floor("dark-panel-4", 0)
        Blocks.darkPanel5 = Floor("dark-panel-5", 0)
        Blocks.darkPanel6 = Floor("dark-panel-6", 0)

        Blocks.darkMetal = StaticWall("dark-metal")
        
        blocks = [
            Blocks.metalFloor, Blocks.metalFloorDamaged, Blocks.metalFloor2, Blocks.metalFloor3,
            Blocks.metalFloor4, Blocks.metalFloor5, Blocks.darkPanel1, Blocks.darkPanel2,
            Blocks.darkPanel3, Blocks.darkPanel4, Blocks.darkPanel5, Blocks.darkPanel6
        ]

        for b in blocks:
            b.wall = Blocks.darkMetal
        
        Blocks.pebbles = OverlayFloor('pebbles')
        Blocks.tendrils = OverlayFloor('tendrils')
        
        # region ore
        
        Blocks.oreCopper = OreBlock(Items.copper)
        Blocks.oreCopper.oreDefault = True
        Blocks.oreCopper.oreThreshold = 0.81
        Blocks.oreCopper.oreScale = 23.47619

        Blocks.oreLead = OreBlock(Items.lead)
        Blocks.oreLead.oreDefault = True
        Blocks.oreLead.oreThreshold = 0.828
        Blocks.oreLead.oreScale = 23.952381

        Blocks.oreScrap = OreBlock(Items.scrap)

        Blocks.oreCoal = OreBlock(Items.coal)
        Blocks.oreCoal.oreDefault = True
        Blocks.oreCoal.oreThreshold = 0.846
        Blocks.oreCoal.oreScale = 24.428572

        Blocks.oreTitanium = OreBlock(Items.titanium)
        Blocks.oreTitanium.oreDefault = True
        Blocks.oreTitanium.oreThreshold = 0.864
        Blocks.oreTitanium.oreScale = 24.904762

        Blocks.oreThorium = OreBlock(Items.thorium)
        Blocks.oreThorium.oreDefault = True
        Blocks.oreThorium.oreThreshold = 0.882
        Blocks.oreThorium.oreScale = 25.380953

        Blocks.oreBeryllium = OreBlock(Items.beryllium)

        Blocks.oreTungsten = OreBlock(Items.tungsten)

        Blocks.oreCrystalThorium = OreBlock("ore-crystal-thorium", Items.thorium)

        Blocks.wallOreThorium = OreBlock("ore-wall-thorium", Items.thorium)
        Blocks.wallOreThorium.wallOre = True

        Blocks.wallOreBeryllium = OreBlock("ore-wall-beryllium", Items.beryllium)
        Blocks.wallOreBeryllium.wallOre = True

        Blocks.graphiticWall = StaticWall("graphitic-wall")
        Blocks.graphiticWall.itemDrop = Items.graphite
        Blocks.graphiticWall.variants = 3

        # TODO merge with standard ore?
        Blocks.wallOreTungsten = OreBlock("ore-wall-tungsten", Items.tungsten)
        Blocks.wallOreTungsten.wallOre = True
        
        # region crafting
        
        Blocks.graphitePress = GenericCrafter("graphite-press")
        Blocks.graphitePress.setRequirements(Category.crafting, ItemStack.with_items(Items.titanium, 100, Items.silicon, 25, Items.lead, 100, Items.graphite, 50))
        # craftEffect = Fx.pulverizeMedium
        Blocks.graphitePress.outputItem = ItemStack(Items.graphite, 1)
        Blocks.graphitePress.craftTime = 90.0
        Blocks.graphitePress.size = 2
        Blocks.graphitePress.hasItems = True
        Blocks.graphitePress.consumeItem(Items.coal, 2)
        
        Blocks.multiPress = GenericCrafter("multi-press")
        Blocks.multiPress.setRequirements(Category.crafting, ItemStack.with_items(Items.titanium, 100, Items.silicon, 25, Items.lead, 100, Items.graphite, 50))
        # Blocks.multiPress.craftEffect = Fx.pulverizeMedium
        Blocks.multiPress.outputItem = ItemStack(Items.graphite, 2)
        Blocks.multiPress.craftTime = 30.0
        Blocks.multiPress.itemCapacity = 20
        Blocks.multiPress.size = 3
        Blocks.multiPress.hasItems = True
        Blocks.multiPress.hasLiquids = True
        Blocks.multiPress.hasPower = True
        Blocks.multiPress.consumePower(1.8)
        Blocks.multiPress.consumeItem(Items.coal, 3)
        Blocks.multiPress.consumeLiquid(Liquids.water, 0.1)
        
        Blocks.siliconSmelter = GenericCrafter("silicon-smelter")
        Blocks.siliconSmelter.setRequirements(Category.crafting, ItemStack.with_items(Items.copper, 30, Items.lead, 25))
        # Blocks.siliconSmelter.craftEffect = Fx.smeltsmoke
        Blocks.siliconSmelter.outputItem = ItemStack(Items.silicon, 1)
        Blocks.siliconSmelter.craftTime = 40.0
        Blocks.siliconSmelter.size = 2
        Blocks.siliconSmelter.hasPower = True
        Blocks.siliconSmelter.hasLiquids = False
        # Blocks.siliconSmelter.drawer = DrawMulti(DrawDefault(), DrawFlame(Color.valueOf("ffef99")))
        # Blocks.siliconSmelter.ambientSound = Sounds.smelter
        Blocks.siliconSmelter.ambientSoundVolume = 0.07
        Blocks.siliconSmelter.consumeItems(ItemStack.with_items(Items.coal, 1, Items.sand, 2))
        Blocks.siliconSmelter.consumePower(0.50)
        
        Blocks.siliconCrucible = AttributeCrafter("silicon-crucible")
        Blocks.siliconCrucible.setRequirements(Category.crafting, ItemStack.with_items(Items.titanium, 120, Items.metaglass, 80, Items.plastanium, 35, Items.silicon, 60))
        # Blocks.siliconCrucible.craftEffect = Fx.smeltsmoke
        Blocks.siliconCrucible.outputItem = ItemStack(Items.silicon, 8)
        Blocks.siliconCrucible.craftTime = 90.0
        Blocks.siliconCrucible.size = 3
        Blocks.siliconCrucible.hasPower = True
        Blocks.siliconCrucible.hasLiquids = False
        Blocks.siliconCrucible.itemCapacity = 30
        Blocks.siliconCrucible.boostScale = 0.15
        # Blocks.siliconCrucible.drawer = DrawMulti(DrawDefault(), DrawFlame(Color.valueOf("ffef99")))
        # Blocks.siliconCrucible.ambientSound = Sounds.smelter
        Blocks.siliconCrucible.ambientSoundVolume = 0.07
        Blocks.siliconCrucible.consumeItems(ItemStack.with_items(Items.coal, 4, Items.sand, 6, Items.pyratite, 1))
        Blocks.siliconCrucible.consumePower(4.0)
        
        Blocks.kiln = GenericCrafter("kiln")
        Blocks.kiln.setRequirements(Category.crafting, ItemStack.with_items(Items.copper, 60, Items.graphite, 30, Items.lead, 30))
        # Blocks.kiln.craftEffect = Fx.smeltsmoke
        Blocks.kiln.outputItem = ItemStack(Items.metaglass, 1)
        Blocks.kiln.craftTime = 30.0
        Blocks.kiln.size = 2
        Blocks.kiln.hasPower = True
        Blocks.kiln.hasItems = True
        # Blocks.kiln.drawer = DrawMulti(DrawDefault(), DrawFlame(Color.valueOf("ffc099")))
        # Blocks.kiln.ambientSound = Sounds.smelter
        Blocks.kiln.ambientSoundVolume = 0.07
        Blocks.kiln.consumeItems(ItemStack.with_items(Items.lead, 1, Items.sand, 1))
        Blocks.kiln.consumePower(0.60)

        Blocks.plastaniumCompressor = GenericCrafter("plastanium-compressor")
        Blocks.plastaniumCompressor.setRequirements(Category.crafting, ItemStack.with_items(Items.silicon, 80, Items.lead, 115, Items.graphite, 60, Items.titanium, 80))
        Blocks.plastaniumCompressor.hasItems = True
        Blocks.plastaniumCompressor.liquidCapacity = 60.0
        Blocks.plastaniumCompressor.craftTime = 60.0
        Blocks.plastaniumCompressor.outputItem = ItemStack(Items.plastanium, 1)
        Blocks.plastaniumCompressor.size = 2
        Blocks.plastaniumCompressor.health = 320
        Blocks.plastaniumCompressor.hasPower = True
        Blocks.plastaniumCompressor.hasLiquids = True
        # Blocks.plastaniumCompressor.craftEffect = Fx.formsmoke
        # Blocks.plastaniumCompressor.updateEffect = Fx.plasticburn
        # Blocks.plastaniumCompressor.drawer = DrawMulti(DrawDefault(), DrawFade())
        Blocks.plastaniumCompressor.consumeLiquid(Liquids.oil, 0.25)
        Blocks.plastaniumCompressor.consumePower(3.0)
        Blocks.plastaniumCompressor.consumeItem(Items.titanium, 2)

        Blocks.phaseWeaver = GenericCrafter("phase-weaver")
        Blocks.phaseWeaver.setRequirements(Category.crafting, ItemStack.with_items(Items.silicon, 130, Items.lead, 120, Items.thorium, 75))
        # Blocks.phaseWeaver.craftEffect = Fx.smeltsmoke
        Blocks.phaseWeaver.outputItem = ItemStack(Items.phaseFabric, 1)
        Blocks.phaseWeaver.craftTime = 120.0
        Blocks.phaseWeaver.size = 2
        Blocks.phaseWeaver.hasPower = True
        # Blocks.phaseWeaver.drawer = DrawMulti(DrawRegion("-bottom"), DrawWeave(), DrawDefault())
        Blocks.phaseWeaver.envEnabled |= Env.space
        # Blocks.phaseWeaver.ambientSound = Sounds.techloop
        Blocks.phaseWeaver.ambientSoundVolume = 0.02
        Blocks.phaseWeaver.consumeItems(ItemStack.with_items(Items.thorium, 4, Items.sand, 10))
        Blocks.phaseWeaver.consumePower(5.0)
        Blocks.phaseWeaver.itemCapacity = 30

        Blocks.surgeSmelter = GenericCrafter("surge-smelter")
        Blocks.surgeSmelter.setRequirements(Category.crafting, ItemStack.with_items(Items.silicon, 80, Items.lead, 80, Items.thorium, 70))
        # Blocks.surgeSmelter.craftEffect = Fx.smeltsmoke
        Blocks.surgeSmelter.outputItem = ItemStack(Items.surgeAlloy, 1)
        Blocks.surgeSmelter.craftTime = 75.0
        Blocks.surgeSmelter.size = 3
        Blocks.surgeSmelter.hasPower = True
        Blocks.surgeSmelter.itemCapacity = 20
        # Blocks.surgeSmelter.drawer = DrawMulti(DrawDefault(), DrawFlame())
        Blocks.surgeSmelter.consumePower(4.0)
        Blocks.surgeSmelter.consumeItems(ItemStack.with_items(Items.copper, 3, Items.lead, 4, Items.titanium, 2, Items.silicon, 3))

        Blocks.cryofluidMixer = GenericCrafter("cryofluid-mixer")
        Blocks.cryofluidMixer.setRequirements(Category.crafting, ItemStack.with_items(Items.lead, 65, Items.silicon, 40, Items.titanium, 60))
        Blocks.cryofluidMixer.outputLiquid = LiquidStack(Liquids.cryofluid, 12.0 / 60.0)
        Blocks.cryofluidMixer.size = 2
        Blocks.cryofluidMixer.hasPower = True
        Blocks.cryofluidMixer.hasItems = True
        Blocks.cryofluidMixer.hasLiquids = True
        Blocks.cryofluidMixer.rotate = False
        Blocks.cryofluidMixer.solid = True
        Blocks.cryofluidMixer.outputsLiquid = True
        Blocks.cryofluidMixer.envEnabled = Env.any
        # Blocks.cryofluidMixer.drawer = DrawMulti(DrawRegion("-bottom"), DrawLiquidTile(Liquids.water), DrawLiquidTile(Liquids.cryofluid, drawLiquidLight=True), DrawDefault())
        Blocks.cryofluidMixer.liquidCapacity = 24.0
        Blocks.cryofluidMixer.craftTime = 120.0
        Blocks.cryofluidMixer.lightLiquid = Liquids.cryofluid
        Blocks.cryofluidMixer.consumePower(1.0)
        Blocks.cryofluidMixer.consumeItem(Items.titanium)
        Blocks.cryofluidMixer.consumeLiquid(Liquids.water, 12.0 / 60.0)

        Blocks.pyratiteMixer = GenericCrafter("pyratite-mixer")
        Blocks.pyratiteMixer.setRequirements(Category.crafting, ItemStack.with_items(Items.copper, 50, Items.lead, 25))
        Blocks.pyratiteMixer.hasItems = True
        Blocks.pyratiteMixer.hasPower = True
        Blocks.pyratiteMixer.outputItem = ItemStack(Items.pyratite, 1)
        Blocks.pyratiteMixer.envEnabled |= Env.space
        Blocks.pyratiteMixer.size = 2
        Blocks.pyratiteMixer.consumePower(0.20)
        Blocks.pyratiteMixer.consumeItems(ItemStack.with_items(Items.coal, 1, Items.lead, 2, Items.sand, 2))

        Blocks.blastMixer = GenericCrafter("blast-mixer")
        Blocks.blastMixer.setRequirements(Category.crafting, ItemStack.with_items(Items.lead, 30, Items.titanium, 20))
        Blocks.blastMixer.hasItems = True
        Blocks.blastMixer.hasPower = True
        Blocks.blastMixer.outputItem = ItemStack(Items.blastCompound, 1)
        Blocks.blastMixer.size = 2
        Blocks.blastMixer.envEnabled |= Env.space
        Blocks.blastMixer.consumeItems(ItemStack.with_items(Items.pyratite, 1, Items.sporePod, 1))
        Blocks.blastMixer.consumePower(0.40)

        Blocks.melter = GenericCrafter("melter")
        Blocks.melter.setRequirements(Category.crafting, ItemStack.with_items(Items.copper, 30, Items.lead, 35, Items.graphite, 45))
        Blocks.melter.health = 200
        Blocks.melter.outputLiquid = LiquidStack(Liquids.slag, 12.0 / 60.0)
        Blocks.melter.craftTime = 10.0
        Blocks.melter.hasLiquids = True
        Blocks.melter.hasPower = True
        # Blocks.melter.drawer = DrawMulti(DrawRegion("-bottom"), DrawLiquidTile(), DrawDefault())
        Blocks.melter.consumePower(1.0)
        Blocks.melter.consumeItem(Items.scrap, 1)
        
        Blocks.separator = GenericCrafter("separator")
        Blocks.separator.setRequirements(Category.crafting, ItemStack.with_items(Items.copper, 30, Items.titanium, 25))
        Blocks.separator.outputItems = ItemStack.with_items(Items.copper, 5, Items.lead, 3, Items.graphite, 2, Items.titanium, 2)
        Blocks.separator.hasPower = True
        Blocks.separator.craftTime = 35.0
        Blocks.separator.size = 2
        Blocks.separator.consumePower(1.1)
        Blocks.separator.consumeLiquid(Liquids.slag, 4.0 / 60.0)

        Blocks.disassembler = GenericCrafter("disassembler")
        Blocks.disassembler.setRequirements(Category.crafting, ItemStack.with_items(Items.plastanium, 40, Items.titanium, 100, Items.silicon, 150, Items.thorium, 80))
        Blocks.disassembler.outputItems = ItemStack.with_items(Items.sand, 2, Items.graphite, 1, Items.titanium, 1, Items.thorium, 1)
        Blocks.disassembler.hasPower = True
        Blocks.disassembler.craftTime = 15.0
        Blocks.disassembler.size = 3
        Blocks.disassembler.itemCapacity = 20
        Blocks.disassembler.consumePower(4.0)
        Blocks.disassembler.consumeItem(Items.scrap)
        Blocks.disassembler.consumeLiquid(Liquids.slag, 0.12)

        Blocks.sporePress = GenericCrafter("spore-press")
        Blocks.sporePress.setRequirements(Category.crafting, ItemStack.with_items(Items.lead, 35, Items.silicon, 30))
        Blocks.sporePress.liquidCapacity = 60.0
        Blocks.sporePress.craftTime = 20.0
        Blocks.sporePress.outputLiquid = LiquidStack(Liquids.oil, 18.0 / 60.0)
        Blocks.sporePress.size = 2
        Blocks.sporePress.health = 320
        Blocks.sporePress.hasLiquids = True
        Blocks.sporePress.hasPower = True
        Blocks.sporePress.consumeItem(Items.sporePod, 1)
        Blocks.sporePress.consumePower(0.7)

        Blocks.pulverizer = GenericCrafter("pulverizer")
        Blocks.pulverizer.setRequirements(Category.crafting, ItemStack.with_items(Items.copper, 30, Items.lead, 25))
        Blocks.pulverizer.outputItem = ItemStack(Items.sand, 1)
        Blocks.pulverizer.craftTime = 40.0
        Blocks.pulverizer.hasItems = True
        Blocks.pulverizer.hasPower = True
        Blocks.pulverizer.consumeItem(Items.scrap, 1)
        Blocks.pulverizer.consumePower(0.5)

        Blocks.coalCentrifuge = GenericCrafter("coal-centrifuge")
        Blocks.coalCentrifuge.setRequirements(Category.crafting, ItemStack.with_items(Items.titanium, 20, Items.graphite, 40, Items.lead, 30))
        Blocks.coalCentrifuge.outputItem = ItemStack(Items.coal, 1)
        Blocks.coalCentrifuge.craftTime = 30.0
        Blocks.coalCentrifuge.size = 2
        Blocks.coalCentrifuge.hasPower = True
        Blocks.coalCentrifuge.hasItems = True
        Blocks.coalCentrifuge.hasLiquids = True
        Blocks.coalCentrifuge.consumeLiquid(Liquids.oil, 0.1)
        Blocks.coalCentrifuge.consumePower(0.7)
        
        Blocks.incinerator = GenericCrafter("incinerator")
        Blocks.incinerator.setRequirements(Category.crafting, ItemStack.with_items(Items.graphite, 5, Items.lead, 15))
        Blocks.incinerator.health = 90
        Blocks.incinerator.envEnabled |= Env.space
        Blocks.incinerator.consumePower(0.50)

        Blocks.siliconArcFurnace = GenericCrafter("silicon-arc-furnace")
        Blocks.siliconArcFurnace.setRequirements(Category.crafting, ItemStack.with_items(Items.beryllium, 70, Items.graphite, 80))
        # Blocks.siliconArcFurnace.craftEffect = Fx.none
        Blocks.siliconArcFurnace.outputItem = ItemStack(Items.silicon, 4)
        Blocks.siliconArcFurnace.craftTime = 50.0
        Blocks.siliconArcFurnace.size = 3
        Blocks.siliconArcFurnace.hasPower = True
        Blocks.siliconArcFurnace.hasLiquids = False
        Blocks.siliconArcFurnace.envEnabled |= Env.space | Env.underwater
        Blocks.siliconArcFurnace.envDisabled = Env.none
        Blocks.siliconArcFurnace.itemCapacity = 30
        # Blocks.siliconArcFurnace.drawer = DrawMulti(DrawRegion("-bottom"), DrawArcSmelt(), DrawDefault())
        Blocks.siliconArcFurnace.fogRadius = 3
        Blocks.siliconArcFurnace.researchCost = ItemStack.with_items(Items.beryllium, 150, Items.graphite, 50)
        # Blocks.siliconArcFurnace.ambientSound = Sounds.smelter
        # Blocks.siliconArcFurnace.ambientSoundVolume = 0.12
        Blocks.siliconArcFurnace.consumeItems(ItemStack.with_items(Items.graphite, 1, Items.sand, 4))
        Blocks.siliconArcFurnace.consumePower(6.0)

        Blocks.electrolyzer = GenericCrafter("electrolyzer")
        Blocks.electrolyzer.setRequirements(Category.crafting, ItemStack.with_items(Items.silicon, 50, Items.graphite, 40, Items.beryllium, 130, Items.tungsten, 80))
        Blocks.electrolyzer.size = 3
        Blocks.electrolyzer.researchCostMultiplier = 1.2
        Blocks.electrolyzer.craftTime = 10.0
        Blocks.electrolyzer.rotate = True
        Blocks.electrolyzer.invertFlip = True
        Blocks.electrolyzer.group = BlockGroup.liquids
        Blocks.electrolyzer.itemCapacity = 0
        Blocks.electrolyzer.liquidCapacity = 50.0
        Blocks.electrolyzer.consumeLiquid(Liquids.water, 10.0 / 60.0)
        Blocks.electrolyzer.consumePower(1.0)
        # drawer = new DrawMulti(
        #         new DrawRegion("-bottom"),
        #         new DrawLiquidTile(Liquids.water, 2f),
        #         new DrawBubbles(Color.valueOf("7693e3")){{
        #             sides = 10;
        #             recurrence = 3f;
        #             spread = 6;
        #             radius = 1.5f;
        #             amount = 20;
        #         }},
        #         new DrawRegion(),
        #         new DrawLiquidOutputs(),
        #         new DrawGlowRegion(){{
        #             alpha = 0.7f;
        #             color = Color.valueOf("c4bdf3");
        #             glowIntensity = 0.3f;
        #             glowScale = 6f;
        #         }}
        
        # Blocks.electrolyzer.ambientSound = Sounds.electricHum
        Blocks.electrolyzer.ambientSoundVolume = 0.08
        Blocks.electrolyzer.regionRotated1 = 3
        Blocks.electrolyzer.outputLiquids = LiquidStack.with_liquids(Liquids.ozone, 4.0 / 60.0, Liquids.hydrogen, 6.0 / 60.0)
        Blocks.electrolyzer.liquidOutputDirections = [1, 3]
        
        Blocks.atmosphericConcentrator = HeatCrafter("atmospheric-concentrator")
        Blocks.atmosphericConcentrator.setRequirements(Category.crafting, ItemStack.with_items(Items.oxide, 60, Items.beryllium, 180, Items.silicon, 150))
        Blocks.atmosphericConcentrator.size = 3
        Blocks.atmosphericConcentrator.hasLiquids = True
        Blocks.atmosphericConcentrator.liquidCapacity = 40.0
        Blocks.atmosphericConcentrator.itemCapacity = 0
        Blocks.atmosphericConcentrator.consumePower(2.0)
        # Blocks.atmosphericConcentrator.ambientSound = Sounds.extractLoop
        Blocks.atmosphericConcentrator.ambientSoundVolume = 0.06
        Blocks.atmosphericConcentrator.heatRequirement = 6.0
        Blocks.atmosphericConcentrator.outputLiquid = LiquidStack(Liquids.nitrogen, 4.0 / 60.0)
        Blocks.atmosphericConcentrator.researchCostMultiplier = 1.1
        Blocks.atmosphericConcentrator.researchCost = ItemStack.with_items(Items.silicon, 2000, Items.oxide, 900, Items.beryllium, 2400)
        # Blocks.atmosphericConcentrator.drawer = DrawMulti(DrawRegion("-bottom"), DrawLiquidTile(Liquids.nitrogen, 4.1), DrawDefault(), DrawHeatInput(), DrawParticles(color=Color.valueOf("d4f0ff"), alpha=0.6, particleSize=4.0, particles=10, particleRad=12.0, particleLife=140.0))
        
        Blocks.oxidationChamber = HeatProducer("oxidation-chamber")
        Blocks.oxidationChamber.setRequirements(Category.crafting, ItemStack.with_items(Items.tungsten, 120, Items.graphite, 80, Items.silicon, 100, Items.beryllium, 120))
        Blocks.oxidationChamber.size = 3
        Blocks.oxidationChamber.outputItem = ItemStack(Items.oxide, 1)
        Blocks.oxidationChamber.researchCostMultiplier = 1.1
        Blocks.oxidationChamber.consumeLiquid(Liquids.ozone, 2.0 / 60.0)
        Blocks.oxidationChamber.consumeItem(Items.beryllium)
        Blocks.oxidationChamber.consumePower(0.5)
        Blocks.oxidationChamber.rotateDraw = False
        # Blocks.oxidationChamber.drawer = DrawMulti(DrawRegion("-bottom"), DrawLiquidRegion(), DrawDefault(), DrawHeatOutput())
        # Blocks.oxidationChamber.ambientSound = Sounds.extractLoop
        Blocks.oxidationChamber.ambientSoundVolume = 0.08
        Blocks.oxidationChamber.regionRotated1 = 2
        Blocks.oxidationChamber.craftTime = 60.0 * 2.0
        Blocks.oxidationChamber.liquidCapacity = 30.0
        Blocks.oxidationChamber.heatOutput = 5.0
        
        Blocks.electricHeater = HeatProducer("electric-heater")
        Blocks.electricHeater.setRequirements(Category.crafting, ItemStack.with_items(Items.tungsten, 30, Items.oxide, 30, Items.beryllium, 30))
        Blocks.electricHeater.researchCostMultiplier = 4.0
        # Blocks.electricHeater.drawer = DrawMulti(DrawDefault(), DrawHeatOutput())
        Blocks.electricHeater.rotateDraw = False
        Blocks.electricHeater.size = 2
        Blocks.electricHeater.heatOutput = 3.0
        Blocks.electricHeater.regionRotated1 = 1
        # Blocks.electricHeater.ambientSound = Sounds.hum
        Blocks.electricHeater.itemCapacity = 0
        Blocks.electricHeater.consumePower(100.0 / 60.0)

        Blocks.slagHeater = HeatProducer("slag-heater")
        Blocks.slagHeater.setRequirements(Category.crafting, ItemStack.with_items(Items.tungsten, 50, Items.oxide, 20, Items.beryllium, 20))
        Blocks.slagHeater.researchCostMultiplier = 4.0
        # Blocks.slagHeater.drawer = DrawMulti(DrawRegion("-bottom"), DrawLiquidTile(Liquids.slag), DrawDefault(), DrawHeatOutput())
        Blocks.slagHeater.size = 3
        Blocks.slagHeater.itemCapacity = 0
        Blocks.slagHeater.liquidCapacity = 40.0
        Blocks.slagHeater.rotateDraw = False
        Blocks.slagHeater.regionRotated1 = 1
        # Blocks.slagHeater.ambientSound = Sounds.hum
        Blocks.slagHeater.consumeLiquid(Liquids.slag, 40.0 / 60.0)
        Blocks.slagHeater.heatOutput = 8.0
        Blocks.slagHeater.researchCost = ItemStack.with_items(Items.tungsten, 1200, Items.oxide, 900, Items.beryllium, 2400)

        Blocks.phaseHeater = HeatProducer("phase-heater")
        Blocks.phaseHeater.setRequirements(Category.crafting, ItemStack.with_items(Items.oxide, 30, Items.carbide, 30, Items.beryllium, 30))
        # Blocks.phaseHeater.drawer = DrawMulti(DrawDefault(), DrawHeatOutput())
        Blocks.phaseHeater.size = 2
        Blocks.phaseHeater.heatOutput = 15.0
        Blocks.phaseHeater.craftTime = 60.0 * 8.0
        # Blocks.phaseHeater.ambientSound = Sounds.hum
        Blocks.phaseHeater.consumeItem(Items.phaseFabric)

        Blocks.heatRedirector = HeatConductor("heat-redirector")
        Blocks.heatRedirector.setRequirements(Category.crafting, ItemStack.with_items(Items.tungsten, 10, Items.graphite, 10))
        Blocks.heatRedirector.researchCostMultiplier = 10.0
        Blocks.heatRedirector.group = BlockGroup.heat
        Blocks.heatRedirector.size = 3
        # Blocks.heatRedirector.drawer = DrawMulti(DrawDefault(), DrawHeatOutput(), DrawHeatInput("-heat"))
        Blocks.heatRedirector.regionRotated1 = 1

        Blocks.smallHeatRedirector = HeatConductor("small-heat-redirector")
        Blocks.smallHeatRedirector.setRequirements(Category.crafting, ItemStack.with_items(Items.surgeAlloy, 10, Items.graphite, 10))
        Blocks.smallHeatRedirector.researchCostMultiplier = 10.0
        Blocks.smallHeatRedirector.group = BlockGroup.heat
        Blocks.smallHeatRedirector.size = 2
        # Blocks.smallHeatRedirector.drawer = DrawMulti(DrawDefault(), DrawHeatOutput(), DrawHeatInput("-heat"))
        Blocks.smallHeatRedirector.regionRotated1 = 1

        Blocks.heatRouter = HeatConductor("heat-router")
        Blocks.heatRouter.setRequirements(Category.crafting, ItemStack.with_items(Items.tungsten, 15, Items.graphite, 10))
        Blocks.heatRouter.researchCostMultiplier = 10.0
        Blocks.heatRouter.group = BlockGroup.heat
        Blocks.heatRouter.size = 3
        # Blocks.heatRouter.drawer = DrawMulti(DrawDefault(), DrawHeatOutput(-1, False), DrawHeatOutput(), DrawHeatOutput(1, False), DrawHeatInput("-heat"))
        Blocks.heatRouter.regionRotated1 = 1
        Blocks.heatRouter.splitHeat = True
        
        Blocks.slagIncinerator = ItemIncinerator("slag-incinerator")
        Blocks.slagIncinerator.setRequirements(Category.crafting, ItemStack.with_items(Items.tungsten, 15))
        Blocks.slagIncinerator.size = 1
        Blocks.slagIncinerator.consumeLiquid(Liquids.slag, 0.0)
        
        Blocks.carbideCrucible = HeatCrafter("carbide-crucible")
        Blocks.carbideCrucible.setRequirements(Category.crafting, ItemStack.with_items(Items.tungsten, 110, Items.thorium, 150, Items.oxide, 60))
        # Blocks.carbideCrucible.craftEffect = Fx.none
        Blocks.carbideCrucible.outputItem = ItemStack(Items.carbide, 1)
        Blocks.carbideCrucible.craftTime = 135.0
        Blocks.carbideCrucible.size = 3
        Blocks.carbideCrucible.itemCapacity = 20
        Blocks.carbideCrucible.hasPower = True
        Blocks.carbideCrucible.hasItems = True
        # Blocks.carbideCrucible.drawer = DrawMulti(DrawRegion("-bottom"), DrawCrucibleFlame(), DrawDefault(), DrawHeatInput())
        # Blocks.carbideCrucible.ambientSound = Sounds.smelter
        Blocks.carbideCrucible.ambientSoundVolume = 0.09
        Blocks.carbideCrucible.heatRequirement = 10.0
        Blocks.carbideCrucible.consumeItems(ItemStack.with_items(Items.tungsten, 2, Items.graphite, 3))
        Blocks.carbideCrucible.consumePower(2.0)

        Blocks.slagCentrifuge = GenericCrafter("slag-centrifuge")
        Blocks.slagCentrifuge.setRequirements(Category.crafting, BuildVisibility.debugOnly, ItemStack.with_items(Items.carbide, 70, Items.graphite, 60, Items.silicon, 40, Items.oxide, 40))
        Blocks.slagCentrifuge.consumePower(2.0 / 60.0)
        Blocks.slagCentrifuge.size = 3
        Blocks.slagCentrifuge.consumeItem(Items.sand, 1)
        Blocks.slagCentrifuge.consumeLiquid(Liquids.slag, 40.0 / 60.0)
        Blocks.slagCentrifuge.liquidCapacity = 80.0
        # Blocks.slagCentrifuge.drawer = DrawMulti(DrawRegion("-bottom"), DrawLiquidRegion(Liquids.slag, alpha=0.7), DrawGlowRegion(-1.0, glowIntensity=0.3, rotateSpeed=3.0, alpha=0.4, color=Color(1.0, 0.5, 0.5, 1.0)), DrawDefault())
        Blocks.slagCentrifuge.craftTime = 120.0
        Blocks.slagCentrifuge.outputLiquid = LiquidStack(Liquids.gallium, 1.0 / 60.0)

        Blocks.surgeCrucible = HeatCrafter("surge-crucible")
        Blocks.surgeCrucible.setRequirements(Category.crafting, ItemStack.with_items(Items.silicon, 100, Items.graphite, 80, Items.tungsten, 80, Items.oxide, 80))
        Blocks.surgeCrucible.size = 3
        Blocks.surgeCrucible.itemCapacity = 20
        Blocks.surgeCrucible.heatRequirement = 10.0
        Blocks.surgeCrucible.craftTime = 180.0
        Blocks.surgeCrucible.liquidCapacity = 400.0
        # Blocks.surgeCrucible.ambientSound = Sounds.smelter
        Blocks.surgeCrucible.ambientSoundVolume = 0.9
        Blocks.surgeCrucible.outputItem = ItemStack(Items.surgeAlloy, 1)
        # Blocks.surgeCrucible.craftEffect = RadialEffect(Fx.surgeCruciSmoke, 4, 90.0, 5.0)
        # Blocks.surgeCrucible.drawer = DrawMulti(DrawRegion("-bottom"), DrawCircles(color=Color.valueOf("ffc073").a(0.24), strokeMax=2.5, radius=10.0, amount=3), DrawLiquidRegion(Liquids.slag), DrawDefault(), DrawHeatInput(), DrawHeatRegion(color=Color.valueOf("ff6060ff")), DrawHeatRegion("-vents", color.a=1.0))
        Blocks.surgeCrucible.consumeItem(Items.silicon, 3)
        Blocks.surgeCrucible.consumeLiquid(Liquids.slag, 40.0 / 60.0)
        Blocks.surgeCrucible.consumePower(2.0)

        Blocks.cyanogenSynthesizer = HeatCrafter("cyanogen-synthesizer")
        Blocks.cyanogenSynthesizer.setRequirements(Category.crafting, ItemStack.with_items(Items.carbide, 50, Items.silicon, 80, Items.beryllium, 90))
        Blocks.cyanogenSynthesizer.heatRequirement = 5.0
        # Blocks.cyanogenSynthesizer.drawer = DrawMulti(DrawRegion("-bottom"), DrawLiquidTile(Liquids.cyanogen), DrawParticles(color=Color.valueOf("89e8b6"), alpha=0.5, particleSize=3.0, particles=10, particleRad=9.0, particleLife=200.0, reverse=True, particleSizeInterp=Interp.one), DrawDefault(), DrawHeatInput(), DrawHeatRegion("-heat-top"))
        Blocks.cyanogenSynthesizer.size = 3
        # Blocks.cyanogenSynthesizer.ambientSound = Sounds.extractLoop
        Blocks.cyanogenSynthesizer.ambientSoundVolume = 0.08
        Blocks.cyanogenSynthesizer.liquidCapacity = 80.0
        Blocks.cyanogenSynthesizer.outputLiquid = LiquidStack(Liquids.cyanogen, 3.0 / 60.0)
        Blocks.cyanogenSynthesizer.consumeLiquid(Liquids.arkycite, 40.0 / 60.0)
        Blocks.cyanogenSynthesizer.consumeItem(Items.graphite)
        Blocks.cyanogenSynthesizer.consumePower(2.0)

        Blocks.phaseSynthesizer = HeatCrafter("phase-synthesizer")
        Blocks.phaseSynthesizer.setRequirements(Category.crafting, ItemStack.with_items(Items.carbide, 90, Items.silicon, 100, Items.thorium, 100, Items.tungsten, 200))
        Blocks.phaseSynthesizer.size = 3
        Blocks.phaseSynthesizer.itemCapacity = 40
        Blocks.phaseSynthesizer.heatRequirement = 8.0
        Blocks.phaseSynthesizer.craftTime = 120.0
        Blocks.phaseSynthesizer.liquidCapacity = 40.0
        # Blocks.phaseSynthesizer.ambientSound = Sounds.techloop
        Blocks.phaseSynthesizer.ambientSoundVolume = 0.04
        Blocks.phaseSynthesizer.outputItem = ItemStack(Items.phaseFabric, 1)
        # Blocks.phaseSynthesizer.drawer = DrawMulti(DrawRegion("-bottom"), DrawSpikes(color=Color.valueOf("ffd59e"), stroke=1.5, layers=2, amount=12, rotateSpeed=0.5, layerSpeed=-0.9), DrawMultiWeave(glowColor=Color(1.0, 0.4, 0.4, 0.8)), DrawDefault(), DrawHeatInput(), DrawHeatRegion("-vents", color=Color(1.0, 0.4, 0.3, 1.0)))
        Blocks.phaseSynthesizer.consumeItems(ItemStack.with_items(Items.thorium, 2, Items.sand, 6))
        Blocks.phaseSynthesizer.consumeLiquid(Liquids.ozone, 2.0 / 60.0)
        Blocks.phaseSynthesizer.consumePower(8.0)

        Blocks.heatReactor = HeatProducer("heat-reactor")
        Blocks.heatReactor.setRequirements(Category.crafting, BuildVisibility.debugOnly, ItemStack.with_items(Items.oxide, 70, Items.graphite, 20, Items.carbide, 10, Items.thorium, 80))
        Blocks.heatReactor.size = 3
        Blocks.heatReactor.craftTime = 600.0
        # Blocks.heatReactor.craftEffect = RadialEffect(Fx.heatReactorSmoke, 4, 90.0, 7.0)
        Blocks.heatReactor.itemCapacity = 20
        Blocks.heatReactor.outputItem = ItemStack(Items.fissileMatter, 1)
        Blocks.heatReactor.consumeItem(Items.thorium, 3)
        Blocks.heatReactor.consumeLiquid(Liquids.nitrogen, 1.0 / 60.0)
        
        # region defense
        wallHealthMultiplier:int = 4
        
        Blocks.copperWall = Wall("copper-wall")
        Blocks.copperWall.requirements = Category.defense, ItemStack.with_items(Items.copper, 6)
        Blocks.copperWall.health = 80 * wallHealthMultiplier
        Blocks.copperWall.researchCostMultiplier = 0.1

        Blocks.copperWallLarge = Wall("copper-wall-large")
        Blocks.copperWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.copperWall.requirements, 4)
        Blocks.copperWallLarge.health = 80 * 4 * wallHealthMultiplier
        Blocks.copperWallLarge.size = 2

        Blocks.titaniumWall = Wall("titanium-wall")
        Blocks.titaniumWall.requirements = Category.defense, ItemStack.with_items(Items.titanium, 6)
        Blocks.titaniumWall.health = 110 * wallHealthMultiplier

        Blocks.titaniumWallLarge = Wall("titanium-wall-large")
        Blocks.titaniumWallLarge.requirements = Category.defense, ItemStack.ItemStack.mult(Blocks.titaniumWall.requirements, 4)
        Blocks.titaniumWallLarge.health = 110 * wallHealthMultiplier * 4
        Blocks.titaniumWallLarge.size = 2

        Blocks.plastaniumWall = Wall("plastanium-wall")
        Blocks.plastaniumWall.requirements = Category.defense, ItemStack.with_items(Items.plastanium, 5, Items.metaglass, 2)
        Blocks.plastaniumWall.health = 125 * wallHealthMultiplier
        Blocks.plastaniumWall.insulated = True
        Blocks.plastaniumWall.absorbLasers = True
        Blocks.plastaniumWall.schematicPriority = 10

        Blocks.plastaniumWallLarge = Wall("plastanium-wall-large")
        Blocks.plastaniumWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.plastaniumWall.requirements, 4)
        Blocks.plastaniumWallLarge.health = 125 * wallHealthMultiplier * 4
        Blocks.plastaniumWallLarge.size = 2
        Blocks.plastaniumWallLarge.insulated = True
        Blocks.plastaniumWallLarge.absorbLasers = True
        Blocks.plastaniumWallLarge.schematicPriority = 10

        Blocks.thoriumWall = Wall("thorium-wall")
        Blocks.thoriumWall.requirements = Category.defense, ItemStack.with_items(Items.thorium, 6)
        Blocks.thoriumWall.health = 200 * wallHealthMultiplier

        Blocks.thoriumWallLarge = Wall("thorium-wall-large")
        Blocks.thoriumWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.thoriumWall.requirements, 4)
        Blocks.thoriumWallLarge.health = 200 * wallHealthMultiplier * 4
        Blocks.thoriumWallLarge.size = 2

        Blocks.phaseWall = Wall("phase-wall")
        Blocks.phaseWall.requirements = Category.defense, ItemStack.with_items(Items.phaseFabric, 6)
        Blocks.phaseWall.health = 150 * wallHealthMultiplier
        Blocks.phaseWall.chanceDeflect = 10.0
        Blocks.phaseWall.flashHit = True

        Blocks.phaseWallLarge = Wall("phase-wall-large")
        Blocks.phaseWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.phaseWall.requirements, 4)
        Blocks.phaseWallLarge.health = 150 * 4 * wallHealthMultiplier
        Blocks.phaseWallLarge.size = 2
        Blocks.phaseWallLarge.chanceDeflect = 10.0
        Blocks.phaseWallLarge.flashHit = True

        Blocks.surgeWall = Wall("surge-wall")
        Blocks.surgeWall.requirements = Category.defense, ItemStack.with_items(Items.surgeAlloy, 6)
        Blocks.surgeWall.health = 230 * wallHealthMultiplier
        Blocks.surgeWall.lightningChance = 0.05

        Blocks.surgeWallLarge = Wall("surge-wall-large")
        Blocks.surgeWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.surgeWall.requirements, 4)
        Blocks.surgeWallLarge.health = 230 * 4 * wallHealthMultiplier
        Blocks.surgeWallLarge.size = 2
        Blocks.surgeWallLarge.lightningChance = 0.05
        
        Blocks.door = Door("door")
        Blocks.door.requirements = Category.defense, ItemStack.with_items(Items.titanium, 6, Items.silicon, 4)
        Blocks.door.health = 100 * wallHealthMultiplier

        Blocks.doorLarge = Door("door-large")
        Blocks.doorLarge.requirements = Category.defense, ItemStack.mult(Blocks.door.requirements, 4)
        # Blocks.doorLarge.openfx = Fx.dooropenlarge
        # Blocks.doorLarge.closefx = Fx.doorcloselarge
        Blocks.doorLarge.health = 100 * 4 * wallHealthMultiplier
        Blocks.doorLarge.size = 2

        Blocks.scrapWall = Wall("scrap-wall")
        Blocks.scrapWall.requirements = Category.defense, ItemStack.with_items(Items.scrap, 6)
        Blocks.scrapWall.health = 60 * wallHealthMultiplier
        Blocks.scrapWall.variants = 5
        Blocks.scrapWall.buildCostMultiplier = 4.0

        Blocks.scrapWallLarge = Wall("scrap-wall-large")
        Blocks.scrapWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.scrapWall.requirements, 4)
        Blocks.scrapWallLarge.health = 60 * 4 * wallHealthMultiplier
        Blocks.scrapWallLarge.size = 2
        Blocks.scrapWallLarge.variants = 4
        Blocks.scrapWallLarge.buildCostMultiplier = 4.0

        Blocks.scrapWallHuge = Wall("scrap-wall-huge")
        Blocks.scrapWallHuge.requirements = Category.defense, ItemStack.mult(Blocks.scrapWall.requirements, 9)
        Blocks.scrapWallHuge.health = 60 * 9 * wallHealthMultiplier
        Blocks.scrapWallHuge.size = 3
        Blocks.scrapWallHuge.variants = 3
        Blocks.scrapWallHuge.buildCostMultiplier = 4.0

        Blocks.scrapWallGigantic = Wall("scrap-wall-gigantic")
        Blocks.scrapWallGigantic.requirements = Category.defense, ItemStack.mult(Blocks.scrapWall.requirements, 16)
        Blocks.scrapWallGigantic.health = 60 * 16 * wallHealthMultiplier
        Blocks.scrapWallGigantic.size = 4
        Blocks.scrapWallGigantic.buildCostMultiplier = 4.0
        
        Blocks.thruster = Thruster("thruster")
        Blocks.thruster.requirements = Category.defense, BuildVisibility.sandboxOnly, ItemStack.with_items(Items.scrap, 96)
        Blocks.thruster.health = 55 * 16 * wallHealthMultiplier
        Blocks.thruster.size = 4

        Blocks.berylliumWall = Wall("beryllium-wall")
        Blocks.berylliumWall.requirements = Category.defense, ItemStack.with_items(Items.beryllium, 6)
        Blocks.berylliumWall.health = 130 * wallHealthMultiplier
        Blocks.berylliumWall.armor = 2.0
        Blocks.berylliumWall.buildCostMultiplier = 8.0

        Blocks.berylliumWallLarge = Wall("beryllium-wall-large")
        Blocks.berylliumWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.berylliumWall.requirements, 4)
        Blocks.berylliumWallLarge.health = 130 * wallHealthMultiplier * 4
        Blocks.berylliumWallLarge.armor = 2.0
        Blocks.berylliumWallLarge.buildCostMultiplier = 5.0
        Blocks.berylliumWallLarge.size = 2

        Blocks.tungstenWall = Wall("tungsten-wall")
        Blocks.tungstenWall.requirements = Category.defense, ItemStack.with_items(Items.tungsten, 6)
        Blocks.tungstenWall.health = 180 * wallHealthMultiplier
        Blocks.tungstenWall.armor = 14.0
        Blocks.tungstenWall.buildCostMultiplier = 8.0

        Blocks.tungstenWallLarge = Wall("tungsten-wall-large")
        Blocks.tungstenWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.tungstenWall.requirements, 4)
        Blocks.tungstenWallLarge.health = 180 * wallHealthMultiplier * 4
        Blocks.tungstenWallLarge.armor = 14.0
        Blocks.tungstenWallLarge.buildCostMultiplier = 5.0
        Blocks.tungstenWallLarge.size = 2
        
        Blocks.blastDoor = AutoDoor("blast-door")
        Blocks.blastDoor.requirements = Category.defense, ItemStack.with_items(Items.tungsten, 24, Items.silicon, 24)
        Blocks.blastDoor.health = 175 * wallHealthMultiplier * 4
        Blocks.blastDoor.armor = 14.0
        Blocks.blastDoor.size = 2

        Blocks.reinforcedSurgeWall = Wall("reinforced-surge-wall")
        Blocks.reinforcedSurgeWall.requirements = Category.defense, ItemStack.with_items(Items.surgeAlloy, 6, Items.tungsten, 2)
        Blocks.reinforcedSurgeWall.health = 250 * wallHealthMultiplier
        Blocks.reinforcedSurgeWall.lightningChance = 0.05
        Blocks.reinforcedSurgeWall.lightningDamage = 30.0
        Blocks.reinforcedSurgeWall.armor = 20.0
        Blocks.reinforcedSurgeWall.researchCost = ItemStack.with_items(Items.surgeAlloy, 20, Items.tungsten, 100)

        Blocks.reinforcedSurgeWallLarge = Wall("reinforced-surge-wall-large")
        Blocks.reinforcedSurgeWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.reinforcedSurgeWall.requirements, 4)
        Blocks.reinforcedSurgeWallLarge.health = 250 * wallHealthMultiplier * 4
        Blocks.reinforcedSurgeWallLarge.lightningChance = 0.05
        Blocks.reinforcedSurgeWallLarge.lightningDamage = 30.0
        Blocks.reinforcedSurgeWallLarge.armor = 20.0
        Blocks.reinforcedSurgeWallLarge.size = 2
        Blocks.reinforcedSurgeWallLarge.researchCost = ItemStack.with_items(Items.surgeAlloy, 40, Items.tungsten, 200)

        Blocks.carbideWall = Wall("carbide-wall")
        Blocks.carbideWall.requirements = Category.defense, ItemStack.with_items(Items.thorium, 6, Items.carbide, 6)
        Blocks.carbideWall.health = 270 * wallHealthMultiplier
        Blocks.carbideWall.armor = 16.0

        Blocks.carbideWallLarge = Wall("carbide-wall-large")
        Blocks.carbideWallLarge.requirements = Category.defense, ItemStack.mult(Blocks.carbideWall.requirements, 4)
        Blocks.carbideWallLarge.health = 270 * wallHealthMultiplier * 4
        Blocks.carbideWallLarge.armor = 16.0
        Blocks.carbideWallLarge.size = 2
        
        Blocks.shieldedWall = ShieldWall("shielded-wall")
        Blocks.shieldedWall.requirements = Category.defense, ItemStack.with_items(Items.phaseFabric, 20, Items.surgeAlloy, 12, Items.beryllium, 12)
        Blocks.shieldedWall.consumePower(3.0 / 60.0)
        Blocks.shieldedWall.outputsPower = False
        Blocks.shieldedWall.hasPower = True
        Blocks.shieldedWall.consumesPower = True
        Blocks.shieldedWall.conductivePower = True
        Blocks.shieldedWall.chanceDeflect = 8.0
        Blocks.shieldedWall.health = 260 * wallHealthMultiplier * 4
        Blocks.shieldedWall.armor = 15.0
        Blocks.shieldedWall.size = 2
        
        Blocks.mender = MendProjector("mender")
        Blocks.mender.setRequirements(Category.effect, ItemStack.with_items(Items.lead, 30, Items.copper, 25))
        Blocks.mender.consumePower(0.3)
        Blocks.mender.size = 1
        Blocks.mender.reload = 200.0
        Blocks.mender.range = 40.0
        Blocks.mender.healPercent = 4.0
        Blocks.mender.phaseBoost = 4.0
        Blocks.mender.phaseRangeBoost = 20.0
        Blocks.mender.health = 80
        Blocks.mender.consumeItem(Items.silicon).boost()

        Blocks.mendProjector = MendProjector("mend-projector")
        Blocks.mendProjector.setRequirements(Category.effect, ItemStack.with_items(Items.lead, 100, Items.titanium, 25, Items.silicon, 40, Items.copper, 50))
        Blocks.mendProjector.consumePower(1.5)
        Blocks.mendProjector.size = 2
        Blocks.mendProjector.reload = 250.0
        Blocks.mendProjector.range = 85.0
        Blocks.mendProjector.healPercent = 11.0
        Blocks.mendProjector.phaseBoost = 15.0
        Blocks.mendProjector.scaledHealth = 80
        Blocks.mendProjector.consumeItem(Items.phaseFabric).boost()
        
        