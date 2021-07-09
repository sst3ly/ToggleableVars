class Toggleable():
    def __init__(self, setto=False):
        self.value = setto
    def toggle(self):
        if(self.value == False):
            self.value = True
        elif(self.value == True):
            self.value = False
