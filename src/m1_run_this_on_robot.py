"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and
    Alex Wolfe.
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
    #pick_up_object(30)
    #robot = rosebot.RoseBot()
    #robot.arm_and_claw.calibrate_arm()
    #real_thing()
    find_and_pick_up_counterclockwise(50)
def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate.is_time_to_stop:
            break

def pick_up_object(speed):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(speed,speed)
    beeper = robot.sound_system.beeper
    while True:
        beeper.beep()
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
            robot.drive_system.stop()
            break
        data1 = robot.sensor_system.ir_proximity_sensor.get_distance()
        time.sleep(0.01)
        data2 = robot.sensor_system.ir_proximity_sensor.get_distance()
        time.sleep(0.01)
        data3 = robot.sensor_system.ir_proximity_sensor.get_distance()
        avg = (data1 + data2 + data3) / 3
        time.sleep(0.01 * (1 + avg))
    robot.drive_system.go_straight_for_inches_using_encoder(3, speed)
    robot.arm_and_claw.move_arm_to_position(4000)
    robot.drive_system.stop()

def find_and_pick_up_counterclockwise(speed):
    robot = rosebot.RoseBot()
    robot.drive_system.go(-speed,speed)
    while True:
        if robot.sensor_system.camera.get_biggest_blob().center.x > 160 and robot.sensor_system.camera.get_biggest_blob().center.x < 180:
            robot.drive_system.stop()
            break
    pick_up_object(speed)


def find_and_pick_up_clockwise(speed):
    robot = rosebot.RoseBot()
    robot.drive_system.go(speed, -speed)
    while True:
        if robot.sensor_system.camera.get_biggest_blob().center.x > 160 and robot.sensor_system.camera.get_biggest_blob().center.x < 180:
            robot.drive_system.stop()
            break
    pick_up_object(speed)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()