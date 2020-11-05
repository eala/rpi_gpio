import RPi.GPIO as GPIO
import time

PIR_PIN = 26
LED_PIN = 12

def detect_callback(channel):
    print("motion detected!")
    for i in xrange(3):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)


def main():
    # de-bounce when pressed
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED_PIN, GPIO.OUT)
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
