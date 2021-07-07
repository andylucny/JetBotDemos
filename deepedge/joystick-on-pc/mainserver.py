import signal 
import os
def signal_handler(signal, frame):
    os._exit(0)
signal.signal(signal.SIGINT, signal_handler)

from joystickapiagent import JoystickAgent
#from monitoring import MonitoringAgent
from remote import ServerAgent

JoystickAgent('joystick')
#MonitoringAgent('joystick')
ServerAgent(7070,'joystick')
