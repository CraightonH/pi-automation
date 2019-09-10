from gpiozero import LED

red = LED(2)
yellow = LED(3)
green = LED(4)

def toggleRed():
    red.on()