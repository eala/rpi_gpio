import RPi.GPIO as GPIO
import time

BUZZ_PIN = 7
DO_PIN = 11
RE_PIN = 12
ME_PIN = 13
FA_PIN = 15
DO_PITCH = 523  # Hz
RE_PITCH = 587
ME_PITCH = 659
UNKNOWN_PITCH = 0
FA_PITCH = 698
SO_PITCH = 784
LA_PITCH = 880

DURATION = 0.2

def buzz(pitch):
    period = 1.0 / pitch
    half_period = period / 2
    cycles = int(DURATION * pitch)

    for i in xrange(cycles):
        GPIO.output(BUZZ_PIN, GPIO.HIGH)
        time.sleep(half_period)
        GPIO.output(BUZZ_PIN, GPIO.LOW)
        time.sleep(half_period)

def btn_click_callback(channel):
    print("button clicked: ", channel);
    pitch = 523
    duration = 1
    if channel == DO_PIN:
        pitch = DO_PITCH
    if channel == RE_PIN:
        pitch = RE_PITCH
    if channel == ME_PIN:
        pitch = ME_PITCH
    if channel == FA_PIN:
        pitch = FA_PITCH

    MIN_TIME_DIFF = 0.2
    buzz(pitch)

def main():
    # de-bounce when pressed
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZ_PIN, GPIO.OUT)
    GPIO.setup(DO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ME_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(FA_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    WAIT_TIME = 300

    try:
        GPIO.add_event_detect(DO_PIN, GPIO.FALLING, callback = btn_click_callback, bouncetime = WAIT_TIME)
        GPIO.add_event_detect(RE_PIN,GPIO.FALLING, callback = btn_click_callback, bouncetime = WAIT_TIME)
        GPIO.add_event_detect(ME_PIN,GPIO.FALLING, callback = btn_click_callback, bouncetime = WAIT_TIME)
        GPIO.add_event_detect(FA_PIN,GPIO.FALLING, callback = btn_click_callback, bouncetime = WAIT_TIME)

        while True:
            time.sleep(10)

    except KeyboardInterrupt:
        print("Exception: keyboard interrupt")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
