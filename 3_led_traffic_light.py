import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GREEN_LED_PIN =12
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
YELLOW_LED_PIN =16
GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)
RED_LED_PIN =18
GPIO.setup(RED_LED_PIN, GPIO.OUT)

try:
    while True:
        print("green")
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)

        print("yellow")
        GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
    
        print("red")
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        #print("LED is off")
        #GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        #time.sleep(1)

except KeyboardInterrupt:
    print("Exception: keyboard interrupt")

finally:
    GPIO.cleanup()
