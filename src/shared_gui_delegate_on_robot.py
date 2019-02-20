"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Haiden Smith, Alex Wolfe, Alex, Tabuyo
  Winter term, 2018-2019.
"""
import time
import mqtt_remote_method_calls as com


class Handler(object):
    def __init__(self, robot):
        self.robot = robot
        self.is_time_to_stop = False
        self.mqtt_robot_sender = com.MqttClient(robot)
        self.mqtt_robot_sender.connect_to_pc()

        """
        :type robot: rosebot.RoseBot
        """

    def forward(self, left_wheel_speed, right_wheel_speed):
        print('got forward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def m1forward(self, left_wheel_speed, right_wheel_speed):
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 4:
            self.speech('I am too close to the wall')
        else:
            self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))
            print('Going Forward')


    def m1backward(self, left_motor_speed, right_motor_speed):

        self.robot.drive_system.right_motor.turn_on(-(int(left_motor_speed)))
        self.robot.drive_system.left_motor.turn_on(-(int(right_motor_speed)))
        print('Going backwards')

    def m1left(self,left_speed, right_speed):

        self.robot.drive_system.left_motor.turn_on(-(int(left_speed)))
        self.robot.drive_system.right_motor.turn_on(int(right_speed))
        print('Turning Left')

    def m1right(self, left_speed, right_speed):

        self.robot.drive_system.left_motor.turn_on(int(left_speed))
        self.robot.drive_system.right_motor.turn_on(-(int(right_speed)))
        print('Turning Right')

    def remember_colors(self):
        list = ''
        self.robot.drive_system.go(30,30)
        initialcolor = None
        while True:
            color_number_encountered = self.robot.sensor_system.color_sensor.get_color()
            x = self.robot.sensor_system.color_sensor.COLORS[color_number_encountered]
            if x!= initialcolor:
                list = list + ' ' + x
                initialcolor = x
            if self.robot.sensor_system.touch_sensor.is_pressed():
                break
            time.sleep(0.7)
        self.robot.drive_system.stop()
        print(list)
        self.speech(list)

    def stop(self):
        self.robot.drive_system.right_motor.turn_off()
        self.robot.drive_system.left_motor.turn_off()

    def backward(self, left_motor_speed, right_motor_speed):
        self.robot.drive_system.right_motor.turn_on(-(int(left_motor_speed)))
        self.robot.drive_system.left_motor.turn_on(-(int(right_motor_speed)))

    def left(self, left_speed, right_speed):
        self.robot.drive_system.left_motor.turn_on(-(int(left_speed)))
        self.robot.drive_system.right_motor.turn_on(int(right_speed))

    def right(self, left_speed, right_speed):
        self.robot.drive_system.left_motor.turn_on(int(left_speed))
        self.robot.drive_system.right_motor.turn_on(-(int(right_speed)))

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def go_forward_for_seconds(self, seconds, speed):
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def go_inches_using_time(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to(self, desired_arm_position):
        self.robot.arm_and_claw.move_arm_to_position(int(desired_arm_position))

    def beep_n(self, n):
        for k in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, freq, dur):
        self.robot.sound_system.tone_maker.play_tone(int(freq), int(dur)).wait()

    def speech(self, s):
        print('speaking')
        self.robot.sound_system.speech_maker.speak(s).wait()

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity, int(speed)))

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity), int(speed))

    def go_straight_until_color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(color, int(speed))

    def go_straight_until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, int(speed))

    def go_forward_until_distance_is_less_than(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))

    def go_until_distance_is_within(self, delta, inches, speed):
        self.robot.drive_system.go_until_distance_is_within(int(delta), int(inches), int(speed))

    def spin_clockwise_until_beacon_heading_is_nonnegative(self, speed):
        self.robot.drive_system.spin_clockwise_until_beacon_heading_is_nonnegative(int(speed))

    def spin_counterclockwise_until_beacon_heading_is_nonpositive(self, speed):
        self.robot.drive_system.spin_counterclockwise_until_beacon_heading_is_nonpositive(int(speed))

    def go_straight_to_the_beacon(self, inches, speed):
        self.robot.drive_system.go_straight_to_the_beacon(int(inches), int(speed))

    def display_camera_data(self):
        pass

    def spin_clockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def spin_counterclockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))

    def turn_off_leds(self):
        self.robot.led_system.right_led.turn_off()
        self.robot.led_system.left_led.turn_off()

    def turn_on_left(self):
        self.robot.led_system.left_led.turn_on()

    def turn_on_right(self):
        self.robot.led_system.right_led.turn_on()

    def cycle(self):
        self.robot.led_system.left_led.turn_on().wait()
        self.robot.led_system.right_led.turn_on().wait()
        self.robot.led_system.right_led.turn_off().wait()
        self.robot.led_system.left_led.turn_off().wait()

    def pick_up_object_beeper(self, speed):
        self.robot.arm_and_claw.calibrate_arm()
        self.robot.drive_system.go(int(speed), int(speed))
        beeper = self.robot.sound_system.beeper
        while True:
            beeper.beep()
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
                self.robot.drive_system.stop()
                break
            data1 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            time.sleep(0.01)
            data2 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            time.sleep(0.01)
            data3 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            avg = (data1 + data2 + data3) / 3
            time.sleep(0.01 * (1 + avg))
        self.robot.drive_system.go_straight_for_inches_using_encoder(3, int(speed))
        self.robot.arm_and_claw.move_arm_to_position(4000)
        self.robot.drive_system.stop()

    def find_and_pick_up_counterclockwise(self, speed):
        self.robot.drive_system.go(-int(speed), int(speed))
        while True:
            if 150 < self.robot.sensor_system.camera.get_biggest_blob().center.x < 165:
                self.robot.drive_system.stop()
                break
        self.robot.arm_and_claw.calibrate_arm()
        self.robot.drive_system.go(int(speed), int(speed))
        beeper = self.robot.sound_system.beeper
        while True:
            beeper.beep()
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
                self.robot.drive_system.stop()
                break
            data1 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            time.sleep(0.01)
            data2 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            time.sleep(0.01)
            data3 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            avg = (data1 + data2 + data3) / 3
            time.sleep(0.01 * (1 + avg))
        self.robot.drive_system.go_straight_for_inches_using_encoder(3, int(speed))
        self.robot.arm_and_claw.move_arm_to_position(4000)
        self.robot.drive_system.stop()

    def find_and_pick_up_clockwise(self, speed):
        self.robot.drive_system.go(int(speed), -int(speed))
        while True:
            if 150 < self.robot.sensor_system.camera.get_biggest_blob().center.x < 165 :
                self.robot.drive_system.stop()
                break
        self.robot.arm_and_claw.calibrate_arm()
        self.robot.drive_system.go(int(speed), int(speed))
        beeper = self.robot.sound_system.beeper
        while True:
            beeper.beep()
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
                self.robot.drive_system.stop()
                break
            data1 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            time.sleep(0.01)
            data2 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            time.sleep(0.01)
            data3 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            avg = (data1 + data2 + data3) / 3
            time.sleep(0.01 * (1 + avg))
        self.robot.drive_system.go_straight_for_inches_using_encoder(3, int(speed))
        self.robot.arm_and_claw.move_arm_to_position(4000)
        self.robot.drive_system.stop()

    def pick_up_object_with_cycles(self, speed):
        self.robot.arm_and_claw.calibrate_arm()
        self.robot.drive_system.go(int(speed), int(speed))
        while True:
            self.robot.led_system.left_led.turn_on().wait()
            self.robot.led_system.right_led.turn_on().wait()
            self.robot.led_system.right_led.turn_off().wait()
            self.robot.led_system.left_led.turn_off().wait()
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
                self.robot.drive_system.stop()
                break
            data1 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            time.sleep(0.01)
            data2 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            time.sleep(0.01)
            data3 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
            avg = (data1 + data2 + data3) / 3
            time.sleep(0.01 * (1 + avg))
        self.robot.drive_system.go_straight_for_inches_using_encoder(3, int(speed))
        self.robot.arm_and_claw.move_arm_to_position(4000)
        self.robot.drive_system.stop()

    def run_follow_a_color(self):
        speed = 50
        saved_x = self.robot.sensor_system.camera.get_biggest_blob().center.x
        saved_area = self.robot.sensor_system.camera.get_biggest_blob().get_area()
        while True:
            if saved_x < self.robot.sensor_system.camera.get_biggest_blob().center.x:
                self.robot.drive_system.go(-int(speed), int(speed))
            if saved_x < self.robot.sensor_system.camera.get_biggest_blob().center.x:
                self.robot.drive_system.go(int(speed), -int(speed))
            if saved_x == self.robot.sensor_system.camera.get_biggest_blob().center.x:
                self.robot.drive_system.stop()

            if saved_area < self.robot.sensor_system.camera.get_biggest_blob().get_area():
                self.robot.drive_system.go(int(speed), int(speed))
            if saved_area > self.robot.sensor_system.camera.get_biggest_blob().get_area():
                self.robot.drive_system.go(-int(speed), -int(speed))
            if saved_area == self.robot.sensor_system.camera.get_biggest_blob().get_area():
                self.robot.drive_system.stop()
            saved_x = self.robot.sensor_system.camera.get_biggest_blob().center.x
            saved_area = self.robot.sensor_system.camera.get_biggest_blob().get_area()

    def make_tones_and_pickup(self, freq, delta):
        self.robot.arm_and_claw.calibrate_arm()
        dur = 300
        self.robot.drive_system.go(25, 25)
        dist = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        while True:
            self.robot.sound_system.tone_maker.play_tone(int(freq), int(dur))
            time.sleep(0.3)
            if dist <= self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches():
                freq = int(freq) - int(delta)
            if dist >= self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches():
                freq = int(freq) + int(delta)
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
                self.robot.drive_system.stop()
                self.robot.drive_system.go_straight_for_inches_using_encoder(4, 25)
                self.robot.arm_and_claw.move_arm_to_position(3000)
                break
            dist = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

# ###################################### HAIDEN'S FINAL CODE ##########################################################
    def mario_forward(self, speed):
        self.robot.drive_system.go(int(speed), int(speed))
        n = 1000
        while True:
            if self.robot.sensor_system.color_sensor.get_color() == 5:
                self.robot.drive_system.stop()
                for k in range(3):
                    self.robot.sound_system.tone_maker.play_tone(n, 2000)
                    n = n - 200
                self.robot.sound_system.speech_maker.speak("Oh no you lost")
                # self.mqtt_robot_sender.connect_to_pc()
                # self.mqtt_robot_sender.send_message('window_one')
                break

            if self.robot.sensor_system.color_sensor.get_color() == 3:
                self.robot.drive_system.go(int(speed), int(speed))
                beeper = self.robot.sound_system.beeper
                while True:
                    beeper.beep()
                    if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
                        self.robot.drive_system.stop()
                        break
                    data1 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
                    time.sleep(0.01)
                    data2 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
                    time.sleep(0.01)
                    data3 = self.robot.sensor_system.ir_proximity_sensor.get_distance()
                    avg = (data1 + data2 + data3) / 3
                    time.sleep(0.01 * (1 + avg))
                self.robot.drive_system.go_straight_for_inches_using_encoder(3, int(speed))
                self.robot.arm_and_claw.raise_arm()
                self.robot.drive_system.stop()

                if self.robot.sensor_system.touch_sensor.is_pressed:
                    self.robot.sound_system.speech_maker.speak('Ya Who Its uh me mario')
                    # self.mqtt_robot_sender.connect_to_pc()
                    # self.mqtt_robot_sender.send_message('window_two')
                    break

    def cup_remover(self, speed, table):
        self.robot.drive_system.go(int(speed), -int(speed))
        self.mqtt_robot_sender.connect_to_pc()
        color = self.robot.sensor_system.color_sensor.get_color()
        count = 0
        while True:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > int(table) / 2:
                self.robot.drive_system.go(int(speed), -int(speed))
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < int(table) / 2:
                self.robot.drive_system.go(int(speed) / 2, int(speed) / 2)
                print('retrieving')
                if self.robot.sensor_system.camera.get_biggest_blob().get_area() > 400:
                    while True:
                        self.robot.drive_system.stop()
                        self.robot.sound_system.speech_maker.speak('Sorry')
                        self.robot.drive_system.go(-int(speed), -int(speed))
                        time.sleep(1.5)
                        break

                # if color != self.robot.sensor_system.color_sensor.get_color():
                #     self.robot.sound_system.speech_maker.speak('Out of Bounds!')
                #     self.robot.drive_system.go(-int(speed), -int(speed))
                #     time.sleep(0.5)
                #     self.robot.drive_system.stop()
                #     self.robot.drive_system.go(int(speed), -int(speed))
                #     time.sleep(1)
                #     self.robot.drive_system.stop()
                #     self.robot.drive_system.go(int(speed), int(speed))
                #     break
                if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 3:
                    print('Object Found!')
                    self.robot.arm_and_claw.lower_arm()
                    self.robot.drive_system.go_straight_for_inches_using_encoder(5, int(speed) / 2)
                    self.robot.arm_and_claw.move_arm_to_position(3500)
                    self.robot.drive_system.go(int(speed) / 2, int(speed) / 2)
                    while True:
                        if color != self.robot.sensor_system.color_sensor.get_color():
                            count = count + 1
                            self.robot.drive_system.stop()
                            self.robot.arm_and_claw.lower_arm()
                            self.robot.sound_system.speech_maker.speak('All done!')
                            self.robot.drive_system.go(-int(speed) / 2, -int(speed) / 2)
                            time.sleep(2)
                            self.robot.drive_system.stop()
                            self.mqtt_robot_sender.send_message('print_cup_count', count)
                            break


