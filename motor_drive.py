import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7,gpio.OUT)
    gpio.setup(5,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)
    gpio.setup(3,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.output(3,True)
    gpio.output(18,True)

def forward(t):
    init()
    gpio.output(5,0)
    gpio.output(7,1)
    gpio.output(13,0)
    gpio.output(15,1)
    time.sleep(t)
    gpio.output(3,0)
    gpio.output(16,0)
    gpio.cleanup()
def reverse(t):
    init()
    gpio.output(7,1)
    gpio.output(11,0)
    gpio.output(13,1)
    gpio.output(15,0)
    time.sleep(t)
    gpio.output(18,0)
    gpio.output(16,0)
    gpio.cleanup()

def left(t):
    init()
    gpio.output(7,0)
    gpio.output(11,1)
    gpio.output(13,0)
    gpio.output(15,0)
    time.sleep(t)
    gpio.output(18,0)
    gpio.output(16,0)
    gpio.cleanup()
    
def right(t):
    init()
    gpio.output(7,1)
    gpio.output(11,1)
    gpio.output(13,0)
    gpio.output(15,1)
    time.sleep(t)
    gpio.output(18,0)
    gpio.output(16,0)
    gpio.cleanup()

def turn(t):
    init()
    gpio.output(7,1)
    gpio.output(11,0)
    gpio.output(13,0)
    gpio.output(15,1)
    time.sleep(t)
    gpio.output(18,0)
    gpio.output(16,0)
    gpio.cleanup()
