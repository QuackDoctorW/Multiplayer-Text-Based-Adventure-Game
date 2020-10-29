class Decision:
    def __init__(self, startnode, aname:str = None): #([2,3,4] <- connected to, ["do this", "do that", "do nothing"], speaker, picture, string, consequences-a dict,can be None)
        self.start = startnode
        self.graph = {0: startnode}
        self.name = aname
    
    def add_node(self, index, newnode): #single direction graph
        self.graph[index] = newnode

    def get_indexes(self,nodeindex):
        return self.graph[nodeindex][0]
    
    def get_options(self,nodeindex):
        return self.graph[nodeindex][1]      
    
    def get_speaker(self,nodeindex):
        return self.graph[nodeindex][2]
    
    def get_display(self,nodeindex):
        return self.graph[nodeindex][3]
    
    def get_string(self,nodeindex):
        return self.graph[nodeindex][4]
    
    def run_player_decision(self, playerlist, npclist):
        curr_index = 0
        while True:
            for player in playerlist:
                print(self.get_display(curr_index), self.get_speaker(curr_index).name, self.get_string(curr_index))
                self.process_consequence(curr_index, player, npclist)
                if self.get_indexes(curr_index) != []:
                    chosen_index = int(input(str(self.get_indexes(curr_index)) + str(self.get_options(curr_index)))) #click on button to choose the new node index
                    print(player.name, " chose", chosen_index)
                else:
                    return 
            curr_index = chosen_index # it's implied chosen index should result in the same current index for both players
    
    def run_npc_decision(self, npclist):
        curr_index = 0
        while True:
            self.process_consequence(curr_index, None, npclist)
            if self.get_indexes(curr_index):
                curr_index = self.event.get_indexes(curr_index)[-1]
            else:
                break
    
    def process_consequence(self, nodeindex, player, npclist): #Default None, dictionary with key as char object, list of tuples being changed - 
        #[charobj]: consequence object
        #a player consequence is denoted as string "Player"
        consequences = self.graph[nodeindex][-1]
        if consequences != None:
            for achar in consequences:
                if achar == "Player":
                    if player != None: #player only changes
                        consequences[achar].make_player_changes(player)
                elif achar == "Audience":
                    for npc in npclist: 
                        if npc not in consequences: #audience is an npc that's not required, but may happen to be there too, still should be influenced by event
                            consequences[achar].make_npc_changes(npc)                    
                else:
                    consequences[achar].make_npc_changes(achar)    
        
