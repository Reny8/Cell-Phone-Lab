class Cell_Phone():
    def __init__(self,model):
        self.cell_model = model
        self.phone_number = 2672664443
        self.contacts = {"Becky": 2158675309, "John": 2672356010, "Tay" : 6103320234}
        self.messages_list = []
        self.phone_on_vibrate = False
    
    def message(self,text):
        self.messages_list.append(text)

    def vibrate(self):
        if self.phone_on_vibrate == False:
            self.phone_on_vibrate == True
            print("Your phone is on vibrate mode")
        elif self.phone_on_vibrate == True:
            self.phone_on_vibrate == False
            print("Your phone is on full volume")

    def send_a_text(self,contact):
        input("What would you like the message to say: ")
        print(f"Your message has been sent to {contact}")
