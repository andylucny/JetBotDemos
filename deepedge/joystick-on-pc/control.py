from remote import ClientAgent
from gearagent import GearAgent
from agentspace import Agent,Space

ClientAgent('192.168.2.3',7070,'joystick')
GearAgent('Forward','Turn')

class ControlAgent(Agent):

    def __init__(self,nameJoystick,nameForward,nameTurn):
        self.nameJoystick = nameJoystick
        self.nameForward = nameForward
        self.nameTurn = nameTurn
        super().__init__()

    def init(self):
        self.attach_trigger(self.nameJoystick)

    def senseSelectAct(self):
        data = Space.read(self.nameJoystick,[])
        if data[1][0] < -5000: # to left
            Space.write(self.nameForward,0,0.2)
            Space.write(self.nameTurn,-1,0.2)
        elif data[1][0] > 5000: # to right
            Space.write(self.nameForward,0,0.2)
            Space.write(self.nameTurn,1,0.2)
        elif data[1][1] < -5000: # forward
            Space.write(self.nameForward,1,0.2)
            Space.write(self.nameTurn,0,0.2)
        elif data[1][1] > 5000: # backward
            Space.write(self.nameForward,-1,0.2)
            Space.write(self.nameTurn,0,0.2)
        else:
            Space.write(self.nameForward,0,0.2)
            Space.write(self.nameTurn,0,0.2)

ControlAgent('joystick','Forward','Turn')
