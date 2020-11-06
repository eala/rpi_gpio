import RPi.GPIO as GPIO
import time

LED_PIN = 12

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    pwm_led = GPIO.PWM(LED_PIN, 100)
    pwm_led.start(0)  # duty

    duty = 0
    direct = 1  # increase or decrease
    unit = 5
    try:
        while True:
            pwm_led.ChangeDutyCycle(duty)
            time.sleep(0.1)

            duty = duty + direct * unit
            if duty > 100 or duty < 0:
                direct *= -1
                duty = duty + direct * unit
                time.sleep(0.5)

    except KeyboardInterrupt:
        pwm_led.stop()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
