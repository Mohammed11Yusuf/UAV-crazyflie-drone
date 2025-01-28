import time
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.utils import uri_helper
import math

URI = uri_helper.uri_from_env(default='radio://0/90/2M/E7E7E7E7E5')

def simple_sequence():
    # Low-level drivers
    cflib.crtp.init_drivers()
    cf = Crazyflie()
    cf.open_link(URI)  # Connecting to drone...
    print('Connected to Crazyflie')

    commander = cf.high_level_commander  # High Level Commander...

    cf.param.set_value('kalman.resetEstimation', '1')
    time.sleep(0.1)
    cf.param.set_value('kalman.resetEstimation', '0')
    time.sleep(2)

    print('Taking off...')
    commander.takeoff(0.5, 2.0)  # Take off to 0.5m height over 2 seconds
    time.sleep(3)

    # Fly the first circle at 0.5m height with a 0.5m radius
    fly_circle(commander, 0.5, 0.5, False)  # Fly clockwise
    time.sleep(1)

    # Ascend to 1m height
    commander.go_to(0, 0, 1.0, 0, 2)
    time.sleep(3)

    # Fly the second circle at 1m height with a 0.5m radius
    fly_circle(commander, 0.5, 1.0, True)  # Fly counterclockwise
    time.sleep(1)

    # Return to origin
    print('Returning to origin...')
    commander.go_to(0, 0, 0.5, 0, 2)  # Return to start point at 0.5m height
    time.sleep(4)

    print('Landing...')
    commander.land(0.0, 2.0)  # Land
    time.sleep(2)

    commander.stop()
    print('Flight sequence completed')

    cf.close_link()

# Function to fly in a circular pattern
def fly_circle(commander, radius, height, reverse):
    steps = 36  # Number of steps for the circle (the more steps, the smoother the circle)
    direction = -1 if reverse else 1  # Reverse the direction if needed
    for i in range(steps + 1):
        angle = direction * 2 * math.pi * i / steps
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        commander.go_to(x, y, height, 0, 2)
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        simple_sequence()
    except KeyboardInterrupt:
        print('Program terminated!')
