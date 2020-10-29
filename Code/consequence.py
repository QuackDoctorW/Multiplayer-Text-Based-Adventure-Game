class Consequence:
    def __init__(self, tfactindex, talliance, trelation, tlocknown, tlocaccess, tschedule):
        self.indexchg = tfactindex #((speaker,1),(speaker,3))
        self.alliancechg = talliance #(Alliance, change in val)
        self.relationchg = trelation #(char, change in val)
        self.locknownchg = tlocknown #(place1,place2,place3)
        self.locaccesschg = tlockaccess #(place1,place2)
        self.scheudlechg = tschedule #(timeint, location)
        #Default None, dictionary with key as char object, list of tuples being changed
        #[charobj]:(factindexes),(alliance),(relation),(locationsknown),(locationunlocked),(schedulechange)        
    
    def make_npc_changes(npc):
        pass
    
    def make_player_changes(player):
        pass
        
        
        
