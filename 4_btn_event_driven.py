import RPi.GPIO as GPIO
import time

def btn_click_callback(channel):
    print("button clicked")

def main():
    BTN_PIN = 11
    WAIT_TIME = 200     # ms

    # de-bounce when pressed
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BTN_PIN, GPIO.IN)

    try:
        GPIO.add_event_detect(BTN_PIN, \
                            GPIO.FALLING, \
                            callback = btn_click_callback, \
                            bouncetime = WAIT_TIME)
        while True:
            time.sleep(10)

    except KeyboardInterrupt:
        print("Exception: keyboard interrupt")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
