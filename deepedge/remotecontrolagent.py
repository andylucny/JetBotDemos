from agentspace import Agent,Space

class RemoteControlAgent(Agent):

    def __init__(self,nameJoystick,nameForward,nameTurn):
        self.nameJoystick = nameJoystick
        self.nameForward = nameForward
        self.nameTurn = nameTurn
        super().__init__()

    def init(self):
        self.attach_trigger(self.nameJoystick)

    def senseSelectAct(self):
        data = Space.read(self.nameJoystick,[[],[0,0,0],[]])
        if data[1][0] < -5000: # to left
            Space.write(self.nameForward,0,validity=0.2,priority=2.0)
            Space.write(self.nameTurn,-1,validity=0.2,priority=2.0)
        elif data[1][0] > 5000: # to right
            Space.write(self.nameForward,0,validity=0.2,priority=2.0)
            Space.write(self.nameTurn,1,validity=0.2,priority=2.0)
        elif data[1][1] < -5000: # forward
            Space.write(self.nameForward,1,validity=0.2,priority=2.0)
            Space.write(self.nameTurn,0,validity=0.2,priority=2.0)
        elif data[1][1] > 5000: # backward
            Space.write(self.nameForward,-1,validity=0.2,priority=2.0)
            Space.write(self.nameTurn,0,validity=0.2,priority=2.0)
