from enum import Enum
class Scheduleinfo(Enum):
    required = 1
    optional = 0

class Schedule:
    def __init__(self, dschedule):
        self.agenda = dschedule #key is time int, value is (location,attendance)
    
    def getlocation(self, timeint):
        if timeint == None:
            return None #past time can be none at start of game
        return self.agenda[timeint][0]
        
    def getattendance(self, timeint):
        if timeint == None:
            return None
        return self.agenda[timeint][1]
    
    def updateschedule(self, timeint, area):
        self.agenda[timeint] = (area,0)
        
    

