class TargetPriority:
    # nobody cares about walls
    walk:float = -2.0
    # transport infrastructure isn't as important as factories
    transport:float = -1.0
    # most blocks
    base:float = 0.0
    # turrets deal damage so they are more important
    turret:float = 1.0
    # core is always the most important thing to destroy
    core:float = 2.0