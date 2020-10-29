from timemodule import Time
from character import Player, Npc
from schedule import Schedule
from decision import Decision
from requirement import Requirement
from mapmodule import Map
from info import Info

w1locations = ["Sheep House", "Wolf Den", "Common Area"]
w1time = Time([111, 222, 333, None])
w1factdict = {1: "Meow"}

player1 = Player("Sheep Detective",Map(["Sheep House", "Wolf Den", "Common Area"],["Sheep House", "Common Area"]),Info(w1factdict),
                 Schedule({111: ["Sheep House",1], 222: ["Sheep House",0], 333: ["Common Area",1]}), 10) 
player2 = Player("Country Wolf", Map(["Sheep House", "Wolf Den", "Common Area"],["Wolf Den", "Common Area"]), Info(w1factdict), 
                 Schedule({111: ["Wolf Den",1], 222: ["Wolf Den",0], 333: ["Common Area",1]}), -10)

npc1 = Npc("Stolen Sheep", Map(["Sheep House", "Wolf Den", "Common Area"],["Wolf Den"]), Info(w1factdict),
           Schedule({111: ["Wolf Den",1], 222: ["Wolf Den",1], 333: ["Wolf Den",1]}), 0)
npc2 = Npc("Best Friend Sheep", Map(["Sheep House", "Wolf Den", "Common Area"], ["Sheep House", "Common Area"]),Info(w1factdict),
           Schedule({111: ["Sheep House",1], 222: ["Sheep House",1], 333:["Common Area",1]}), 33)
npc3 = Npc("Big Bad Wolf", Map(["Wolf Den","Wolf Den","Common Area"],["Wolf Den", "Common Area"]), Info(w1factdict), 
           Schedule({111: ["Wolf Den",1], 222: ["Wolf Den",1], 333:["Common Area",1]}), -10)

npc1.assign_relation({player1: 0, player2: 0, npc1: 100, npc2:-100 , npc3:15})
npc2.assign_relation({player1: 0, player2: 0, npc1: -100, npc2: 100, npc3: -15})
npc3.assign_relation({player1: 0, player2: 0, npc1: 100, npc2: -100, npc3: 100})

w1charlist = [player1,player2,npc1,npc2,npc3]
w1players = [player1,player2]
w1npcs = [npc1,npc2,npc3]



w1eventdict = {1:(Requirement("Common Area",[],2,[npc2,npc3],{},{},{},333),
                  Decision(([2,2],["Yes Sweets Plz", "Yes Savoury Plz"], npc3, None, "Which flavour do you prefer?", None) ,"Finish IT"))}
w1eventdict[1][1].add_node(2, ([],[], npc3, None, "Ending1", None))
w1eventdict[1][1].add_node(3, ([],[], npc3, None, "Ending2", None))
    
w1convodict = {npc2:{1:(Requirement("Common Area",[],2,[npc2,npc3],{},{},{},333),
                        Decision(([],[],npc2,None,"End of Convo MUAHAHAHA", None),"Sheep1")),
                     2:(Requirement("Common Area",[],2,[npc2,npc3],{},{},{},333),
                        Decision(([],[],npc2,None,"End of Convo MUAHAHAHA", None),"Sheep2"))                     },
               npc1:{1:(Requirement("Common Area",[],2,[npc2,npc3],{},{},{},333),
                        Decision(([],[],npc1,None,"End of Convo MUAHAHAHA", None),"Wolf 1"))},
               npc3:{1:(Requirement("Common Area",[],2,[npc2,npc3],{},{},{},333),
                        Decision(([],[],npc3,None,"End of Convo MUAHAHAHA", None)))}}





#startnode, aname:str = None): #([2,3,4] <- connected to, ["do this", "do that", "do nothing"], speaker, picture, string, consequences)

#time sequence code:
'''
a = [1,2,3]
timesequence = [31]
for i in a:
    for j in a:
        for k in a:
            timesequence.append(i*100+j*10+k*1)
timesequence.append(411)
timesequence.append(None)
w1time = Time(timesequence)
'''
