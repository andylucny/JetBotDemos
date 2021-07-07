from agentspace import Agent,Space
from Adafruit_MotorHAT import Adafruit_MotorHAT as HAT

class GearAgent(Agent):

    def __init__(self,nameForward,nameTurn):
        self.nameForward = nameForward
        self.nameTurn = nameTurn
        super().__init__()

    def init(self):
        left_motor_channel = 1 
        right_motor_channel = 2
        driver = HAT(i2c_bus=1) 
        self.left_motor = driver.getMotor(left_motor_channel)
        self.right_motor = driver.getMotor(right_motor_channel)
        speed = 75 # 0 .. 255
        self.left_motor.setSpeed(speed)
        self.right_motor.setSpeed(speed)
        self.attach_timer(0.1)

    def senseSelectAct(self):
        forward = Space.read(self.nameForward,0)
        turn = Space.read(self.nameTurn,0)
        if turn < 0: # to left
            self.left_motor.run(HAT.BACKWARD)
            self.right_motor.run(HAT.FORWARD)
        elif turn > 0: # to right
            self.left_motor.run(HAT.FORWARD)
            self.right_motor.run(HAT.BACKWARD)
        elif forward > 0: # forward
            self.left_motor.run(HAT.FORWARD)
            self.right_motor.run(HAT.FORWARD)
        elif forward < 0: # backward
            self.left_motor.run(HAT.BACKWARD)
            self.right_motor.run(HAT.BACKWARD)
        else:
            self.left_motor.run(HAT.RELEASE)
            self.right_motor.run(HAT.RELEASE)
