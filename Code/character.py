from alliance import Alliance

class Character:
    def __init__(self, aname, amap, ainfo, aschedule, alliancenumber):
        self.name = aname
        self.mapk = amap
        self.info = ainfo
        self.schedule = aschedule
        self.alliancevalue = alliancenumber
        
    def add_info(self, fromc, factindex, rating = None):
        self.info.addcontent(self, fromc, factindex, rating)
        
    def unlock_map(self, area, accessible = 0):
        self.mapk.unlockarea(area, accessible)
    
    def get_location(self, timeint):
        return self.schedule.getlocation(timeint)
    
    def get_attendance(self, timeint):
        return self.schedule.getattendance(timeint)
    
    def update_schedule(self, timeint, area):
        if area in self.mapk.access: 
            self.schedule.updateschedule(timeint, area)
        else:
            print("a chartacter went where they do not have access and this angry game dev bunny cat is going to eat this character..alive!!!!!")
            
    def get_alliance(self):
        return Alliance.getalliance(self.alliancevalue)
        
    def update_alliance(self, value):
        self.alliancevalue += value
    
    def reset_alliance(self, value):
        self.alliancevalue = value
  
    

class Player(Character):
    pass

class Npc(Character):
    def __init__(self, aname, amap, ainfo, aschedule, aalliance):
        super(Npc, self).__init__(aname, amap, ainfo, aschedule, aalliance)
        self.relation = None
    
    def assign_relation(self, drelation):
        self.relation = drelation
            
    def get_relation(self, char):
        return self.relation.getrelation(char)
        
    def update_relation(self, char, value):
        self.relation.updaterelation(char, value)
        
    def reset_relation(self,char,value):
        self.relation.resetrelation(char, value)
 
    
    