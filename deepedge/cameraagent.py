import cv2
import numpy as np
from gstreamer import gstreamer_pipeline
from agentspace import Agent,Space

class CameraAgent(Agent):

    def __init__(self,cameraId,nameImage):
        self.cameraId = cameraId
        self.nameImage = nameImage
        super().__init__()

    def init(self): 
        self.camera = cv2.VideoCapture(gstreamer_pipeline(1280,720,1280//2,720//2,20,0), cv2.CAP_GSTREAMER)
        while True:
            hasFrame, frame = self.camera.read() 
            if hasFrame: 
                Space.write(self.nameImage,frame,0.15)
    
    def senseSelectAct(self):
        pass

