import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 16
ECHO_PIN = 18

def measure():
    temp = 25   # assumption temperature
    v = 331 + 0.6 * temp
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)     # 10 us from spec.
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    t = pulse_end - pulse_start
    d = t * v / 2   # twice distance near->far->near
    return d

def main():
    # de-bounce when pressed
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    try:
        while True:
            dist = measure()
            print("dist: " + str(dist))
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exception: keyboard interrupt")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
