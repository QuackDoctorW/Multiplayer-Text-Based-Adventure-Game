'''
to do:
weekend
#implement contradiction decider
#integrate both into rateinfo
#calculate consequences
#test it

Monday
#netowrking + client/server code - python

Wednesday
#develop basic interface  unity/c#
#image holders, add in image

Weekend+following week
#write story
#implement story

August
#prettier interface code
#real images/animation work
#polish image effect/text effect/animation
#sound effect
#test play
#ending animation

End of August
Shippppp :)
'''
from w1 import * #w1time, w1charlist...etc
from event import Event
from conversation import Conversation

while w1time.current != None:
    #ascertain location
    for player in w1players:
        oldlocation = player.get_location(w1time.past)
        newlocation = player.get_location(w1time.current)
        if player.get_attendance(w1time.current) == Scheduleinfo.optional.value:
            places_to_go = player.mapk.access
            if newlocation == None:
                print("You didn't have a plan.")
            else: 
                print("Your plan was to go to " + newlocation + " now.")    
            newlocation = input("Where would you like to go? " + str(places_to_go))
            player.update_schedule(w1time.current, newlocation)
        if oldlocation == newlocation:
            print("You are staying at " + str(oldlocation) + ".")
        else:
            print("You are now heading to " + str(newlocation) + ".")
    #run any runnable events
    count = 1
    while count != 0:
        count = 0
        for eventindex, (eventreq,event) in w1eventdict.items():
            e = Event(eventindex, w1eventdict)
            count += e.run_event(w1time.current, w1charlist) 
    #run conversation
    for location in w1locations:
        playerspresent = []
        for player in w1players:
            if player.get_location(w1time.current) == location:
                playerspresent.append(player)
        if playerspresent:
            npcpresent = []
            for npc in w1npcs:
                if npc.get_location(w1time.current) == location:
                    npcpresent.append(npc)
            conversation = Conversation(playerspresent, npcpresent)  
            conversation.run_conversation(w1time.current, w1charlist, w1eventdict, w1convodict)
    #time passes
    w1time.timepass()
    print("time passes!")
    
print("the game is over")

            
            
        

    
    
    


