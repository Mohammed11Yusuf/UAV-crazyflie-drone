"""Crazyflie autonomous dual-circle flight demonstration.

The sequence performs:
1. Takeoff to 0.5 m
2. Clockwise circular trajectory at 0.5 m
3. Ascend to 1.0 m
4. Counter-clockwise circular trajectory at 1.0 m
5. Return to the origin
6. Land

Requires the Bitcraze cflib package and a configured Crazyflie link.
"""

import math
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.utils import uri_helper


URI = uri_helper.uri_from_env(default="radio://0/90/2M/E7E7E7E7E5")


def fly_circle(commander, radius, height, reverse=False):
    """Command a circular trajectory using discrete go_to waypoints."""
    steps = 36
    direction = -1 if reverse else 1

    for step in range(steps + 1):
        angle = direction * 2 * math.pi * step / steps
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        commander.go_to(x, y, height, 0, 2)
        time.sleep(0.5)


def run_flight_sequence():
    """Connect to Crazyflie and execute the demonstration sequence."""
    cflib.crtp.init_drivers()
    cf = Crazyflie()

    print("Connecting to Crazyflie...")
    cf.open_link(URI)
    print("Connected to Crazyflie")

    commander = cf.high_level_commander

    print("Resetting Kalman estimation...")
    cf.param.set_value("kalman.resetEstimation", "1")
    time.sleep(0.1)
    cf.param.set_value("kalman.resetEstimation", "0")
    time.sleep(2)

    try:
        print("Taking off to 0.5 m...")
        commander.takeoff(0.5, 2.0)
        time.sleep(3)

        print("Flying first clockwise circle...")
        fly_circle(commander, radius=0.5, height=0.5)
        time.sleep(1)

        print("Ascending to 1.0 m...")
        commander.go_to(0, 0, 1.0, 0, 2)
        time.sleep(3)

        print("Flying second counter-clockwise circle...")
        fly_circle(commander, radius=0.5, height=1.0, reverse=True)
        time.sleep(1)

        print("Returning to origin...")
        commander.go_to(0, 0, 0.5, 0, 2)
        time.sleep(4)

        print("Landing...")
        commander.land(0.0, 2.0)
        time.sleep(2)

        print("Flight sequence completed")
    finally:
        commander.stop()
        cf.close_link()


if __name__ == "__main__":
    try:
        run_flight_sequence()
    except KeyboardInterrupt:
        print("Program terminated by user")
