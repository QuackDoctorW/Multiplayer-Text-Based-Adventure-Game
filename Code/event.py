from character import Player
class Event:
    def __init__(self, index, eventdict):
        self.event = eventdict[index][1] 
        self.requirement = eventdict[index][0]
        self.eventdict = eventdict
   
      
    def run_event(self, timeint, charlist):
        #under process, keeps trackers if any new events are being ran, so returns 1 or 0
        if self.requirement.check_req(timeint, charlist, self.eventdict):
            self.requirement.completed = True
            playerlist = []
            npclist = []
            for char in charlist:
                if char.get_location(timeint) == self.requirement.location:
                    if isinstance(char, Player):    
                        playerlist.append(char)
                    else:
                        npclist.append(char)
            if playerlist:
                self.event.run_player_decision(playerlist, npclist)
            else:
                self.event.run_npc_decision(npclist)
            return 1
        else:
            return 0
    
    
    
