from enum import Enum

class Alliance(Enum):
    sweet = (6,10000)
    neutral = (-5,5)
    savory = (-10000,-6)
    
    def getalliance(value):
        for faction in Alliance:
            if value >= faction.value[0] and value <= faction.value[1]:
                return faction