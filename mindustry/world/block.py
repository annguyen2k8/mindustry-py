from typing import *

from ..graphics import *
from ..type import *
from .meta import *

class Block:
    name: str
    # If true, buildings have an ItemModule
    hasItems: bool
    # If true, buildings have a LiquidModule.
    hasLiquids: bool
    # If true, buildings have a PowerModule.
    hasPower: bool
    # Flag for determining whether this block outputs liquid somewhere; used for connections.
    outputsLiquid: bool = False
    # Used by certain power blocks (nodes) to flag as non-consuming of power. True by default, even if this block has no power.
    consumesPower: bool = True
    # If true, this block is a generator that can produce power.
    outputsPower: bool = False
    # If false, power nodes cannot connect to this block.
    connectedPower: bool = True
    # If true, this block can conduct power like a cable.
    conductivePower: bool = False
    # If true, this block can output payloads; affects blending.
    outputsPayload: bool = False
    # If true, payloads will attempt to move into this block.
    acceptsPayload: bool = False
    # Visual flag use for blending of certain transportation blocks.
    acceptsItems: bool = False
    # If true, all item capacities of this block are separate instead of pooled as one number.
    separateItemCapacity: bool = False
    # maximum items this block can carry (usually, this is per-type of item)
    itemCapacity: int = 10
    # maximum total liquids this block can carry if hasLiquids = true
    liquidCapacity: float = 10.0
    # higher numbers increase liquid output speed; TODO remove and replace with better liquids system
    liquidPressure: float = 1.0
    # If true, this block outputs to its facing direction, when applicable.
    # Used for blending calculations.
    outputFacing: bool = True
    # if true, this block does not accept input from the sides (used for armored conveyors)
    noSideBlend: bool = False
    # whether to display flow rate
    displayFlow: bool = True
    # whether this block is visible in the editor
    inEditor: bool = True
    # the last configuration value applied to this block.
    lastConfig: Optional[object] = None
    # whether to save the last config and apply it to newly placed blocks
    saveConfig: bool = False
    # whether to allow copying the config through middle click
    copyConfig: bool = True
    # if true, double-tapping this configurable block clears configuration.
    clearOnDoubleTap: bool = False
    # whether this block has a tile entity that updates
    update: bool
    # whether this block has health and can be destroyed
    destructible: bool
    # whether unloaders work on this block
    unloadable: bool = True
    # if true, this block acts a duct and will connect to armored ducts from the side.
    isDuct: bool = False
    # whether units can resupply by taking items from this block
    allowResupply: bool = False
    # whether this is solid
    solid: bool
    # whether this block CAN be solid.
    solidifes: bool
    # if true, this counts as a non-solid block to this team.
    teamPassable: bool
    # if true, this block cannot be hit by bullets unless explicitly targeted.
    underBullets: bool
    # whether this is rotatable
    rotate: bool
    # if rotate is true and this is false, the region won't rotate when drawing
    rotateDraw: bool = True
    # if rotate = false and this is true, rotation will be locked at 0 when placing (default); advanced use only
    lockRotation: bool = True
    # if true, schematic flips with this block are inverted.
    invertFlip: bool = False
    # number of different variant regions to use
    variants: int = 0
    # whether to draw a rotation arrow - this does not apply to lines of blocks
    drawArrow: bool = True
    # whether to draw the team corner by default
    drawTeamOverlay: bool = True
    # for static blocks only: if true, tile data() is saved in world data.
    saveData: bool
    # whether you can break this with rightclick
    breakable: bool
    # whether to add this block to brokenblocks
    rebuildable: bool = True
    # if true, this logic-related block can only be used with privileged processors (or is one itself)
    privileged: bool = False
    # whether this block can only be placed on water
    requiresWater: bool = False
    # whether this block can be placed on any liquids, anywhere
    placeableLiquid: bool = False
    # whether this block can be placed directly by the player via PlacementFragment
    placeablePlayer: bool = True
    # whether this floor can be placed on.
    placeableOn: bool = True
    # whether this block has insulating properties.
    insulated: bool = False
    # whether the sprite is a full square.
    squareSprite: bool = True
    # whether this block absorbs laser attacks.
    absorbLasers: bool = False
    # if false, the status is never drawn
    enableDrawStatus: bool = True
    # whether to draw disabled status
    drawDisabled: bool = True
    # whether to automatically reset enabled status after a logic block has not interacted for a while.
    autoResetEnabled: bool = True
    # if true, the block stops updating when disabled
    noUpdateDisabled: bool = False
    # if true, this block updates when it's a payload in a unit.
    updateInUnits: bool = True
    # if true, this block updates in payloads in units regardless of the experimental game rule
    alwaysUpdateInUnits: bool = False
    # Whether to use this block's color in the minimap. Only used for overlays.
    useColor: bool = True
    # item that drops from this block, used for drills
    itemDrop: Optional[Item] = None
    # if true, this block cannot be mined by players. useful for annoying things like sand.
    playerUnmineable: bool = False
    # Array of affinities to certain things.
    attributes: set[Attribute] = set()
    # Health per square tile that this block occupies; essentially, this is multiplied by size * size. Overridden if health is > 0. If <0, the default is 40.
    scaledHealth: float = -1
    # building health; -1 to use scaledHealth
    health: int = -1
    # damage absorption, similar to unit armor
    armor: float = 0.0
    # base block explosiveness
    baseExplosiveness: float = 0.0
    # bullet that this block spawns when destroyed
    # destroyBullet: Optional[BulletType] = None
    # if true, destroyBullet is spawned on the block's team instead of Derelict team
    destroyBulletSameTeam: bool = False
    # liquid used for lighting
    # lightLiquid: Optional[Liquid]
    # whether cracks are drawn when this block is damaged
    drawCracks: bool = True
    # whether rubble is created when this block is destroyed
    createRubble: bool = True
    # whether this block can be placed on edges of liquids.
    floating: bool = False
    # multiblock size
    size: int = 1
    # multiblock offset
    offset: float = 0.0
    # offset for iteration (internal use only)
    sizeOffset: int = 0
    # Clipping size of this block. Should be as large as the block will draw.
    clipSize: float = -1.0
    # When placeRangeCheck is enabled, this is the range checked for enemy blocks.
    placeOverlapRange: float = 50.0
    # Multiplier of damage dealt to this block by tanks. Does not apply to crawlers.
    crushDamageMultiplier: float = 1.0
    # Max of timers used.
    timers: int = 0
    # Cache layer. Only used for 'cached' rendering.
    cacheLayer: CacheLayer = CacheLayer.normal
    # Special flag; if false, floor will be drawn under this block even if it is cached.
    fillsTile: bool = True
    # If true, this block can be covered by darkness / fog even if synthetic.
    forceDark: bool = False
    # whether this block can be replaced in all cases
    alwaysReplace: bool = False
    # if false, this block can never be replaced.
    replaceable: bool = True
    # The block group. Unless {@link #canReplace} is overridden, blocks in the same group can replace each other.
    # group: BlockGroup = BlockGroup.none
    # List of block flags. Used for AI indexing.
    flags: set[BlockFlag] = set()
    # Targeting priority of this block, as seen by enemies.
    # priority: float = TargetPriority.base
    # How much this block affects the unit cap by.
    # The block flags must contain unitModifier in order for this to work.
    unitCapModifier: int = 0
    # Whether the block can be tapped and selected to configure.
    configurable: bool
    # If true, this building can be selected like a unit when commanding.
    commandable: bool
    # If true, the building inventory can be shown with the config.
    allowConfigInventory: bool = True
    # Defines how large selection menus, such as that of sorters, should be.
    selectionRows: int = 5
    selectionColumns: int = 4
    # If true, this block can be configured by logic.
    logicConfigurable: bool = False
    # Whether this block consumes touchDown events when tapped.
    consumesTap: bool
    # Whether to draw the glow of the liquid for this block, if it has one.
    drawLiquidLight: bool = True
    # Environmental flags that are *all* required for this block to function. 0 = any environment
    envRequired: int = 0
    # The environment flags that this block can function in. If the env matches any of these, it will be enabled.
    envEnabled: int = Env.terrestrial
    # The environment flags that this block *cannot* function in. If the env matches any of these, it will be *disabled*.
    envDisabled: int = 0
    # Whether to periodically sync this block across the network.
    sync: bool
    # Whether this block uses conveyor-type placement mode.
    conveyorPlacement: bool
    # If false, diagonal placement (ctrl) for this block is not allowed.
    allowDiagonal: bool = True
    # Whether to swap the diagonal placement modes.
    swapDiagonalPlacement: bool
    # Build queue priority in schematics.
    schematicPriority: int = 0
    # The color of this block when displayed on the minimap or map preview.
    # Do not set manually! This is overridden when loading for most blocks.
    mapColor: Color = Color(0, 0, 0, 1)
    # Whether this block has a minimap color.
    hasColor: bool = False
    # Whether units target this block.
    targetable: bool = True
    # If true, this block attacks and is considered a turret in the indexer. Building must implement Ranged.
    attacks: bool = False
    # If true, this block is mending-related and can be suppressed with special units/missiles.
    suppressable: bool = False
    # Whether the overdrive core has any effect on this block.
    canOverdrive: bool = True
    # Outlined icon color.
    outlineColor: Color = Color.valueOf("404049")
    # Whether any icon region has an outline added.
    outlineIcon: bool = False
    # Outline icon radius.
    outlineRadius: int = 4
    # Which of the icon regions gets the outline added. Uses last icon if <= 0.
    outlinedIcon: int = -1
    # Whether this block has a shadow under it.
    hasShadow: bool = True
    # If true, a custom shadow (name-shadow) is drawn under this block.
    customShadow: bool = False
    # Should the sound made when this block is built change in pitch.
    placePitchChange: bool = True
    # Should the sound made when this block is deconstructed change in pitch.
    breakPitchChange: bool = True
    # Sound made when this block is built.
    # placeSound: Sound = Sounds.place
    # Sound made when this block is deconstructed.
    # breakSound: Sound = Sounds.breaks
    # Sounds made when this block is destroyed.
    # destroySound: Sound = Sounds.boom
    # How reflective this block is.
    albedo: float = 0.0
    # Environmental passive light color.
    lightColor: Color = Colors.white
    # Whether this environmental block passively emits light.
    # Does not change behavior for non-environmental blocks, but still updates clipSize.
    emitLight: bool = False
    # Radius of the light emitted by this block.
    lightRadius: float = 60.0
    # How much fog this block uncovers, in tiles. Cannot be dynamic. <= 0 to disable.
    fogRadius: int = -1
    # The sound that this block makes while active. One sound loop. Do not overuse.
    # loopSound: Sound = Sounds.none
    # Active sound base volume.
    loopSoundVolume: float = 0.5
    # The sound that this block makes while idle. Uses one sound loop for all blocks.
    # ambientSound: Sound = Sounds.none
    # Idle sound base volume.
    ambientSoundVolume: float = 0.05
    # Cost of constructing this block.
    requirements: List[ItemStack] = []
    # Category in place menu.
    # category: Category = Category.distribution
    # Time to build this block in ticks; do not modify directly!
    buildCost: float = 20.0
    # Whether this block is visible and can currently be built.
    # buildVisibility: BuildVisibility = BuildVisibility.hidden
    # Multiplier for speed of building this block.
    buildCostMultiplier: float = 1.0
    # Build completion at which deconstruction finishes.
    deconstructThreshold: float = 0.0
    # If true, this block deconstructs immediately. Instant deconstruction implies no resource refund.
    instantDeconstruct: bool = False
    # Effect for placing the block. Passes size as rotation.
    # placeEffect: Effect = Fx.placeBlock
    # Effect for breaking the block. Passes size as rotation.
    # breakEffect: Effect = Fx.breakBlock
    # Effect for destroying the block.
    # destroyEffect: Effect = Fx.dynamicExplosion
    # Multiplier for cost of research in tech tree.
    researchCostMultiplier: float = 1.0
    # Cost multipliers per-item.
    # researchCostMultipliers: ObjectFloatMap[Item] = ObjectFloatMap()
    # Override for research cost. Uses multipliers above and building requirements if not set.
    researchCost: Optional[List[ItemStack]] = None
    # Whether this block has instant transfer.
    instantTransfer: bool = False
    # Whether you can rotate this block after it is placed.
    quickRotate: bool = True
    # Main subclass. Non-anonymous.
    subclass: Optional[Type] = None
    # Scroll position for certain blocks.
    selectScroll: float
    # Building that is created for this block. Initialized in init() via reflection. Set manually if modded.
    # buildType: Optional[Prov[Building]] = None
    # Configuration handlers by type.
    # configurations: ObjectMap[Type, Cons2] = ObjectMap()
    # Consumption filters.
    itemFilter: List[bool] = []
    liquidFilter: List[bool] = []
    # Array of consumers used by this block. Only populated after init().
    # consumers: List[Consume] = []
    # optionalConsumers: List[Consume] = []
    # nonOptionalConsumers: List[Consume] = []
    # updateConsumers: List[Consume] = []
    # Set to true if this block has any consumers in its array.
    hasConsumers: bool
    # The single power consumer, if applicable.
    # consPower: Optional[ConsumePower] = None
    # Map of bars by name.
    # barMap: OrderedMap[str, Func[Building, Bar]] = OrderedMap()
    # List for building up consumption before init().
    # consumeBuilder: Seq[Consume] = Seq()
    # Regions indexes from icons() that are rotated. If either of these is not -1, other regions won't be rotated in ConstructBlocks.
    # regionRotated1: int = -1
    # regionRotated2: int = -1
    # region: TextureRegion
    # editorIcon: TextureRegion
    # customShadowRegion: TextureRegion
    # teamRegion: TextureRegion
    # teamRegions: List[TextureRegion] = []
    # variantRegions: List[TextureRegion] = []
    # variantShadowRegions: List[TextureRegion] = []
    # tempTiles: Seq[Tile] = Seq()
    # tempBuilds: Seq[Building] = Seq()
    # Dump timer ID.
    timerDump: int = timers + 1
    # How often to try dumping items in ticks, e.g. 5 = 12 times/sec
    dumpTime: int = 5

    def __init__(self, name: str):
        self.name = name