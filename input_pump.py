import RPi.GPIO as GPIO
import time
import argparse


def setup_GPIO(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)

def main():
    #Parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--time',type=int)
    parser.add_argument('--pin',type=int)
    args = parser.parse_args()
    seconds = args.time
    pin = args.pin

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
