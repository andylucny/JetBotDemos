import cv2
import numpy as np
from gstreamer import gstreamer_pipeline
from jetbot import JetBot

robot = JetBot()
robot.stop() 
 
threshold = 300
def updateThreshold( *args ):
    global threshold
    threshold = max(args[0],4)

speed = 70
def updateSpeed( *args ):
    global speed
    speed = args[0]
    robot.setSpeed(speed)

cv2.namedWindow("Circle")
cv2.createTrackbar("threshold", "Circle", threshold, 512, updateThreshold)
cv2.createTrackbar("speed", "Circle", speed, 255, updateSpeed)

camera = cv2.VideoCapture(gstreamer_pipeline(1280,720,1280//2,720//2,20,0), cv2.CAP_GSTREAMER)

trials = 0;
while True:
    hasFrame, frame = camera.read() 
    if not hasFrame: 
        break
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    frame = cv2.blur(frame,(5,5))
    
    circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 2, 100, param1=threshold, param2=threshold//4, minRadius=10, maxRadius=90)
    found = False
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    if circles is not None: 
        for circle in circles[0,:]:
            x = circle[0]
            y = circle[1]
            r = circle[2]
            if r > 0:
                cv2.circle(frame,(x,y),r,(0,0,255),2)
                cv2.circle(frame,(x,y),2,(0,0,255),cv2.FILLED)
                found = True
                found_x = x
                found_y = y
                found_radius = r
                break
    
    if found:
        print(found_x,found_y,found_radius)
        if found_x < frame.shape[1]*0.4 :
            robot.left()
        elif found_x > frame.shape[1]*0.6 :
            robot.right()
        elif found_radius > 70:
            robot.backward()
        elif found_radius < 40:
            robot.forward()
        else:
            robot.stop() 
        trials = 0
    else:
        print('ball not recognized')
        trials += 1
        if trials == 5:
            robot.stop()
    
    cv2.imshow("Circle",frame)
    if cv2.waitKey(10) == 27:
        break
    
cv2.destroyAllWindows()
robot.stop() 

