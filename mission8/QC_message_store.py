class SMS_Store:
    def __init__(self):
        self.messages = []
        
    def add_new_arrival(self,from_number,time_arrived,text_of_SMS):
        has_been_viewed = False
        new_tuple = has_been_viewed,from_number,time_arrived,text_of_SMS
        self.messages.append(new_tuple)
        
    def message_count(self):
        return len(self.messages)
    
    def get_unread_indexes(self):
        liste = []
        for i, message in enumerate(self.messages):
            if message[0] == False:
                liste.append(i)
        return liste
    
    def get_message(self,i):
        if 0 <= i < len(self.messages):
            msg = self.messages[i]
            updated = (True,msg[1],msg[2],msg[3])
            self.messages[i] = updated
            return updated[1:]
        else:
            return None
        
    def delete(self,i):
        if 0 <= i < len(self.messages):
            del self.messages[i]
            
    def clear(self):
        self.messages.clear()