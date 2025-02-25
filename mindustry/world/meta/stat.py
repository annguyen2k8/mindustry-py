from __future__ import annotations
from typing import *

from .stat_cat import StatCat

class Stat:
    allStat:List[Stat] = []
    
    health:Stat
    armor:Stat
    size:Stat
    displaySize:Stat
    buildTime:Stat
    buildCost:Stat
    memoryCapacity:Stat
    explosiveness:Stat
    flammability:Stat
    radioactivity:Stat
    charge:Stat
    heatCapacity:Stat
    viscosity:Stat
    temperature:Stat
    flying:Stat
    speed:Stat
    buildSpeed:Stat
    mineSpeed:Stat
    mineTier:Stat
    payloadCapacity:Stat
    baseDeflectChance:Stat
    lightningChance:Stat
    lightningDamage:Stat
    abilities:Stat
    canBoost:Stat
    maxUnits:Stat
    damageMultiplier:Stat
    healthMultiplier:Stat
    speedMultiplier:Stat
    reloadMultiplier:Stat
    buildSpeedMultiplier:Stat
    reactive:Stat
    healing:Stat
    immunities:Stat
    itemCapacity:Stat
    itemsMoved:Stat
    launchTime:Stat
    maxConsecutive:Stat
    liquidCapacity:Stat
    powerCapacity:Stat
    powerUse:Stat
    powerDamage:Stat
    powerRange:Stat
    powerConnections:Stat
    basePowerGeneration:Stat
    tiles:Stat
    input:Stat
    output:Stat
    productionTime:Stat
    maxEfficiency:Stat
    drillTier:Stat
    drillSpeed:Stat
    linkRange:Stat
    instructions:Stat
    weapons:Stat
    bullet:Stat
    speedIncrease:Stat
    repairTime:Stat
    repairSpeed:Stat
    range:Stat
    shootRange:Stat
    inaccuracy:Stat
    shots:Stat
    reload:Stat
    targetsAir:Stat
    targetsGround:Stat
    damage:Stat
    ammo:Stat
    ammoCapacity:Stat
    ammoUse:Stat
    shieldHealth:Stat
    cooldownTime:Stat
    moduleTier:Stat
    unitType:Stat
    booster:Stat
    boostEffect:Stat
    affinities:Stat
    opposites:Stat

    def __init__(self, name:str, category:StatCat):
        self.category = category
        self.name = name
        Stat.id = len(self.allStat)
        Stat.allStat.append(self)

