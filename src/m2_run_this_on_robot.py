"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Alexander Tabuyo.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # run_test_arm()
    # run_test_calibrate()
    # run_test_move_rose_to_position()
    # run_test_lower_arm()
    real_thing()
    # run_test_go_straight_for_seconds()
    # run_test_go_straight_for_inches_using_time()
    # run_test_go_straight_for_inches_using_encoder()


def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate.is_time_to_stop:
            break

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()


def run_test_calibrate():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()


def run_test_move_rose_to_position():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(2556)


def run_test_lower_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()


def run_test_go_straight_for_seconds():
    print(1)
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_seconds(1, 100)


def run_test_go_straight_for_inches_using_time():
    print(2)
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_time(10, 75)


def run_test_go_straight_for_inches_using_encoder():
    print(3)
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_encoder(10, 50)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()