import RPi.GPIO as GPIO
import time

LED_PIN = 12

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    pwm_led = GPIO.PWM(LED_PIN, 100)
    pwm_led.start(100)

    try:
        while True:
            duty = int(raw_input("Enter brightness (0 to 100):"))

            if duty < 0:
                duty = 0
            if duty > 100:
                duty = 100

            pwm_led.ChangeDutyCycle(duty)

    except KeyboardInterrupt:
        pwm_led.stop()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
