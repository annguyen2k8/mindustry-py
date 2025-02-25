from __future__ import annotations

from mindustry.type import *

class StatusEffects:
    none:StatusEffect
    burning:StatusEffect
    freezing:StatusEffect
    unmoving:StatusEffect
    slow:StatusEffect
    fast:StatusEffect
    wet:StatusEffect
    muddy:StatusEffect
    melting:StatusEffect
    sapped:StatusEffect
    tarred:StatusEffect
    overdrive:StatusEffect
    overclock:StatusEffect
    shielded:StatusEffect
    shocked:StatusEffect
    blasted:StatusEffect
    corroded:StatusEffect
    boss:StatusEffect
    sporeSlowed:StatusEffect
    disarmed:StatusEffect
    electrified:StatusEffect
    invincible:StatusEffect
    dynamic:StatusEffect

    @staticmethod
    def load() :
        StatusEffects.none = StatusEffect("none")
        StatusEffects.burning = StatusEffect("burning")
        StatusEffects.freezing = StatusEffect("freezing")
        StatusEffects.unmoving = StatusEffect("unmoving")
        StatusEffects.slow = StatusEffect("slow")
        StatusEffects.fast = StatusEffect("fast")
        StatusEffects.wet = StatusEffect("wet")
        StatusEffects.muddy = StatusEffect("muddy")
        StatusEffects.melting = StatusEffect("melting")
        StatusEffects.sapped = StatusEffect("sapped")
        StatusEffects.electrified = StatusEffect("electrified")
        StatusEffects.spore_slowed = StatusEffect("spore-slowed")
        StatusEffects.tarred = StatusEffect("tarred")
        StatusEffects.overdrive = StatusEffect("overdrive")
        StatusEffects.overclock = StatusEffect("overclock")
        StatusEffects.shielded = StatusEffect("shielded")
        StatusEffects.boss = StatusEffect("boss")
        StatusEffects.shocked = StatusEffect("shocked")
        StatusEffects.blasted = StatusEffect("blasted")
        StatusEffects.corroded = StatusEffect("corroded")
        StatusEffects.disarmed = StatusEffect("disarmed")
        StatusEffects.invincible = StatusEffect("invincible")
        StatusEffects.dynamic = StatusEffect("dynamic")