# motor 
from Adafruit_MotorHAT import Adafruit_MotorHAT as HAT
import time
left_motor_channel = 1 # right_motor_channel = 2
driver = HAT(i2c_bus=1) 
motor = driver.getMotor(left_motor_channel)
speed = 200 # 0 .. 255
motor.setSpeed(speed)
motor.run(HAT.FORWARD)
time.sleep(0.6)
motor.run(HAT.BACKWARD)
time.sleep(0.6)
motor.run(HAT.RELEASE)

