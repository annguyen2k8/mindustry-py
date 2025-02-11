from mindustry.world.consumer import *
from mindustry.world.blocks import *
from mindustry.world.meta import *
from mindustry.graphics import *
from mindustry.type import *
from mindustry.vars import *

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
        Blocks.graphitePress.setRequirements(Category.crafting, ItemStack.with_item(Items.titanium, 100, Items.silicon, 25, Items.lead, 100, Items.graphite, 50))
        # craftEffect = Fx.pulverizeMedium
        Blocks.graphitePress.outputItem = ItemStack(Items.graphite, 1)
        Blocks.graphitePress.craftTime = 90.0
        Blocks.graphitePress.size = 2
        Blocks.graphitePress.hasItems = True
        Blocks.graphitePress.consumeItem(Items.coal, 2)
        
        Blocks.multiPress = GenericCrafter("multi-press")
        Blocks.multiPress.setRequirements(Category.crafting, ItemStack.with_item(Items.titanium, 100, Items.silicon, 25, Items.lead, 100, Items.graphite, 50))
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
        Blocks.siliconSmelter.setRequirements(Category.crafting, ItemStack.with_item(Items.copper, 30, Items.lead, 25))
        # Blocks.siliconSmelter.craftEffect = Fx.smeltsmoke
        Blocks.siliconSmelter.outputItem = ItemStack(Items.silicon, 1)
        Blocks.siliconSmelter.craftTime = 40.0
        Blocks.siliconSmelter.size = 2
        Blocks.siliconSmelter.hasPower = True
        Blocks.siliconSmelter.hasLiquids = False
        # Blocks.siliconSmelter.drawer = DrawMulti(DrawDefault(), DrawFlame(Color.valueOf("ffef99")))
        # Blocks.siliconSmelter.ambientSound = Sounds.smelter
        Blocks.siliconSmelter.ambientSoundVolume = 0.07
        Blocks.siliconSmelter.consumeItems(ItemStack.with_item(Items.coal, 1, Items.sand, 2))
        Blocks.siliconSmelter.consumePower(0.50)
        
        Blocks.siliconCrucible = AttributeCrafter("silicon-crucible")
        Blocks.siliconCrucible.setRequirements(Category.crafting, ItemStack.with_item(Items.titanium, 120, Items.metaglass, 80, Items.plastanium, 35, Items.silicon, 60))
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
        Blocks.siliconCrucible.consumeItems(ItemStack.with_item(Items.coal, 4, Items.sand, 6, Items.pyratite, 1))
        Blocks.siliconCrucible.consumePower(4.0)
        
        Blocks.kiln = GenericCrafter("kiln")
        Blocks.kiln.setRequirements(Category.crafting, ItemStack.with_item(Items.copper, 60, Items.graphite, 30, Items.lead, 30))
        # Blocks.kiln.craftEffect = Fx.smeltsmoke
        Blocks.kiln.outputItem = ItemStack(Items.metaglass, 1)
        Blocks.kiln.craftTime = 30.0
        Blocks.kiln.size = 2
        Blocks.kiln.hasPower = True
        Blocks.kiln.hasItems = True
        # Blocks.kiln.drawer = DrawMulti(DrawDefault(), DrawFlame(Color.valueOf("ffc099")))
        # Blocks.kiln.ambientSound = Sounds.smelter
        Blocks.kiln.ambientSoundVolume = 0.07
        Blocks.kiln.consumeItems(ItemStack.with_item(Items.lead, 1, Items.sand, 1))
        Blocks.kiln.consumePower(0.60)

        Blocks.plastaniumCompressor = GenericCrafter("plastanium-compressor")
        Blocks.plastaniumCompressor.setRequirements(Category.crafting, ItemStack.with_item(Items.silicon, 80, Items.lead, 115, Items.graphite, 60, Items.titanium, 80))
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
        Blocks.phaseWeaver.setRequirements(Category.crafting, ItemStack.with_item(Items.silicon, 130, Items.lead, 120, Items.thorium, 75))
        # Blocks.phaseWeaver.craftEffect = Fx.smeltsmoke
        Blocks.phaseWeaver.outputItem = ItemStack(Items.phaseFabric, 1)
        Blocks.phaseWeaver.craftTime = 120.0
        Blocks.phaseWeaver.size = 2
        Blocks.phaseWeaver.hasPower = True
        # Blocks.phaseWeaver.drawer = DrawMulti(DrawRegion("-bottom"), DrawWeave(), DrawDefault())
        Blocks.phaseWeaver.envEnabled |= Env.space
        # Blocks.phaseWeaver.ambientSound = Sounds.techloop
        Blocks.phaseWeaver.ambientSoundVolume = 0.02
        Blocks.phaseWeaver.consumeItems(ItemStack.with_item(Items.thorium, 4, Items.sand, 10))
        Blocks.phaseWeaver.consumePower(5.0)
        Blocks.phaseWeaver.itemCapacity = 30

        Blocks.surgeSmelter = GenericCrafter("surge-smelter")
        Blocks.surgeSmelter.setRequirements(Category.crafting, ItemStack.with_item(Items.silicon, 80, Items.lead, 80, Items.thorium, 70))
        # Blocks.surgeSmelter.craftEffect = Fx.smeltsmoke
        Blocks.surgeSmelter.outputItem = ItemStack(Items.surgeAlloy, 1)
        Blocks.surgeSmelter.craftTime = 75.0
        Blocks.surgeSmelter.size = 3
        Blocks.surgeSmelter.hasPower = True
        Blocks.surgeSmelter.itemCapacity = 20
        # Blocks.surgeSmelter.drawer = DrawMulti(DrawDefault(), DrawFlame())
        Blocks.surgeSmelter.consumePower(4.0)
        Blocks.surgeSmelter.consumeItems(ItemStack.with_item(Items.copper, 3, Items.lead, 4, Items.titanium, 2, Items.silicon, 3))

        Blocks.cryofluidMixer = GenericCrafter("cryofluid-mixer")
        Blocks.cryofluidMixer.setRequirements(Category.crafting, ItemStack.with_item(Items.lead, 65, Items.silicon, 40, Items.titanium, 60))
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
        Blocks.pyratiteMixer.setRequirements(Category.crafting, ItemStack.with_item(Items.copper, 50, Items.lead, 25))
        Blocks.pyratiteMixer.hasItems = True
        Blocks.pyratiteMixer.hasPower = True
        Blocks.pyratiteMixer.outputItem = ItemStack(Items.pyratite, 1)
        Blocks.pyratiteMixer.envEnabled |= Env.space
        Blocks.pyratiteMixer.size = 2
        Blocks.pyratiteMixer.consumePower(0.20)
        Blocks.pyratiteMixer.consumeItems(ItemStack.with_item(Items.coal, 1, Items.lead, 2, Items.sand, 2))

        Blocks.blastMixer = GenericCrafter("blast-mixer")
        Blocks.blastMixer.setRequirements(Category.crafting, ItemStack.with_item(Items.lead, 30, Items.titanium, 20))
        Blocks.blastMixer.hasItems = True
        Blocks.blastMixer.hasPower = True
        Blocks.blastMixer.outputItem = ItemStack(Items.blastCompound, 1)
        Blocks.blastMixer.size = 2
        Blocks.blastMixer.envEnabled |= Env.space
        Blocks.blastMixer.consumeItems(ItemStack.with_item(Items.pyratite, 1, Items.sporePod, 1))
        Blocks.blastMixer.consumePower(0.40)

        Blocks.melter = GenericCrafter("melter")
        Blocks.melter.setRequirements(Category.crafting, ItemStack.with_item(Items.copper, 30, Items.lead, 35, Items.graphite, 45))
        Blocks.melter.health = 200
        Blocks.melter.outputLiquid = LiquidStack(Liquids.slag, 12.0 / 60.0)
        Blocks.melter.craftTime = 10.0
        Blocks.melter.hasLiquids = True
        Blocks.melter.hasPower = True
        # Blocks.melter.drawer = DrawMulti(DrawRegion("-bottom"), DrawLiquidTile(), DrawDefault())
        Blocks.melter.consumePower(1.0)
        Blocks.melter.consumeItem(Items.scrap, 1)
        
        