import RPi.GPIO as GPIO
import time
import argparse


def setup_GPIO(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

def pump(seconds, pin):
    setup_GPIO(pin)
    
    led_on = True
    try:
        GPIO.output(pin, led_on) 
        led_on = not led_on
        time.sleep(seconds)
        GPIO.output(pin, led_on)
    except:
        GPIO.cleanup()
        print("Failed to allocate pins")

if __name__ == "__main__":
    main()
