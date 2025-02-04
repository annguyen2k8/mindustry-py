from mindustry.world.blocks import *
from mindustry.world.meta import *
from mindustry.graphics import *
from mindustry.type import *
from mindustry.vars import *

# from mindustry.world.block import Block

class Blocks:
    # environment
    air = None
    spawn = None
    remove_wall = None
    remove_ore = None
    cliff = None
    deepwater = None
    water = None
    tainted_water = None
    deep_tainted_water = None
    tar = None
    slag = None
    cryofluid = None
    stone = None
    craters = None
    charr = None
    sand = None
    darksand = None
    dirt = None
    mud = None
    ice = None
    snow = None
    darksand_tainted_water = None
    space = None
    empty = None
    dacite = None
    rhyolite = None
    rhyolite_crater = None
    rough_rhyolite = None
    regolith = None
    yellow_stone = None
    red_ice = None
    red_stone = None
    dense_red_stone = None
    arkycite_floor = None
    arkyic_stone = None
    redmat = None
    bluemat = None
    stone_wall = None
    dirt_wall = None
    spore_wall = None
    ice_wall = None
    dacite_wall = None
    spore_pine = None
    snow_pine = None
    pine = None
    shrubs = None
    white_tree = None
    white_tree_dead = None
    spore_cluster = None
    redweed = None
    purbush = None
    yellow_coral = None
    rhyolite_vent = None
    carbon_vent = None
    arkyic_vent = None
    yellow_stone_vent = None
    red_stone_vent = None
    crystalline_vent = None
    regolith_wall = None
    yellow_stone_wall = None
    rhyolite_wall = None
    carbon_wall = None
    red_ice_wall = None
    ferric_stone_wall = None
    beryllic_stone_wall = None
    arkyic_wall = None
    crystalline_stone_wall = None
    red_stone_wall = None
    red_diamond_wall = None
    ferric_stone = None
    ferric_craters = None
    carbon_stone = None
    beryllic_stone = None
    crystalline_stone = None
    crystal_floor = None
    yellow_stone_plates = None
    ice_snow = None
    sand_water = None
    darksand_water = None
    dune_wall = None
    sand_wall = None
    moss = None
    spore_moss = None
    shale = None
    shale_wall = None
    grass = None
    salt = None
    core_zone = None
    # boulders
    shale_boulder = None
    sand_boulder = None
    dacite_boulder = None
    boulder = None
    snow_boulder = None
    basalt_boulder = None
    carbon_boulder = None
    ferric_boulder = None
    beryllic_boulder = None
    yellow_stone_boulder = None
    arkyic_boulder = None
    crystal_cluster = None
    vibrant_crystal_cluster = None
    crystal_blocks = None
    crystal_orbs = None
    crystalline_boulder = None
    red_ice_boulder = None
    rhyolite_boulder = None
    red_stone_boulder = None
    metal_floor = None
    metal_floor_damaged = None
    metal_floor2 = None
    metal_floor3 = None
    metal_floor4 = None
    metal_floor5 = None
    basalt = None
    magmarock = None
    hotrock = None
    snow_wall = None
    salt_wall = None
    dark_panel1 = None
    dark_panel2 = None
    dark_panel3 = None
    dark_panel4 = None
    dark_panel5 = None
    dark_panel6 = None
    dark_metal = None
    pebbles = None
    tendrils = None
    # ores
    ore_copper = None
    ore_lead = None
    ore_scrap = None
    ore_coal = None
    ore_titanium = None
    ore_thorium = None
    ore_beryllium = None
    ore_tungsten = None
    ore_crystal_thorium = None
    wall_ore_thorium = None
    # wall ores
    wall_ore_beryllium = None
    graphitic_wall = None
    wall_ore_tungsten = None
    # crafting
    silicon_smelter = None
    silicon_crucible = None
    kiln = None
    graphite_press = None
    plastanium_compressor = None
    multi_press = None
    phase_weaver = None
    surge_smelter = None
    pyratite_mixer = None
    blast_mixer = None
    cryofluid_mixer = None
    melter = None
    separator = None
    disassembler = None
    spore_press = None
    pulverizer = None
    incinerator = None
    coal_centrifuge = None
    # crafting - erekir
    silicon_arc_furnace = None
    electrolyzer = None
    oxidation_chamber = None
    atmospheric_concentrator = None
    electric_heater = None
    slag_heater = None
    phase_heater = None
    heat_redirector = None
    small_heat_redirector = None
    heat_router = None
    slag_incinerator = None
    carbide_crucible = None
    slag_centrifuge = None
    surge_crucible = None
    cyanogen_synthesizer = None
    phase_synthesizer = None
    heat_reactor = None
    # sandbox
    power_source = None
    power_void = None
    item_source = None
    item_void = None
    liquid_source = None
    liquid_void = None
    payload_source = None
    payload_void = None
    illuminator = None
    heat_source = None
    # defense
    copper_wall = None
    copper_wall_large = None
    titanium_wall = None
    titanium_wall_large = None
    plastanium_wall = None
    plastanium_wall_large = None
    thorium_wall = None
    thorium_wall_large = None
    door = None
    door_large = None
    phase_wall = None
    phase_wall_large = None
    surge_wall = None
    surge_wall_large = None
    # walls - erekir
    beryllium_wall = None
    beryllium_wall_large = None
    tungsten_wall = None
    tungsten_wall_large = None
    blast_door = None
    reinforced_surge_wall = None
    reinforced_surge_wall_large = None
    carbide_wall = None
    carbide_wall_large = None
    shielded_wall = None
    mender = None
    mend_projector = None
    overdrive_projector = None
    overdrive_dome = None
    force_projector = None
    shock_mine = None
    scrap_wall = None
    scrap_wall_large = None
    scrap_wall_huge = None
    scrap_wall_gigantic = None
    thruster = None
    # defense - erekir
    radar = None
    build_tower = None
    regen_projector = None
    barrier_projector = None
    shockwave_tower = None
    # campaign only
    shield_projector = None
    large_shield_projector = None
    shield_breaker = None
    # transport
    conveyor = None
    titanium_conveyor = None
    plastanium_conveyor = None
    armored_conveyor = None
    distributor = None
    junction = None
    item_bridge = None
    phase_conveyor = None
    sorter = None
    inverted_sorter = None
    router = None
    overflow_gate = None
    underflow_gate = None
    mass_driver = None
    # transport - alternate
    duct = None
    armored_duct = None
    duct_router = None
    overflow_duct = None
    underflow_duct = None
    duct_bridge = None
    duct_unloader = None
    surge_conveyor = None
    surge_router = None
    unit_cargo_loader = None
    unit_cargo_unload_point = None
    # liquid
    mechanical_pump = None
    rotary_pump = None
    impulse_pump = None
    conduit = None
    pulse_conduit = None
    plated_conduit = None
    liquid_router = None
    liquid_container = None
    liquid_tank = None
    liquid_junction = None
    bridge_conduit = None
    phase_conduit = None
    # liquid - reinforced
    reinforced_pump = None
    reinforced_conduit = None
    reinforced_liquid_junction = None
    reinforced_bridge_conduit = None
    reinforced_liquid_router = None
    reinforced_liquid_container = None
    reinforced_liquid_tank = None
    # power
    combustion_generator = None
    thermal_generator = None
    steam_generator = None
    differential_generator = None
    rtg_generator = None
    solar_panel = None
    large_solar_panel = None
    thorium_reactor = None
    impact_reactor = None
    battery = None
    battery_large = None
    power_node = None
    power_node_large = None
    surge_tower = None
    diode = None
    # power - erekir
    turbine_condenser = None
    vent_condenser = None
    chemical_combustion_chamber = None
    pyrolysis_generator = None
    flux_reactor = None
    neoplasia_reactor = None
    beam_node = None
    beam_tower = None
    beam_link = None
    # production
    mechanical_drill = None
    pneumatic_drill = None
    laser_drill = None
    blast_drill = None
    water_extractor = None
    oil_extractor = None
    cultivator = None
    cliff_crusher = None
    large_cliff_crusher = None
    plasma_bore = None
    large_plasma_bore = None
    impact_drill = None
    eruption_drill = None
    # storage
    core_shard = None
    core_foundation = None
    core_nucleus = None
    vault = None
    container = None
    unloader = None
    # storage - erekir
    core_bastion = None
    core_citadel = None
    core_acropolis = None
    reinforced_container = None
    reinforced_vault = None
    # turrets
    duo = None
    scatter = None
    scorch = None
    hail = None
    arc = None
    wave = None
    lancer = None
    swarmer = None
    salvo = None
    fuse = None
    ripple = None
    cyclone = None
    foreshadow = None
    spectre = None
    meltdown = None
    segment = None
    parallax = None
    tsunami = None
    # turrets - erekir
    breach = None
    diffuse = None
    sublimate = None
    titan = None
    disperse = None
    afflict = None
    lustre = None
    scathe = None
    smite = None
    malign = None
    # units
    ground_factory = None
    air_factory = None
    naval_factory = None
    additive_reconstructor = None
    multiplicative_reconstructor = None
    exponential_reconstructor = None
    tetrative_reconstructor = None
    repair_point = None
    repair_turret = None
    # units - erekir
    tank_fabricator = None
    ship_fabricator = None
    mech_fabricator = None
    tank_refabricator = None
    ship_refabricator = None
    mech_refabricator = None
    prime_refabricator = None
    tank_assembler = None
    ship_assembler = None
    mech_assembler = None
    basic_assembler_module = None
    unit_repair_tower = None
    # payloads
    payload_conveyor = None
    payload_router = None
    reinforced_payload_conveyor = None
    reinforced_payload_router = None
    payload_mass_driver = None
    large_payload_mass_driver = None
    small_deconstructor = None
    deconstructor = None
    constructor = None
    large_constructor = None
    payload_loader = None
    payload_unloader = None
    # logic
    message = None
    switch_block = None
    micro_processor = None
    logic_processor = None
    hyper_processor = None
    large_logic_display = None
    logic_display = None
    memory_cell = None
    memory_bank = None
    canvas = None
    reinforced_message = None
    world_processor = None
    world_cell = None
    world_message = None
    world_switch = None
    # campaign
    launch_pad = None
    interplanetary_accelerator = None
    
    @staticmethod
    def load():
        
        # region environment
        
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
            Blocks.metal_floor, Blocks.metal_floor_damaged, Blocks.metal_floor2, Blocks.metal_floor3,
            Blocks.metal_floor4, Blocks.metal_floor5, Blocks.dark_panel1, Blocks.dark_panel2,
            Blocks.dark_panel3, Blocks.dark_panel4, Blocks.dark_panel5, Blocks.dark_panel6
        ]

        for b in blocks:
            b.as_floor().wall = Blocks.dark_metal
        
        pebbles = OverlayFloor('pebbles')
        tendrils = OverlayFloor('tendrils')
        
        # region ore
        
        