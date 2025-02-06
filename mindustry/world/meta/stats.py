from typing import *

from .stat_value import StatValue
from .stat_cat import StatCat
from .stat import Stat

class Stats:
    useCategories:bool = False
    intialized:bool = False
    timePeriod:float = -1.0
    map_statt:Dict[StatCat, Dict[Stat, List[StatValue]]] = None
    dirty:bool
    
    def __init__(self):
        pass