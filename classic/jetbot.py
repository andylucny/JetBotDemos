from Adafruit_MotorHAT import Adafruit_MotorHAT as HAT

class JetBot:
    
    def __init__(self,speed=200):
        self.speed = speed
        left_motor_channel = 1
        right_motor_channel = 2
        self.driver = HAT(i2c_bus=1) 
        self.left_motor = self.driver.getMotor(left_motor_channel)
        self.right_motor = self.driver.getMotor(right_motor_channel)
        self.left_motor.setSpeed(self.speed)
        self.right_motor.setSpeed(self.speed)

    def left(self):
        self.left_motor.run(HAT.BACKWARD)
        self.right_motor.run(HAT.FORWARD)

    def right(self):
        self.left_motor.run(HAT.FORWARD)
        self.right_motor.run(HAT.BACKWARD)
        
    def forward(self):
        self.left_motor.run(HAT.FORWARD)
        self.right_motor.run(HAT.FORWARD)
        
    def backward(self):
        self.left_motor.run(HAT.BACKWARD)
        self.right_motor.run(HAT.BACKWARD)
        
    def stop(self):
        self.left_motor.run(HAT.RELEASE)
        self.right_motor.run(HAT.RELEASE)

    def setSpeed(self,speed):
        self.speed = speed
        self.left_motor.setSpeed(self.speed)
        self.right_motor.setSpeed(self.speed)

# Test    
if __name__ == "__main__":

    import time
    robot = JetBot()
    print('right')
    robot.right()
    time.sleep(1)
    print('left')
    robot.left()
    time.sleep(1)
    print('forward')
    robot.forward()
    time.sleep(1)
    print('backward')
    robot.backward()
    time.sleep(1)
    print('stop')
    robot.stop()
