from agentspace import Agent,Space

class ControlAgent(Agent):

    def __init__(self,nameBall,nameForward,nameTurn):
        self.nameBall = nameBall
        self.nameForward = nameForward
        self.nameTurn = nameTurn
        super().__init__()

    def init(self):
        self.attach_timer(0.1)

    def senseSelectAct(self):
        ball = Space.read(self.nameBall,None)
        if ball is None:
            Space.write(self.nameForward,0,validity=0.2)
            Space.write(self.nameTurn,0,validity=0.2)
        elif ball[0] < 640*0.4: # to left
            Space.write(self.nameForward,0,validity=0.2)
            Space.write(self.nameTurn,-1,validity=0.2)
        elif ball[0] > 640*0.6: # to right
            Space.write(self.nameForward,0,validity=0.2)
            Space.write(self.nameTurn,1,validity=0.2)
        elif ball[2] < 35: # forward
            Space.write(self.nameForward,1,validity=0.2)
            Space.write(self.nameTurn,0,validity=0.2)
        elif ball[2] > 50: # backward
            Space.write(self.nameForward,-1,validity=0.2)
            Space.write(self.nameTurn,0,validity=0.2)
        else:
            Space.write(self.nameForward,0,validity=0.2)
            Space.write(self.nameTurn,0,validity=0.2)
