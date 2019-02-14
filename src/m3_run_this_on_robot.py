"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Haiden Smith.
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
    real_thing()
    # turn_off_leds()
    # color_leds()
    # cycle()
    # pick_up_object_with_cycles(50)

def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(.01)
        if delegate.is_time_to_stop:
            break


def turn_off_leds():
    robot = rosebot.RoseBot()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_off()


def turn_on_leds():
    robot = rosebot.RoseBot()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_on()


def color_leds():
    robot = rosebot.RoseBot()
    robot.led_system.left_led.set_color_by_name(robot.led_system.left_led.GREEN)
    robot.led_system.right_led.set_color_by_name(robot.led_system.right_led.ORANGE)


def turn_on_left():
    robot = rosebot.RoseBot()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()


def turn_on_right():
    robot = rosebot.RoseBot()
    robot.led_system.right_led.turn_on()


def cycle():
    # n = 3
    # for k in range(5):
    turn_on_left()
    turn_on_right()
    turn_off_leds()
    #     print(k+1, end='')
    #     time.sleep(n)
    #     n = n - 0.5
    # print("all done")


def pick_up_object_with_cycles(speed):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(speed, speed)
    while True:
        cycle()
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


def pick_up_object_beep(speed):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(speed, speed)
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


def run_follow_a_color():
    robot = rosebot.RoseBot()
    speed = 50
    saved_x = robot.sensor_system.camera.get_biggest_blob().center.x
    saved_area = robot.sensor_system.camera.get_biggest_blob().get_area()
    while True:
        if saved_x < robot.sensor_system.camera.get_biggest_blob().center.x:
            robot.drive_system.go(-speed, speed)
        if saved_x < robot.sensor_system.camera.get_biggest_blob().center.x:
            robot.drive_system.go(speed, -speed)
        if saved_x == robot.sensor_system.camera.get_biggest_blob().center.x:
            robot.drive_system.stop()

        if saved_area < robot.sensor_system.camera.get_biggest_blob().get_area():
            robot.drive_system.go(speed, speed)
        if saved_area > robot.sensor_system.camera.get_biggest_blob().get_area():
            robot.drive_system.go(-speed, -speed)
        if saved_area == robot.sensor_system.camera.get_biggest_blob().get_area():
            robot.drive_system.stop()
        saved_x = robot.sensor_system.camera.get_biggest_blob().center.x
        saved_area = robot.sensor_system.camera.get_biggest_blob().get_area()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()