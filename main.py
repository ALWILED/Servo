from time import sleep
from machine import Pin
from servo import Servo

servo_pin = Pin(18)
my_servo = Servo(servo_pin)
while True:
    my_servo.write_us(2000)
    sleep(3)              
