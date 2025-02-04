class Layer:
    # min layer
    min:float =-11

    # background, which may be planets or an image or nothing at all
    background:float =-10

    # floor tiles
    floor:float =0

    # scorch marks on the floor
    scorch:float =10

    # things such as spent casings or rubble
    debris:float =20

    # stuff under blocks, like connections of conveyors/conduits
    blockUnder:float =29.5

    # base block layer - most blocks go here
    block:float =30

    # layer for cracks over blocks, batched to prevent excessive texture swaps
    blockCracks:float =30 + 0.1

    # some blocks need to draw stuff after cracks
    blockAfterCracks:float =30 + 0.2

    # informal layer used for additive blending overlay, grouped together to reduce draw calls
    blockAdditive:float =31

    # props such as boulders
    blockProp:float =32

    # things drawn over blocks (intermediate layer)
    blockOver:float =35

    # blocks currently in progress *shaders used*
    blockBuilding:float =40

    # turrets
    turret:float =50

    # special layer for turret additive blending heat stuff
    turretHeat:float =50.1

    # ground units
    groundUnit:float =60

    # power lines
    power:float =70

    # certain multi-legged units
    legUnit:float =75

    # darkness over block clusters
    darkness:float =80

    # building plans
    plans:float =85

    # flying units (low altitude)
    flyingUnitLow:float =90

    # bullets *bloom begin*
    bullet:float =100

    # effects *bloom end*
    effect:float =110

    # flying units
    flyingUnit:float =115

    # overlaid UI, like block config guides
    overlayUI:float =120

    # build beam effects
    buildBeam:float =122

    # shield effects
    shields:float =125

    # weather effects, e.g. rain and snow
    weather:float =130

    # light rendering *shaders used*
    light:float =140

    # names of players in the game
    playerName:float =150

    # fog of war effect, if applicable
    fogOfWar:float =155

    # space effects, currently only the land and launch effects
    space:float =160

    # the end of all layers
    end:float =200

    # things after pixelation - used for text
    endPixeled:float =210

    # max layer
    max:float =220