from agentspace import Agent,Space
import joystickapi
import time

class JoystickAgent(Agent):

    def __init__(self,name):
        self.name = name
        super().__init__()

    def init(self):
        num = joystickapi.joyGetNumDevs()
        ret, caps, startinfo = False, None, None
        for id in range(num):
            ret, caps = joystickapi.joyGetDevCaps(id)
            if ret:
                print("joystick detected: " + caps.szPname)
                ret, startinfo = joystickapi.joyGetPosEx(id)
                break
        else:
            print("no joystick detected")
        self.id = id
        self.caps = caps
        time.sleep(0.1)
        _, self.startinfo = joystickapi.joyGetPosEx(self.id)
        self.attach_timer(0.1)

    def senseSelectAct(self):
        ret, info = joystickapi.joyGetPosEx(self.id)
        if ret:
            btns = [(1 << i) & info.dwButtons != 0 for i in range(self.caps.wNumButtons)]
            axisXYZ = [info.dwXpos-self.startinfo.dwXpos, info.dwYpos-self.startinfo.dwYpos, info.dwZpos-self.startinfo.dwZpos]
            axisRUV = [info.dwRpos-self.startinfo.dwRpos, info.dwUpos-self.startinfo.dwUpos, info.dwVpos-self.startinfo.dwVpos]
            Space.write(self.name,[btns,axisXYZ,axisRUV])
