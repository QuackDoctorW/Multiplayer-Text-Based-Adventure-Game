from enum import Enum
from collections import namedtuple
from relation import Relationinfo
class Rateinfo(Enum):
    neutral = 0
    lie = -2
    truth = 2

from character import Npc
                           
#global truth
#factdict = {1: Statement(charobj, timeint, "alocation", "about in str"), #anything can be None
            #2: Statement(None, None, None, None),
            #3: Statement(None, None, None, None)}

Statement = namedtuple("Statement", ["char", "timeint","location","about"],\
                       defaults = [None,None,None,None]) 

class Info:
    def __init__(self, afactdict):
        self.content = {} #key: about who, ((value:factindex, fromwho)) can append 
        self.facts = {} #key factindex from factdict, val is (speakers)
        self.maybes = {} #key factindex from factdict, val is (speakers)
        self.lies = {} #key factindex from factdict, val is (speakers)
        self.factdict = afactdict

    def addcontent(self, contentowner, fromc, factindex: int, rating):
        if isinstance(contentowner, Npc):   
            aboutwho = self.factdict[factindex].char
            if aboutwho not in self.content:
                self.content[aboutwho] = set()
            self.content[aboutwho].add((factindex, fromc))              
            if rating == None:
                rating = self.ratefact(contentowner, fromc, aboutwho, factindex)
            processcontent(contentowner, fromc, factindex, rating)                      
        else: #if this is a player
            self.facts[factindex] = [] #just adding to factindex is fine, no need to rate for players
    
    def ratefact(self, contentowner, fromc, aboutwho, factindex):
        relation = contentowner.get_relation(fromc)  
        if fromc == "contentowner":
            return Rateinfo.truth
        elif factindex in self.facts:
            return Rateinfo.truth        
        elif factindex in self.lies and relation!= Relationinfo.soulmate and relation != Relationinfo.friendly:
            return Rateinfo.lie
        elif factindex in self.maybes and \
             relation!= Relationinfo.nemesis and\
             relation != Relationinfo.opposed and \
             len(self.maybes[factindex]) < 3:
            if relation == Relationinfo.soulmate or relation == Relationinfo.friendly:
                return Rateinfo.truth
            else: #neurtral plus minus
                return Rateinfo.maybe
        else: #not self knowledge, and no one else said the same thing - look for contradictions
            #if contradiction then compare trustworthiness, if no contradiction believe it
            contradictions_location = []
            contradictions_about = []
            agreement = []
            agreement_point = 0
            if aboutwho in self.content: #if we do know who it is about 
                location = self.factdict[factindex].location
                timeint = self.factdict[factindex].timeint
                about = self.factdict[factindex].about
                for oldfactindex, oldspeaker in self.content[aboutwho]: #note three type of facts about someone, 1) char is "something", 2) char at when at here 3) char at when at here do what
                    oldlocation = self.factdict[oldfactindex].location
                    oldtimeint = self.factdict[oldfactindex].timeint
                    oldabout = self.factdict[oldfactindex].about
                    multiplier = contentowner.get_relation(oldpseaker).relation_multiplier()
                    if timeint == oldtimeint: #have to go through time and location test, then doing what test
                        if location != oldlocation:
                            contradictions_location.append((oldfactindex, multiplier))
                        elif (about == "not " + oldabout) or ("not " + about == oldabout):
                            multiplier = contentowner.get_relation(oldpseaker).relation_multiplier()
                            contradictions_about.append((oldfactindex, multiplier))
                        else:
                            agreement.append(oldfactindex)
                            agreement_point += multiplier
                                                  
            if contradictions_location or contradictions_about: #yes there are contradiction
                return contradicton_decider(contentowner, fromc, aboutwho, factindex, agreement, agreement_point, contradictions_location, contradictions_about)
            else:
                if relation == Relationinfo.soulmate or relation == Relationinfo.friendly:
                    return Rateinfo.truth
                else:
                    return Rateinfo.neutral

    def contradicton_decider(self, contentowner, fromc, aboutwho, factindex, agreement, agreement_point, contradictions_location, contradictions_about): 
        #list of (fact indexes, multiplier) for contradictions
        #location test
        loc = self.factdict[factindex].location
        locdict = {}
        for contra_l_index, contra_l_multi in contradictions_location: #get a dict of locations and values
            oldloc = self.factdict[contra_l_index].location
            if oldloc not in locdict:
                locdict[oldloc] = 0
            locdict[oldloc] += contra_l_multi
        best_loc = 0
        for aloc in locdict:
            best_loc = max(locdict[aloc], best_loc)
           
        #about test
        about = self.factdict[factindex].about
        aboutdict = {}
        for contra_a_index, contra_a_multi in contradictions_about:
            oldabout = self.factdict[contra_a_index].about
            if oldabout not in aboutdict:
                aboutdict[oldabout] = 0
            aboutdict[oldabout] += contra_a_multi
        best_about = 0
        for anabout in aboutdict:
            best_about = max(aboutdict[anabout], best_about) 
        
        #compare two together
        if best_loc != 0 and best_loc > 
        
        
        if best_loc == 0 or best_loc == locdict[loc]: #just on facts or if they agree in location
            if agreement_point > best_about:
                if self.factdict[factindex].location != None:
                    for contra_l_index, contra_l_multi in contradictions_location: #current fact is true, set location difference to lies
                        if self.factdict[contra_l_index].location != self.factdict[factindex].location:
                            processcontent(contentowner, fromc, contra_l_index, Rateinfo.lie)
                for contra_a_index, contra_a_multi in contradictions_about: #current about is true, set about difference to lies
                    if self.factdict[contra_a_index].about != self.factdict[factindex].about:
                        processcontent(contentowner, fromc, contra_a_index, Rateinfo.lie)
                #for things that don't cause contradiction, doesn't mean they are true: can be bunnycat eating, bunnycat reading, not sure which one's true, but doesn't not "not eating"
                return Rateinfo.truth
            elif agreement_point == best_about:
                return Rateinfo.neutral
            else: #best about wins
                   
                for contra_l_index, contra_l_multi in contradictions_location: #best location is true, set location difference to lies
                    if 
                    if self.factdict[contra_l_index].location != self.factdict[factindex].location:
                        processcontent(contentowner, fromc, contra_l_index, Rateinfo.lie)
                #set anything but best loc to lie (dont set agree with best loc to true)
                #set best_about to truth and everything else to lie - supporting and other contradictions
                return Rateinfo.lie

   
    def processcontent(self, contentowner, fromc, factindex, rating):     
        if rating == Rateinfo.truth :
            if factindex not in self.facts: #if not in truth, add it
                self.facts[factindex] = set()
            self.facts[factindex].add(fromc)
            if factindex in self.maybes:
                for char in self.maybes[factindex]:
                    self.facts[factindex].add(char)
                self.maybes.remove(factindex)
            if factindex in self.lies: #if was in lies before, redeem trust val, delete it
                for char in self.lies[factindex]:
                    contentowner.update_relation(char, +5)
                    self.facts[factindex].add(char)
                self.lies.remove(factindex)
                
        elif rating == Rateinfo.neutral:
            if factindex not in self.maybes: #if not in maybes, add it
                self.maybes[factindex] = set()
            self.maybes[factindex].add(fromc)
            if factindex in self.facts:
                for char in self.facts[factindex]:
                    self.maybes[factindex].add(char)
                self.facts.remove(factindex)
            if factindex in self.lies: #if was in lies before, redeem trust val, delete it
                for char in self.lies[factindex]:
                    contentowner.update_relation(char, +5)
                    self.maybes[factindex].add(char)
                self.lies.remove(factindex)
                
        else:
            if factindex not in self.lies: #if not in lies, add it
                self.lies[factindex] = set()
            self.lies[factindex].add(fromc)
            contentowner.update_relation(fromc, -5) #this value subject to change after balance
            if factindex in self.facts:
                for char in self.facts[factindex]:
                    contentowner.update_relation(char, -5)
                    self.lies[factindex].add(char)
                self.facts.remove(factindex) 
            if factindex in self.maybes:
                for char in self.maybes[factindex]:
                    contentowner.update_relation(char, -5)
                    self.lies[factindex].add(char)
                self.maybes.remove(factindex)                   
            
            
        
        
        
        
        





        
    