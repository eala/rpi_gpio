import RPi.GPIO as GPIO
import time

def buzz(buzz_pin, pitch, duration):
    period = 1.0 / pitch
    half_period = period / 2
    cycles = int(duration * pitch)

    for i in xrange(cycles):
        GPIO.output(buzz_pin, GPIO.HIGH)
        time.sleep(half_period)
        GPIO.output(buzz_pin, GPIO.LOW)
        time.sleep(half_period)

def main():
    BUZZ_PIN = 12

    # de-bounce when pressed
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZ_PIN, GPIO.OUT)

    try:
        while True:
            pitch = raw_input("Enter Pitch (200 to 2000):")
            duration = raw_input("Enter duration (sec): ")
            buzz(BUZZ_PIN, float(pitch), float(duration))

    except KeyboardInterrupt:
        print("Exception: keyboard interrupt")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
