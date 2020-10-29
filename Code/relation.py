from enum import Enum

class Relationinfo(Enum):
    myself = (1000,10000)
    soulmate = (51,999)
    friendly = (11,50)
    neturalplus = (0,10)
    neutralminus = (-10,-1)
    opposed = (-50,-11)
    nemesis = (-51,10000)
    
    def relation_multiplier(self):
        if self == Relationinfo.myself:
            return 100        
        if self == Relationinfo.soulmate:
            return 15
        elif self == Relationinfo.friendly:
            return 7
        elif self == Relationinfo.neutralplus:
            return 5
        elif self == Relationinfo.neutralminus:
            return 4
        elif self == Relationinfo.opposed:
            return 2
        elif self == Relationinfo.nemisis:
            return 1


class Relation:
    def __init__(self, drelation):
        self.relation = drelation
        
    def getrelation(self, char):
        for state in Relationinfo:
            if self.relation[char] >= state.value[0] and self.relation[char] <= state.value[1]:
                return state
    
    def resetrelation(self, char, value):
        self.relation[char] = value
    
    def updaterelation(self, char, value):
        self.relation[char] += value
    