Stat.armor = Stat("armor", StatCat.general)
Stat.size = Stat("size", StatCat.general)
Stat.displaySize = Stat("displaySize", StatCat.general)
Stat.buildTime = Stat("buildTime", StatCat.general)
Stat.buildCost = Stat("buildCost", StatCat.general)
Stat.memoryCapacity = Stat("memoryCapacity", StatCat.general)
Stat.explosiveness = Stat("explosiveness", StatCat.general)
Stat.flammability = Stat("flammability", StatCat.general)
Stat.radioactivity = Stat("radioactivity", StatCat.general)
Stat.charge = Stat("charge", StatCat.general)
Stat.heatCapacity = Stat("heatCapacity", StatCat.general)
Stat.viscosity = Stat("viscosity", StatCat.general)
Stat.temperature = Stat("temperature", StatCat.general)
Stat.flying = Stat("flying", StatCat.general)
Stat.speed = Stat("speed", StatCat.general)
Stat.buildSpeed = Stat("buildSpeed", StatCat.general)
Stat.mineSpeed = Stat("mineSpeed", StatCat.general)
Stat.mineTier = Stat("mineTier", StatCat.general)
Stat.payloadCapacity = Stat("payloadCapacity", StatCat.general)
Stat.baseDeflectChance = Stat("baseDeflectChance", StatCat.general)
Stat.lightningChance = Stat("lightningChance", StatCat.general)
Stat.lightningDamage = Stat("lightningDamage", StatCat.general)
Stat.abilities = Stat("abilities", StatCat.general)
Stat.canBoost = Stat("canBoost", StatCat.general)
Stat.maxUnits = Stat("maxUnits", StatCat.general)
Stat.damageMultiplier = Stat("damageMultiplier", StatCat.general)
Stat.healthMultiplier = Stat("healthMultiplier", StatCat.general)
Stat.speedMultiplier = Stat("speedMultiplier", StatCat.general)
Stat.reloadMultiplier = Stat("reloadMultiplier", StatCat.general)
Stat.buildSpeedMultiplier = Stat("buildSpeedMultiplier", StatCat.general)
Stat.reactive = Stat("reactive", StatCat.general)
Stat.healing = Stat("healing", StatCat.general)
Stat.immunities = Stat("immunities", StatCat.general)
Stat.itemCapacity = Stat("itemCapacity", StatCat.items)
Stat.itemsMoved = Stat("itemsMoved", StatCat.items)
Stat.launchTime = Stat("launchTime", StatCat.items)
Stat.maxConsecutive = Stat("maxConsecutive", StatCat.items)
Stat.liquidCapacity = Stat("liquidCapacity", StatCat.liquids)
Stat.powerCapacity = Stat("powerCapacity", StatCat.power)
Stat.powerUse = Stat("powerUse", StatCat.power)
Stat.powerDamage = Stat("powerDamage", StatCat.power)
Stat.powerRange = Stat("powerRange", StatCat.power)
Stat.powerConnections = Stat("powerConnections", StatCat.power)
Stat.basePowerGeneration = Stat("basePowerGeneration", StatCat.power)
Stat.tiles = Stat("tiles", StatCat.crafting)
Stat.input = Stat("input", StatCat.crafting)
Stat.output = Stat("output", StatCat.crafting)
Stat.productionTime = Stat("productionTime", StatCat.crafting)
Stat.maxEfficiency = Stat("maxEfficiency", StatCat.crafting)
Stat.drillTier = Stat("drillTier", StatCat.crafting)
Stat.drillSpeed = Stat("drillSpeed", StatCat.crafting)
Stat.linkRange = Stat("linkRange", StatCat.crafting)
Stat.instructions = Stat("instructions", StatCat.crafting)
Stat.weapons = Stat("weapons", StatCat.function)
Stat.bullet = Stat("bullet", StatCat.function)
Stat.speedIncrease = Stat("speedIncrease", StatCat.function)
Stat.repairTime = Stat("repairTime", StatCat.function)
Stat.repairSpeed = Stat("repairSpeed", StatCat.function)
Stat.range = Stat("range", StatCat.function)
Stat.shootRange = Stat("shootRange", StatCat.function)
Stat.inaccuracy = Stat("inaccuracy", StatCat.function)
Stat.shots = Stat("shots", StatCat.function)
Stat.reload = Stat("reload", StatCat.function)
Stat.targetsAir = Stat("targetsAir", StatCat.function)
Stat.targetsGround = Stat("targetsGround", StatCat.function)
Stat.damage = Stat("damage", StatCat.function)
Stat.ammo = Stat("ammo", StatCat.function)
Stat.ammoCapacity = Stat("ammoCapacity", StatCat.function)
Stat.ammoUse = Stat("ammoUse", StatCat.function)
Stat.shieldHealth = Stat("shieldHealth", StatCat.function)
Stat.cooldownTime = Stat("cooldownTime", StatCat.function)
Stat.moduleTier = Stat("moduleTier", StatCat.function)
Stat.unitType = Stat("unitType", StatCat.function)
Stat.booster = Stat("booster", StatCat.optional)
Stat.boostEffect = Stat("boostEffect", StatCat.optional)
Stat.affinities = Stat("affinities", StatCat.optional)
Stat.opposites = Stat("opposites", StatCat.optional)