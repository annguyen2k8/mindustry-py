from mindustry.world.blocks import *
from mindustry.graphics import *
from mindustry.type import *
from mindustry.vars import *

class Blocks:
    # environment
    air:Block = None
    spawn:Block = None
    remove_wall:Block = None
    remove_ore:Block = None
    cliff:Block = None
    deepwater:Block = None
    water:Block = None
    tainted_water:Block = None
    deep_tainted_water:Block = None
    tar:Block = None
    slag:Block = None
    cryofluid:Block = None
    stone:Block = None
    craters:Block = None
    charr:Block = None
    sand:Block = None
    darksand:Block = None
    dirt:Block = None
    mud:Block = None
    ice:Block = None
    snow:Block = None
    darksand_tainted_water:Block = None
    space:Block = None
    empty:Block = None
    dacite:Block = None
    rhyolite:Block = None
    rhyolite_crater:Block = None
    rough_rhyolite:Block = None
    regolith:Block = None
    yellow_stone:Block = None
    red_ice:Block = None
    red_stone:Block = None
    dense_red_stone:Block = None
    arkycite_floor:Block = None
    arkyic_stone:Block = None
    redmat:Block = None
    bluemat:Block = None
    stone_wall:Block = None
    dirt_wall:Block = None
    spore_wall:Block = None
    ice_wall:Block = None
    dacite_wall:Block = None
    spore_pine:Block = None
    snow_pine:Block = None
    pine:Block = None
    shrubs:Block = None
    white_tree:Block = None
    white_tree_dead:Block = None
    spore_cluster:Block = None
    redweed:Block = None
    purbush:Block = None
    yellow_coral:Block = None
    rhyolite_vent:Block = None
    carbon_vent:Block = None
    arkyic_vent:Block = None
    yellow_stone_vent:Block = None
    red_stone_vent:Block = None
    crystalline_vent:Block = None
    regolith_wall:Block = None
    yellow_stone_wall:Block = None
    rhyolite_wall:Block = None
    carbon_wall:Block = None
    red_ice_wall:Block = None
    ferric_stone_wall:Block = None
    beryllic_stone_wall:Block = None
    arkyic_wall:Block = None
    crystalline_stone_wall:Block = None
    red_stone_wall:Block = None
    red_diamond_wall:Block = None
    ferric_stone:Block = None
    ferric_craters:Block = None
    carbon_stone:Block = None
    beryllic_stone:Block = None
    crystalline_stone:Block = None
    crystal_floor:Block = None
    yellow_stone_plates:Block = None
    ice_snow:Block = None
    sand_water:Block = None
    darksand_water:Block = None
    dune_wall:Block = None
    sand_wall:Block = None
    moss:Block = None
    spore_moss:Block = None
    shale:Block = None
    shale_wall:Block = None
    grass:Block = None
    salt:Block = None
    core_zone:Block = None
    # boulders
    shale_boulder:Block = None
    sand_boulder:Block = None
    dacite_boulder:Block = None
    boulder:Block = None
    snow_boulder:Block = None
    basalt_boulder:Block = None
    carbon_boulder:Block = None
    ferric_boulder:Block = None
    beryllic_boulder:Block = None
    yellow_stone_boulder:Block = None
    arkyic_boulder:Block = None
    crystal_cluster:Block = None
    vibrant_crystal_cluster:Block = None
    crystal_blocks:Block = None
    crystal_orbs:Block = None
    crystalline_boulder:Block = None
    red_ice_boulder:Block = None
    rhyolite_boulder:Block = None
    red_stone_boulder:Block = None
    metal_floor:Block = None
    metal_floor_damaged:Block = None
    metal_floor2:Block = None
    metal_floor3:Block = None
    metal_floor4:Block = None
    metal_floor5:Block = None
    basalt:Block = None
    magmarock:Block = None
    hotrock:Block = None
    snow_wall:Block = None
    salt_wall:Block = None
    dark_panel1:Block = None
    dark_panel2:Block = None
    dark_panel3:Block = None
    dark_panel4:Block = None
    dark_panel5:Block = None
    dark_panel6:Block = None
    dark_metal:Block = None
    pebbles:Block = None
    tendrils:Block = None
    # ores
    ore_copper:Block = None
    ore_lead:Block = None
    ore_scrap:Block = None
    ore_coal:Block = None
    ore_titanium:Block = None
    ore_thorium:Block = None
    ore_beryllium:Block = None
    ore_tungsten:Block = None
    ore_crystal_thorium:Block = None
    wall_ore_thorium:Block = None
    # wall ores
    wall_ore_beryllium:Block = None
    graphitic_wall:Block = None
    wall_ore_tungsten:Block = None
    # crafting
    silicon_smelter:Block = None
    silicon_crucible:Block = None
    kiln:Block = None
    graphite_press:Block = None
    plastanium_compressor:Block = None
    multi_press:Block = None
    phase_weaver:Block = None
    surge_smelter:Block = None
    pyratite_mixer:Block = None
    blast_mixer:Block = None
    cryofluid_mixer:Block = None
    melter:Block = None
    separator:Block = None
    disassembler:Block = None
    spore_press:Block = None
    pulverizer:Block = None
    incinerator:Block = None
    coal_centrifuge:Block = None
    # crafting - erekir
    silicon_arc_furnace:Block = None
    electrolyzer:Block = None
    oxidation_chamber:Block = None
    atmospheric_concentrator:Block = None
    electric_heater:Block = None
    slag_heater:Block = None
    phase_heater:Block = None
    heat_redirector:Block = None
    small_heat_redirector:Block = None
    heat_router:Block = None
    slag_incinerator:Block = None
    carbide_crucible:Block = None
    slag_centrifuge:Block = None
    surge_crucible:Block = None
    cyanogen_synthesizer:Block = None
    phase_synthesizer:Block = None
    heat_reactor:Block = None
    # sandbox
    power_source:Block = None
    power_void:Block = None
    item_source:Block = None
    item_void:Block = None
    liquid_source:Block = None
    liquid_void:Block = None
    payload_source:Block = None
    payload_void:Block = None
    illuminator:Block = None
    heat_source:Block = None
    # defense
    copper_wall:Block = None
    copper_wall_large:Block = None
    titanium_wall:Block = None
    titanium_wall_large:Block = None
    plastanium_wall:Block = None
    plastanium_wall_large:Block = None
    thorium_wall:Block = None
    thorium_wall_large:Block = None
    door:Block = None
    door_large:Block = None
    phase_wall:Block = None
    phase_wall_large:Block = None
    surge_wall:Block = None
    surge_wall_large:Block = None
    # walls - erekir
    beryllium_wall:Block = None
    beryllium_wall_large:Block = None
    tungsten_wall:Block = None
    tungsten_wall_large:Block = None
    blast_door:Block = None
    reinforced_surge_wall:Block = None
    reinforced_surge_wall_large:Block = None
    carbide_wall:Block = None
    carbide_wall_large:Block = None
    shielded_wall:Block = None
    mender:Block = None
    mend_projector:Block = None
    overdrive_projector:Block = None
    overdrive_dome:Block = None
    force_projector:Block = None
    shock_mine:Block = None
    scrap_wall:Block = None
    scrap_wall_large:Block = None
    scrap_wall_huge:Block = None
    scrap_wall_gigantic:Block = None
    thruster:Block = None
    # defense - erekir
    radar:Block = None
    build_tower:Block = None
    regen_projector:Block = None
    barrier_projector:Block = None
    shockwave_tower:Block = None
    # campaign only
    shield_projector:Block = None
    large_shield_projector:Block = None
    shield_breaker:Block = None
    # transport
    conveyor:Block = None
    titanium_conveyor:Block = None
    plastanium_conveyor:Block = None
    armored_conveyor:Block = None
    distributor:Block = None
    junction:Block = None
    item_bridge:Block = None
    phase_conveyor:Block = None
    sorter:Block = None
    inverted_sorter:Block = None
    router:Block = None
    overflow_gate:Block = None
    underflow_gate:Block = None
    mass_driver:Block = None
    # transport - alternate
    duct:Block = None
    armored_duct:Block = None
    duct_router:Block = None
    overflow_duct:Block = None
    underflow_duct:Block = None
    duct_bridge:Block = None
    duct_unloader:Block = None
    surge_conveyor:Block = None
    surge_router:Block = None
    unit_cargo_loader:Block = None
    unit_cargo_unload_point:Block = None
    # liquid
    mechanical_pump:Block = None
    rotary_pump:Block = None
    impulse_pump:Block = None
    conduit:Block = None
    pulse_conduit:Block = None
    plated_conduit:Block = None
    liquid_router:Block = None
    liquid_container:Block = None
    liquid_tank:Block = None
    liquid_junction:Block = None
    bridge_conduit:Block = None
    phase_conduit:Block = None
    # liquid - reinforced
    reinforced_pump:Block = None
    reinforced_conduit:Block = None
    reinforced_liquid_junction:Block = None
    reinforced_bridge_conduit:Block = None
    reinforced_liquid_router:Block = None
    reinforced_liquid_container:Block = None
    reinforced_liquid_tank:Block = None
    # power
    combustion_generator:Block = None
    thermal_generator:Block = None
    steam_generator:Block = None
    differential_generator:Block = None
    rtg_generator:Block = None
    solar_panel:Block = None
    large_solar_panel:Block = None
    thorium_reactor:Block = None
    impact_reactor:Block = None
    battery:Block = None
    battery_large:Block = None
    power_node:Block = None
    power_node_large:Block = None
    surge_tower:Block = None
    diode:Block = None
    # power - erekir
    turbine_condenser:Block = None
    vent_condenser:Block = None
    chemical_combustion_chamber:Block = None
    pyrolysis_generator:Block = None
    flux_reactor:Block = None
    neoplasia_reactor:Block = None
    beam_node:Block = None
    beam_tower:Block = None
    beam_link:Block = None
    # production
    mechanical_drill:Block = None
    pneumatic_drill:Block = None
    laser_drill:Block = None
    blast_drill:Block = None
    water_extractor:Block = None
    oil_extractor:Block = None
    cultivator:Block = None
    cliff_crusher:Block = None
    large_cliff_crusher:Block = None
    plasma_bore:Block = None
    large_plasma_bore:Block = None
    impact_drill:Block = None
    eruption_drill:Block = None
    # storage
    core_shard:Block = None
    core_foundation:Block = None
    core_nucleus:Block = None
    vault:Block = None
    container:Block = None
    unloader:Block = None
    # storage - erekir
    core_bastion:Block = None
    core_citadel:Block = None
    core_acropolis:Block = None
    reinforced_container:Block = None
    reinforced_vault:Block = None
    # turrets
    duo:Block = None
    scatter:Block = None
    scorch:Block = None
    hail:Block = None
    arc:Block = None
    wave:Block = None
    lancer:Block = None
    swarmer:Block = None
    salvo:Block = None
    fuse:Block = None
    ripple:Block = None
    cyclone:Block = None
    foreshadow:Block = None
    spectre:Block = None
    meltdown:Block = None
    segment:Block = None
    parallax:Block = None
    tsunami:Block = None
    # turrets - erekir
    breach:Block = None
    diffuse:Block = None
    sublimate:Block = None
    titan:Block = None
    disperse:Block = None
    afflict:Block = None
    lustre:Block = None
    scathe:Block = None
    smite:Block = None
    malign:Block = None
    # units
    ground_factory:Block = None
    air_factory:Block = None
    naval_factory:Block = None
    additive_reconstructor:Block = None
    multiplicative_reconstructor:Block = None
    exponential_reconstructor:Block = None
    tetrative_reconstructor:Block = None
    repair_point:Block = None
    repair_turret:Block = None
    # units - erekir
    tank_fabricator:Block = None
    ship_fabricator:Block = None
    mech_fabricator:Block = None
    tank_refabricator:Block = None
    ship_refabricator:Block = None
    mech_refabricator:Block = None
    prime_refabricator:Block = None
    tank_assembler:Block = None
    ship_assembler:Block = None
    mech_assembler:Block = None
    basic_assembler_module:Block = None
    unit_repair_tower:Block = None
    # payloads
    payload_conveyor:Block = None
    payload_router:Block = None
    reinforced_payload_conveyor:Block = None
    reinforced_payload_router:Block = None
    payload_mass_driver:Block = None
    large_payload_mass_driver:Block = None
    small_deconstructor:Block = None
    deconstructor:Block = None
    constructor:Block = None
    large_constructor:Block = None
    payload_loader:Block = None
    payload_unloader:Block = None
    # logic
    message:Block = None
    switch_block:Block = None
    micro_processor:Block = None
    logic_processor:Block = None
    hyper_processor:Block = None
    large_logic_display:Block = None
    logic_display:Block = None
    memory_cell:Block = None
    memory_bank:Block = None
    canvas:Block = None
    reinforced_message:Block = None
    world_processor:Block = None
    world_cell:Block = None
    world_message:Block = None
    world_switch:Block = None
    # campaign
    launch_pad:Block = None
    interplanetary_accelerator:Block = None
    
    @staticmethod
    def load():
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
        Blocks.hotrock.lightColor = Color.orange.cpy().set_a(0.15)

        Blocks.magmarock = Floor("magmarock")
        Blocks.magmarock.attributes.set(Attribute.heat, 0.75)
        Blocks.magmarock.attributes.set(Attribute.water, -0.75)
        Blocks.magmarock.blendGroup = Blocks.basalt
        Blocks.magmarock.emitLight = True
        Blocks.magmarock.lightRadius = 50.0
        Blocks.magmarock.lightColor = Color.orange.cpy().set_a(0.3)

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
        
        