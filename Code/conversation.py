from character import Player
class Conversation():
    def __init__(self, listofpresentplayers, listofpresentnpcs):
        self.players = listofpresentplayers
        self.npcs = listofpresentnpcs

    def run_conversation(self, timeint, charlist, eventdict, convodict):
        for player in self.players:
            talker_options = self.npcs + self.players
            talker_options.remove(player)
            talker_options_text = []     
            for i in talker_options:
                talker_options_text.append(i.name)            
            while True:
                player_choice = input(str(talker_options_text) + "I am done here: type None") #convodict with char as key: give dictionary with index as key, requirement and decisions
                if player_choice == "None": #player can leave early here
                    print("You chose to end all conversations")
                    break                   
                player_choice = self.convert_player_choice(player_choice, talker_options)
                if player_choice == "0": #meaning they made a typo 
                    continue
                talker_options.remove(player_choice) #each player can only talk to a person once
                talker_options_text.remove(player_choice.name)
                
                #check if player is talking to player or npc        
                if isinstance(player_choice, Player):#talking to player
                    count = 2
                    while count > 0:
                        question = input("is there something you want to ask?")
                        print("Player asked " + question)
                        answer = input("what is your reply?")
                        print("player_choice responded " + answer)
                        count -= 1
                else: #talking to npc
                    #check topic_dict empty stuff here
                    topic_dict = convodict[player_choice]
                    count = 3
                    while count > 0:                                
                        topic_options_index = []
                        topic_options_name = []
                        for convoindex, (convoreq, convo) in topic_dict.items(): 
                            if convoreq.check_req(timeint, charlist, eventdict):
                                topic_options_index.append(convoindex)
                                topic_options_name.append(convo.name)
                        chosen_topic_index = int(input(str(topic_options_index) + str(topic_options_name) + "leave this conversation type 0"))
                        if chosen_topic_index == 0: #can end convo with this npc here without going to max topics
                            print("You chose to leave this conversation and maybe talk to someone else.")
                            break
                        else:
                            topic_dict[chosen_topic_index][1].run_player_decision([player], []) #npclist applies for calculating consequences, does not apply here, so it is []
                            topic_dict[chosen_topic_index][0].completed = True
                            count -= 1
    def convert_player_choice(self, player_choice, talker_options):
        print("You chose to talk to " + player_choice)
        for i in talker_options:
            if i.name == player_choice:
                return i
        print("Not Valid Choice, try again")
        return "0"

                
                
        
        
        
