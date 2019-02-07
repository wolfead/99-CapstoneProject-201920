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

        """
        :type robot: rosebot.RoseBot
        """

    def forward(self, left_wheel_speed, right_wheel_speed):
        print('got forward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))
