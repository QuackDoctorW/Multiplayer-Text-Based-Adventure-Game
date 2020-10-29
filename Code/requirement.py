from character import Player

class Requirement:
    def __init__(self, alocation, l_required_event_indexes, required_player_num, l_required_char, d_req_char_fact, d_req_char_relation, d_req_char_alliance, atiming):
        self.location = alocation #required
        self.reqindex = l_required_event_indexes #list, empty or not
        self.reqplayernumber = required_player_num #None, 0 - no player can be here, 1, only one needed, 2, both have to be here; 
        self.reqchar = l_required_char #list, empty or not
        self.reqcharfact = d_req_char_fact #dictionary, wolf: list of factindexes, can be empty list
        self.reqcharrelation = d_req_char_relation #dictionary, wolf: [another required-char2, Relationifo.friendly], note player does not have relation, char don't need an entry in this dictionary
        self.reqcharalliance = d_req_char_alliance #dictionary, wolf: Alliance.sweet, char don't need an entry in this dictionary, can be empty dict
        self.timing = atiming # a timeint, can be None
        self.completed = False
    
    def check_req(self, timeint, charlist, eventdict):
        if self.completed == True:
            return False
        for i in self.reqindex:
            if eventdict[i][0].completed == False:
                return False
        player_count = 0 
        if self.reqplayernumber != None:
            for char in charlist:
                if isinstance(char, Player) and char.get_location(timeint) == self.location:            
                    player_count += 1
            if player_count != self.reqplayernumber:
                return False
        for char in self.reqchar:
            if char.get_location(timeint) != self.location:
                return False
            if char in self.reqcharfact:
                for factindex in self.reqcharfact[char]:
                    if factindex not in char.info.facts and factindex not in char.info.maybes:
                        return False
            if char in self.reqcharrelation:
                if char.get_relation(self.reqcharrelation[char][0]) != self.reqcharrelation[char][1]:
                    return False
            if char in self.reqcharalliance:
                if char.get_alliance() != self.reqcharalliance[char]:
                    return False
        if self.timing != None:
            if self.timing != timeint:
                return False
        return True
