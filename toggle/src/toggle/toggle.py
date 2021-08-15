class t():
    def __init__(self, default=False):
        if(type(default) == bool):
            self.value = default
            self.v = self.value
        else:
            self.value = False
            self.v = False
    def toggle(self, toset="toggle"):
        toSet = toset.lower()
        if(toSet == "true"):
            self.value = True
            self.v = True
        elif(toSet == "false"):
            self.value = False
            self.v = False
        else:
            if(self.value == True and self.v == True):
                self.value = False
                self.v = False
            elif(self.value == False and self.v == False):
                self.value = True
                self.v = True
            else:
                return "Manually changed values"
    def t(self):
        self.toggle()
    def setTo(self, toSetTo):
        toSet = toSetTo.lower()
        if(toSet == "true" or toSet == "t"):
            self.value = True
            self.v = True
        elif(toSet == "false" or toSet == "f"):
            self.value = False
            self.v = False
        else:
            return "input must be true, false, t, or f"
    def setTrue(self):
        self.value = True
        self.v = True
    def setFalse(self):
        self.value = False
        self.v = False
    def st(self):
        self.setTrue()
    def sf(self):
        self.setFalse()
    def f(self):
        self.sf()
    def t(self):
        self.st()
            