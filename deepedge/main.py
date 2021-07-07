from agentspace import Space
import signal 
import os
import time
def signal_handler(signal, frame):
    Space.write('forward',0)
    Space.write('turn',0)
    time.sleep(0.25)
    os._exit(0)
signal.signal(signal.SIGINT, signal_handler)

from cameraagent import CameraAgent
from houghcircleagent import HoughCircleAgent
from remote import ClientAgent
from controlagent import ControlAgent
from remotecontrolagent import RemoteControlAgent
from gearagent import GearAgent

CameraAgent(0,'colorImage')
HoughCircleAgent('colorImage','ballPosition')
ClientAgent('192.168.2.3',7070,'joystick')
ControlAgent('ballPosition','forward','turn')
RemoteControlAgent('joystick','forward','turn')
GearAgent('forward','turn')
