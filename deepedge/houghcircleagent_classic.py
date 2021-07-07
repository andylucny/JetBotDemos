import cv2
import numpy as np
from agentspace import Agent,Space

threshold = 300
def updateThreshold( *args ):
    global threshold
    threshold = max(args[0],4)
    
class HoughCircleAgent(Agent):

    def __init__(self,nameImage,nameBall):
        self.nameImage = nameImage
        self.nameBall = nameBall
        super().__init__()

    def init(self): 
        global threshold
        cv2.namedWindow("hough circle")
        cv2.createTrackbar("threshold", "hough circle", threshold, 512, updateThreshold)
        self.attach_trigger(self.nameImage)

    def senseSelectAct(self):
        global threshold
        frame = Space.read(self.nameImage,None)
        if frame is None:
            cv2.imshow("hough circle",frame)
            return
            
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.blur(frame,(3,3))
        circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 2, 100, param1=threshold, param2=threshold//2, minRadius=10, maxRadius=90)
        found = False
        frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
        if circles is not None: 
            for circle in circles[0,:]:
                x = int(circle[0])
                y = int(circle[1])
                r = int(circle[2])
                if r > 0:
                    cv2.circle(frame,(x,y),r,(0,0,255),2)
                    cv2.circle(frame,(x,y),2,(0,0,255),cv2.FILLED)
                    found = True
                    found_x = x
                    found_y = y
                    found_radius = r
                    break
    
        if found:
            #print('found',found_x,found_y,found_radius)
            Space.write(self.nameBall,[found_x,found_y,found_radius],0.5)
        else:
            #print('ball not recognized, threshold:',threshold)
            pass
    
        cv2.imshow("hough circle",frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite('houghCircle.png',frame)

