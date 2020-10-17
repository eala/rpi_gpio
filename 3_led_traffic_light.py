import RPi.GPIO as GPIO
import time

class TrafficLight:
    def __init__(self, name, pin, duration):
        self.name = name
        self.pin = pin
        self.duration = duration
        GPIO.setup(self.pin, GPIO.OUT)

    def run(self):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(self.duration)
        GPIO.output(self.pin, GPIO.LOW)

def init(traffic_light_list):
    GPIO.setmode(GPIO.BOARD)
    traffic_light_list.append(TrafficLight("GREEN_LED_PIN", 12, 4))
    traffic_light_list.append(TrafficLight("YELLOW_LED_PIN", 16, 2))
    traffic_light_list.append(TrafficLight("RED_LED_PIN", 18, 4))

def main():
    traffic_light_list = list()
    init(traffic_light_list)
    try:
        while True:
            for traffic_light in traffic_light_list:
                traffic_light.run()

    except KeyboardInterrupt:
        print("Exception: keyboard interrupt")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
