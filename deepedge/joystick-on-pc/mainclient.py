import signal 
import os
def signal_handler(signal, frame):
    os._exit(0)
signal.signal(signal.SIGINT, signal_handler)

from remote import ClientAgent
from monitoring import MonitoringAgent

ClientAgent('localhost',7070,'joystick')
MonitoringAgent('joystick')
