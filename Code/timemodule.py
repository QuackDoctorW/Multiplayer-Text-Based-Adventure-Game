from enum import Enum


class Timeinfo(Enum):
    Night0 = 0
    Day1 = 100
    Day2 = 200
    Day3 = 300
    Finalday = 400
    Morning = 10
    Afternoon = 20
    Night = 30
    Eventslot1 = 1
    Eventslot2 = 2
    Eventslot3 = 3

class Time:
    def __init__(self, timesequence):
        self.timeline = timesequence
        self.current = self.timeline[0]
        self.past = None
    
    def timepass(self):
        self.past = self.current 
        self.timeline = self.timeline[1:]
        self.current = self.timeline[0]
        
    def readtime(self, timeint):
        day = round(timeint,-2) #round always rounds down, since we have 1,2,3
        segment = round(timeint,-1)%100
        slot = timeint%10
        return Timeinfo(day).name, Timeinfo(segment).name, Timeinfo(slot).name
    


    
    
