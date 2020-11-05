import RPi.GPIO as GPIO
import time

PIR_PIN = 26

def detect_callback(channel):
    print("motion detected!")

def main():
    # de-bounce when pressed
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    WAIT_TIME = 100

    try:
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback = detect_callback, bouncetime = WAIT_TIME)

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exception: keyboard interrupt")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
