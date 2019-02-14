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
    run_test_calibrate()
    # run_test_move_rose_to_position()
    # run_test_lower_arm()
    # real_thing()
    # run_test_go_straight_for_seconds()
    # run_test_go_straight_for_inches_using_time()
    # run_test_go_straight_for_inches_using_encoder()
    # run_test_display_camera_data()
    # run_test_turn_clockwise_object_spotted()
    # run_test_turn_counter_clockwise_object_spotted()
    # run_test_make_tones_and_pickup(440, 30)
    # robot = rosebot.RoseBot()
    # robot.arm_and_claw.calibrate_arm()
    # run_follow_a_color()
    # run_feature_10()

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

def run_test_display_camera_data():
    robot = rosebot.RoseBot()
    robot.drive_system.display_camera_data()


def run_test_turn_clockwise_object_spotted():
    robot = rosebot.RoseBot()
    robot.drive_system.spin_clockwise_until_sees_object(50, 50)


def run_test_turn_counter_clockwise_object_spotted():
    robot = rosebot.RoseBot()
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 25)


def run_test_make_tones_and_pickup(freq, delta):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    dur = 300
    robot.drive_system.go(25, 25)
    dist = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        robot.sound_system.tone_maker.play_tone(freq, dur)
        time.sleep(0.3)
        if dist <= robot.sensor_system.ir_proximity_sensor.get_distance_in_inches():
            freq = freq - delta
        if dist >= robot.sensor_system.ir_proximity_sensor.get_distance_in_inches():
            freq = freq + delta
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
            robot.drive_system.stop()
            robot.drive_system.go_straight_for_inches_using_encoder(4, 25)
            robot.arm_and_claw.move_arm_to_position(3000)
            break
        dist = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()


def run_feature_10():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.spin_counterclockwise_until_sees_object(-50, 400)
    run_test_make_tones_and_pickup(440, 10)

def run_follow_a_color():
    robot = rosebot.RoseBot()
    speed = 50
    while True:

        if 1500 > robot.sensor_system.camera.get_biggest_blob().get_area():
            print('forward')
            robot.drive_system.go(speed, speed)
            while True:
                if 1500 < robot.sensor_system.camera.get_biggest_blob().get_area():
                    break
        if 2500 < robot.sensor_system.camera.get_biggest_blob().get_area():
            print('backward')
            robot.drive_system.go(-speed, -speed)
            while True:
                if 2500 > robot.sensor_system.camera.get_biggest_blob().get_area():
                    break
        if robot.sensor_system.camera.get_biggest_blob().center.x > 180:
            print('turnright')
            robot.drive_system.go(speed,0)
            while True:
                if robot.sensor_system.camera.get_biggest_blob().center.x < 180:
                    break
        if robot.sensor_system.camera.get_biggest_blob().center.x < 75:
            print('turnleft')
            robot.drive_system.go(0,speed)
            while True:
                if robot.sensor_system.camera.get_biggest_blob().center.x > 75:
                    break
        else:
            robot.drive_system.stop()
            print('stop')

        # if robot.sensor_system.camera.get_biggest_blob().is_against_left_edge():
        #     robot.drive_system.go(-speed, speed)
        # if robot.sensor_system.camera.get_biggest_blob().is_against_right_edge():
        #     robot.drive_system.go(speed, -speed)

        # print(robot.sensor_system.camera.get_biggest_blob())
        # time.sleep(0.1)
        # time.sleep(0.5)
        # print(saved_area)
        # print(saved_x)
        # if saved_x < robot.sensor_system.camera.get_biggest_blob().center.x:
        #     robot.drive_system.go(-speed, speed)
        # if saved_x < robot.sensor_system.camera.get_biggest_blob().center.x:
        #     robot.drive_system.go(speed, -speed)
        # if saved_x == robot.sensor_system.camera.get_biggest_blob().center.x:
        #     robot.drive_system.stop()
        # time.sleep(0.1)
        # if saved_area < robot.sensor_system.camera.get_biggest_blob().get_area():
        #     print('backward')
        #     robot.drive_system.go(-speed, -speed)
        # time.sleep(0.1)
        # if saved_area > robot.sensor_system.camera.get_biggest_blob().get_area():
        #     print('forward')
        #     robot.drive_system.go(speed, speed)
        # else:
        #     robot.drive_system.stop()
        # saved_x = robot.sensor_system.camera.get_biggest_blob().center.x
        # saved_area = robot.sensor_system.camera.get_biggest_blob().get_area()
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()