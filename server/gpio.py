import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def cleanup():
    GPIO.cleanup()
    