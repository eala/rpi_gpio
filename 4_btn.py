import RPi.GPIO as GPIO
import time

def main():
    BTN_PIN = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BTN_PIN, GPIO.IN)

    prev_status = None
    try:
        while True:
            input = GPIO.input(BTN_PIN)
            if input == GPIO.LOW and prev_status == GPIO.HIGH:
                print("button pressed " + time.ctime())
            prev_status = input

    except KeyboardInterrupt:
        print("Exception: keyboard interrupt")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
