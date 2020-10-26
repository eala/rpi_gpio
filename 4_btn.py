import RPi.GPIO as GPIO
import time

def main():
    BTN_PIN = 11
    MIN_TIME_INTERVAL = 0.4 # sec

    # de-bounce when pressed
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BTN_PIN, GPIO.IN)

    prev_status = None
    prev_time = time.time()
    try:
        while True:
            input = GPIO.input(BTN_PIN)
            cur_time = time.time()
            if input == GPIO.LOW and prev_status == GPIO.HIGH and \
                    (cur_time - prev_time > MIN_TIME_INTERVAL):
                print("button pressed " + time.ctime())
                prev_time = cur_time
            prev_status = input

    except KeyboardInterrupt:
        print("Exception: keyboard interrupt")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
