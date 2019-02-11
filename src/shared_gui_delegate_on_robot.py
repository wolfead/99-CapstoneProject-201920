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
        self.robot.sound_system.beep_number_of_times(int(n))

    def tone(self, freq, dur):
        self.robot.sound_system.play_tone(int(freq), int(dur))

    def speech(self, s):
        self.robot.sound_system.speak_phrase(s)

    def quit(self):
        self.is_time_to_stop = True
