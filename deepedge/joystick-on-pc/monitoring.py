from agentspace import Agent,Space

class MonitoringAgent(Agent):

    def __init__(self,name):
        self.name = name
        super().__init__()

    def init(self):
        self.attach_trigger(self.name)

    def senseSelectAct(self):
        data = Space.read(self.name,[])
        print(data)
