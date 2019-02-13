"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Haiden Smith, Alex Wolfe, Alex, Tabuyo
  Winter term, 2018-2019.
"""

class Handler(object):
    def __init__(self, robot):
        self.robot = robot
        self.is_time_to_stop = False
        """
        :type robot: rosebot.RoseBot
        """

    def forward(self, left_wheel_speed, right_wheel_speed):
        print('got forward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))
 
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

