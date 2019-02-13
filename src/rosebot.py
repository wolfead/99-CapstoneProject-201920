"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Alex Wolfe, Alexander Tabuyo, Haiden Smith.
  Winter term, 2018-2019.
"""

import ev3dev.ev3 as ev3
import time
import math


###############################################################################
#    RoseBot class.
#
# NOTE TO STUDENTS:
#   You should construct a RoseBot for the Snatch3r robot.
#   Do ** NOT ** construct any instances of any other classes in this module,
#   since a RoseBot constructs instances of all the sub-systems that provide
#   ALL of the functionality available to a Snatch3r robot.
#
#   Use those sub-systems (and their instance variables)
#   to make the RoseBot (and its associated Snatch3r robot) do things.
###############################################################################
class RoseBot(object):
    def __init__(self):
        # Use these instance variables
        self.sensor_system = SensorSystem()
        self.sound_system = SoundSystem()
        self.led_system = LEDSystem()
        self.drive_system = DriveSystem(self.sensor_system)
        self.arm_and_claw = ArmAndClaw(self.sensor_system.touch_sensor)
        self.beacon_system = BeaconSystem()
        self.display_system = DisplaySystem()

###############################################################################
#    DriveSystem
###############################################################################
class DriveSystem(object):
    """
    Controls the robot's motion via GO and STOP methods,
        along with various methods that GO/STOP under control of a sensor.
    """
    # -------------------------------------------------------------------------
    # NOTE:
    #   Throughout, when going straight:
    #     -- Positive speeds should make the robot move forward.
    #     -- Negative speeds should make the robot move backward.
    #   Throughout, when spinning:
    #     -- Positive speeds should make the robot spin in place clockwise
    #          (i.e., left motor goes at speed S, right motor at speed -S).
    #     -- Negative speeds should make the robot spin in place
    #          counter-clockwise
    #          (i.e., left motor goes at speed -S, right motor at speed S).
    # -------------------------------------------------------------------------

    def __init__(self, sensor_system):
        """
        Stores the given SensorSystem object.
        Constructs two Motors (for the left and right wheels).
          :type sensor_system:  SensorSystem
        """
        self.sensor_system = sensor_system
        self.left_motor = Motor('B')
        self.right_motor = Motor('C')

        self.wheel_circumference = 1.3 * math.pi

    # -------------------------------------------------------------------------
    # Methods for driving with no external sensor (just the built-in encoders).
    # -------------------------------------------------------------------------

    def go(self, left_wheel_speed, right_wheel_speed):
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(right_wheel_speed)

    def stop(self):
        """ Stops the left and right wheel motors. """
        self.left_motor.turn_off()
        self.right_motor.turn_off()

    def go_straight_for_seconds(self, seconds, speed):
        """
        Makes the robot go straight (forward if speed > 0, else backward)
        at the given speed for the given number of seconds.
        """
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()

    def go_straight_for_inches_using_time(self, inches, speed):
        """
        Makes the robot go straight at the given speed
        for the given number of inches, using the approximate
        conversion factor of 10.0 inches per second at 100 (full) speed.
        """
        # NOTE to students:  The constant and formula below are not accurate
        seconds_per_inch_at_100 = 10.0  # 1 sec = 10 inches at 100 speed
        seconds = abs(inches * seconds_per_inch_at_100 / speed)

        self.go_straight_for_seconds(seconds, speed)

    def go_straight_for_inches_using_encoder(self, inches, speed):
        """
        Makes the robot go straight (forward if speed > 0, else backward)
        at the given speed for the given number of inches,
        using the encoder (degrees traveled sensor) built into the motors.
        """
        self.left_motor.reset_position()
        self.right_motor.reset_position()
        inches_per_degree = self.wheel_circumference / 360
        degrees_to_move = inches // inches_per_degree
        self.left_motor.turn_on(speed)
        self.right_motor.turn_on(speed)
        while True:
            self.left_motor.get_position()
            if abs(self.left_motor.get_position()) >= degrees_to_move:
                self.left_motor.turn_off()
                self.right_motor.turn_off()
                break

    # -------------------------------------------------------------------------
    # Methods for driving that use the color sensor.
    # -------------------------------------------------------------------------

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        """
        Goes straight at the given speed until the intensity returned
        by the color_sensor is less than the given intensity.
        """
        self.left_motor.turn_on(speed)
        self.right_motor.turn_on(speed)
        color_sensor = ColorSensor(3)
        while True:
            if color_sensor.get_reflected_light_intensity() < intensity:
                self.left_motor.turn_off()
                self.right_motor.turn_off()
                break

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        """
        Goes straight at the given speed until the intensity returned
        by the color_sensor is greater than the given intensity.
        """
        self.left_motor.turn_on(speed)
        self.right_motor.turn_on(speed)
        color_sensor = ColorSensor(3)
        while True:
            if color_sensor.get_reflected_light_intensity() > intensity:
                self.left_motor.turn_off()
                self.right_motor.turn_off()
                break

    def go_straight_until_color_is(self, color, speed):
        """
        Goes straight at the given speed until the color returned
        by the color_sensor is equal to the given color.

        Colors can be integers from 0 to 7 or any of the strings
        listed in the ColorSensor class.

        If the color is an integer (int), then use the  get_color   method
        to access the color sensor's color.  If the color is a string (str),
        then use the   get_color_as_name   method to access
        the color sensor's color.
        """
        self.go(speed, speed)
        color_number = self.sensor_system.color_sensor.get_color_number_from_color_name(color)
        while True:
            if self.sensor_system.color_sensor.get_color() == color_number:
                self.stop()
                break

    def go_straight_until_color_is_not(self, color, speed):
        """
         Goes straight at the given speed until the color returned
        by the color_sensor is NOT equal to the given color.

        Colors can be integers from 0 to 7 or any of the strings
        listed in the ColorSensor class.
        """
        self.go(speed,speed)
        color_number = self.sensor_system.color_sensor.get_color_number_from_color_name(color)
        while True:
            if self.sensor_system.color_sensor.get_color() != color_number:
                self.stop()
                break

    # -------------------------------------------------------------------------
    # Methods for driving that use the infrared proximity sensor.
    # -------------------------------------------------------------------------
    def go_forward_until_distance_is_less_than(self, inches, speed):
        """
        Goes forward at the given speed until the robot is less than
        the given number of inches from the nearest object that it senses.
        """
        self.go(speed, speed)
        while True:
            if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= inches:
                self.stop()
                break

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        """
        Goes straight at the given speed until the robot is greater than
        the given number of inches from the nearest object that it senses.
        Assumes that it senses an object when it starts.
        """
        self.go(-speed, -speed)
        while True:
            time.sleep(0.1)
            if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= inches:
                self.stop()
                break
    def go_until_distance_is_within(self, delta, inches, speed):
        """
         Goes forward or backward, repeated as necessary, until the robot is
        within the given delta of the given inches from the nearest object
        that it senses.  Assumes that it senses an object when it starts.

        For example, if delta is 0.3 and inches is 7.1, then
        the robot should move until it is between 6.8 and 7.4 inches
        from the object.
        """
        if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() > (inches + delta):
            self.go(speed, speed)
        elif self.sensor_system.ir_proximity_sensor.get_distance_in_inches() < (inches - delta):
            self.go(-speed, -speed)
        while True:
            time.sleep(0.1)
            if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() < (inches + delta) and self.sensor_system.ir_proximity_sensor.get_distance_in_inches() > (inches - delta):
                self.stop()
                break
    # -------------------------------------------------------------------------
    # Methods for driving that use the infrared beacon sensor.
    # -------------------------------------------------------------------------

    def spin_clockwise_until_beacon_heading_is_nonnegative(self, speed):
        """
        Spins clockwise at the given speed until the heading to the Beacon
        is nonnegative.  Requires that the user turn on the Beacon.
        """
        pass
    def spin_counterclockwise_until_beacon_heading_is_nonpositive(self, speed):
        """
        Spins counter-clockwise at the given speed until the heading to the Beacon
        is nonnegative.  Requires that the user turn on the Beacon.
        """
        pass
    def go_straight_to_the_beacon(self, inches, speed):
        """
        Goes forward at the given speed until the robot is less than the
        given number of inches from the Beacon.
        Assumes that the Beacon is turned on and placed straight ahead.
        """
        pass
    # -------------------------------------------------------------------------
    # Methods for driving that use the camera.
    # -------------------------------------------------------------------------
    def display_camera_data(self):
        """
        Displays on the GUI the Blob data of the Blob that the camera sees
        (if any).
        """
        print(self.sensor_system.camera.get_biggest_blob())

    def spin_clockwise_until_sees_object(self, speed, area):
        """
        Spins clockwise at the given speed until the camera sees an object
        of the trained color whose area is at least the given area.
        Requires that the user train the camera on the color of the object.
        """
        self.go(speed, -speed)
        while True:
            h = self.sensor_system.camera.get_biggest_blob().height
            w = self. sensor_system.camera.get_biggest_blob().width
            a = h * w
            if a >= area:
                self.stop()
                break

    def spin_counterclockwise_until_sees_object(self, speed, area):
        """
        Spins counter-clockwise at the given speed until the camera sees an object
        of the trained color whose area is at least the given area.
        Requires that the user train the camera on the color of the object.
        """
        self.go(-speed, speed)
        while True:
            h = self.sensor_system.camera.get_biggest_blob().height
            w = self. sensor_system.camera.get_biggest_blob().width
            a = h * w
            if a >= area:
                self.stop()
                break

###############################################################################
#    ArmAndClaw
###############################################################################
class ArmAndClaw(object):
    """ Controls the robot's arm and claw (which operate together). """
    # -------------------------------------------------------------------------
    # NOTE:
    #   A POSITIVE speed for the ArmAndClaw's motor moves the arm UP.
    #   A NEGATIVE speed for the ArmAndClaw's motor moves the arm DOWN.
    #   It takes   14.2 revolutions    of the ArmAndClaw's motor
    #     to go from all the way UP to all the way DOWN.
    # -------------------------------------------------------------------------

    def __init__(self, touch_sensor):
        """
        Stores the given touch sensor for stopping the Arm in its UP position.
        Constructs the Arm's motor.
          :type  touch_sensor:  TouchSensor
        """
        self.touch_sensor = touch_sensor
        self.motor = Motor('A', motor_type='medium')

    def raise_arm(self):
        """ Raises the Arm until its touch sensor is pressed. """
        self.motor.turn_on(100)
        while True:
            if self.touch_sensor.is_pressed():
                self.motor.turn_off()
                break

    def calibrate_arm(self):
        """
        Calibrates its Arm, that is:
          1. Raises its Arm until it is all the way UP
               (i.e., its touch sensor is pressed)
          2. Lowers its Arm until it is all the way down
               (i.e., 14.2 motor revolutions),
          3. Resets the motor's position to 0.
        """
        print('calibrate_arm')
        self.raise_arm()
        self.motor.reset_position()
        self.motor.turn_on(-100)
        while True:
            if abs(self.motor.get_position()) >= (14.1 * 360):
                self.motor.turn_off()
                self.motor.reset_position()
                print(self.motor.get_position(), "should be in move arm now")
                break
    
    def move_arm_to_position(self, desired_arm_position):
        """
        Move its Arm to the given position, where 0 means all the way DOWN.
        The robot must have previously calibrated its Arm.
        """
        # self.calibrate_arm()
        print('move arm to position')
        self.motor.turn_on(100)
        print(desired_arm_position)
        while True:
            if self.motor.get_position() >= desired_arm_position:
                self.motor.turn_off()
                break

    def lower_arm(self):
        """
        Lowers the Arm until it is all the way down, i.e., position 0.
        The robot must have previously calibrated its Arm.
        """
        self.motor.turn_on(-100)
        while True:
            if self.motor.get_position() <= 3:
                self.motor.turn_off()
                break

###############################################################################
#    SensorSystem
###############################################################################
class SensorSystem(object):
    """
    Has all the sensor objects available to the Snatch3r robot, including
    the Button objects that form part of the BeaconSystem and DisplaySystem.
    Use this object to get   ** any **   sensor reading.
    """

    def __init__(self):
        self.touch_sensor = TouchSensor(1)
        self.color_sensor = ColorSensor(3)
        self.ir_proximity_sensor = InfraredProximitySensor(4)
        self.camera = Camera()
        # self.ir_beacon_sensor = InfraredBeaconSensor(4)
        # self.beacon_system =
        # self.display_system =



###############################################################################
#    SoundSystem
###############################################################################
class SoundSystem(object):
    """
    Has all the kinds of "noise makers" available to the Snatch3r robot.
    Use this object to make   ** any **   sounds.
    """

    def __init__(self):
        self.beeper = Beeper()
        self.tone_maker = ToneMaker()
        self.speech_maker = SpeechMaker()
        self.song_maker = SongMaker()


###############################################################################
#    LEDSystem
###############################################################################
class LEDSystem(object):
    """
    Has the left and right LEDs on the Brick.
    """

    def __init__(self):
        """ Constructs and stores the left and right LED objects. """
        self.left_led = LED("left")
        self.right_led = LED("right")


###############################################################################
#    BeaconSystem
###############################################################################
class BeaconSystem(object):
    pass


###############################################################################
#    DisplaySystem
###############################################################################
class DisplaySystem(object):
    pass


###############################################################################
###############################################################################
# Classes built directly upon the underlying EV3 robot modules.
# USE them, and AUGMENT them if you wish, but do NOT modify them.
#
# In the DriveSystem:
#   -- Motor
#
# Sensors in the SensorSystem:
#   -- TouchSensor (also used in the ArmAndClaw)
#   -- ColorSensor
#   -- InfraredProximitySensor
#   -- InfraredBeaconSensor
#   -- Camera
#
# In the SoundSystem:
#   -- Beeper
#   -- ToneMaker
#   -- SpeechMaker
#   -- SongPlayer
#
###############################################################################
###############################################################################


###############################################################################
# -----------------------------------------------------------------------------
# DriveSystem classes
# -----------------------------------------------------------------------------
###############################################################################

###############################################################################
# Motor
###############################################################################
class Motor(object):
    # Future enhancements: Add additional methods from the many things
    # an ev3.Motor can do.

    def __init__(self, port, motor_type='large'):
        # port must be 'A', 'B', 'C', or 'D'.  Use 'arm' as motor_type for Arm.
        if motor_type == 'large':
            self._motor = ev3.LargeMotor('out' + port)
        elif motor_type == 'medium':
            self._motor = ev3.MediumMotor('out' + port)

    def turn_on(self, speed):  # speed must be -100 to 100
        self._motor.run_direct(duty_cycle_sp=speed)

    def turn_off(self):
        self._motor.stop(stop_action="brake")

    def get_position(self):  # Units are degrees (that the motor has rotated).
        return self._motor.position

    def reset_position(self):
        self._motor.position = 0


###############################################################################
# -----------------------------------------------------------------------------
# SensorSystem classes
# -----------------------------------------------------------------------------
###############################################################################

###############################################################################
# Touch Sensor
###############################################################################
class TouchSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._touch_sensor = ev3.TouchSensor('in' + str(port))

    def is_pressed(self):
        """ Returns True if this TouchSensor is pressed, else returns False """
        return self._touch_sensor.is_pressed


###############################################################################
# ColorSensor
###############################################################################
class ColorSensor(object):
    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._color_sensor = ev3.ColorSensor('in' + str(port))
        self.COLORS = (
            'NoColor',
            'Black',
            'Blue',
            'Green',
            'Yellow',
            'Red',
            'White',
            'Brown',
        )
        self.COLOR_NUMBERS = {
            'NoColor': 0,
            'Black': 1,
            'Blue': 2,
            'Green': 3,
            'Yellow': 4,
            'Red': 5,
            'White': 6,
            'Brown': 7,
        }

    def get_reflected_light_intensity(self):
        """
        Shines red light and returns the intensity of the reflected light.
        The returned value is from 0 to 100,
        but in practice more like 3 to 90+ in our classroom lighting with our
        downward-facing sensor that is about 0.25 inches from the ground.
        """
        return self._color_sensor.reflected_light_intensity

    def get_ambient_light_intensity(self):
        """
        Shines dimly lit blue light and returns the intensity
        of the ambient light.  The returned value is from 0 to 100.
        """
        return self._color_sensor.ambient_light_intensity

    def get_color(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is an integer between
        0 and 7, where the meanings of the integers are:
          - 0: No color
                  (that is, cannot classify the color as one of the following)
          - 1: Black
          - 2: Blue
          - 3: Green
          - 4: Yellow
          - 5: Red
          - 6: White
          - 7: Brown
        """
        return self._color_sensor.color


    def get_color_as_name(self):
        """
        Same as  get_color  but returns the color as a STRING, in particular,
        as one of the strings listed in the doc-string for get_color.
        """
        return self.COLORS[self.get_color()]

    def get_color_number_from_color_name(self, color_name):
        """
        Returns the color NUMBER associated with the given color NAME.
        The color_name must be one of the 7 strings
        listed in the doc-string for get_color.
        """
        return self.COLOR_NUMBERS[color_name]

    def get_raw_color(self):
        """
        Shines red, then green, then blue light down.  Returns the reflected
        intensities of each, with each in the range 0-1020.
        Example usage:
            red, green, blue = color_sensor.get_raw_color
        """


###############################################################################
# InfraredProximitySensor
###############################################################################
class InfraredProximitySensor(object):
    """
    The infrared sensor when it is in the mode in which it emits infrared light
    and uses the reflected information to estimate distance to the nearest
    object in its field of vision.
    """

    def __init__(self, port):  # port must be 1, 2, 3 or 4
        self._ir_sensor = ev3.InfraredSensor('in' + str(port))

    def get_distance(self):
        """
        Returns the distance to the nearest object in its field of vision,
        as a integer between 0 and 100, where a value N indicates that the
        distance to the nearest object is 70 * (N / 100) cm.  For example:
           - numbers < 10 indicate that the object is less than 7 cm away
           - 20 means 1/5 of 70, i.e., 14 cm
           - 40 means 2/5 of 70, i.e., 28 cm
           - 50 means 1/2 of 70, i.e., 35 cm
           - greater than 70 is too far away to be useful
               (i.e., greater than 49 cm away)
           - 100 is the maximum distance for the sensor, namely, 70 cm.
        """
        return self._ir_sensor.proximity

    def get_distance_in_inches(self):
        """
        Returns the distance to the nearest object in its field of vision,
        in inches, where about 39.37 inches (which is 100 cm) means no object
        is within its field of vision.
        """
        cm_per_inch = 2.54
        distance = (48 / cm_per_inch) * self.get_distance() / 100
        print(distance)
        return distance


###############################################################################
# InfraredBeaconSensor
###############################################################################
class InfraredBeaconSensor(object):
    """
    The infrared sensor when it is in the mode in which it measures the
    heading and distance to the Beacon when the Beacon is emitting
    its signal continuously ("beacon mode") on one of its 4 channels (1 to 4).
    """

    def __init__(self, port, channel=1):  # port must be 1, 2, 3 or 4
        self.port = port
        self.channel = channel
        self._ir_sensor = ev3.BeaconSeeker('in' + str(self.port),
                                           channel=channel)

    def set_channel(self, channel):
        """
        Makes this sensor look for signals on the given channel. The physical
        Beacon has a switch that can set the channel to 1, 2, 3 or 4.
        """
        self.channel = channel
        self._ir_sensor = ev3.BeaconSeeker('in' + str(self.port),
                                           channel=channel)

    def get_channel(self):
        return self.channel

    def get_heading_and_distance_to_beacon(self):
        """
        Returns a 2-tuple containing the heading and distance to the Beacon.
        Looks for signals at the frequency of the given channel,
        or at the InfraredAsBeaconSensor's channel if channel is None.
         - The heading is in degrees in the range -25 to 25 with:
             - 0 means straight ahead
             - negative degrees mean the Beacon is to the left
             - positive degrees mean the Beacon is to the right
         - Distance is from 0 to 100, where 100 is about 70 cm
         - -128 means the Beacon is not detected.
        """
        return self._ir_sensor.heading_and_distance

    def get_heading_to_beacon(self):
        """
        Returns the heading to the Beacon.
        Units are per the   get_heading_and_distance_to_beacon   method.
        """
        return self._ir_sensor.heading

    def get_distance_to_beacon(self):
        """
        Returns the heading to the Beacon.
        Units are per the   get_heading_and_distance_to_beacon   method.
        """
        return self._ir_sensor.distance


###############################################################################
# Camera
###############################################################################
class Camera(object):
    """
    A class for a Pixy camera.
    Use the   PixyMon    program to initialize the camera's firmware.
    Download the program from the    Windows   link at:
        http://www.cmucam.org/projects/cmucam5/wiki/Latest_release

    Learn how to use the Pixy camera's "color signatures" to recognize objects
        at: http://www.cmucam.org/projects/cmucam5/wiki/Teach_Pixy_an_object.
    """

    def __init__(self, port=ev3.INPUT_2):
        try:
            self.low_level_camera = ev3.Sensor(port, driver_name="pixy-lego")
        except AssertionError:
            print("Is the camera plugged into port 2?")
            print("If that is not the problem, then check whether the camera")
            print("has gotten into 'Arduino mode', as follows:")
            print("  In PixyMon, select the gear (Configure) icon,")
            print("  then look for a tab that has 'Arduino' on its page.")
            print("  Make sure it says 'Lego' and not 'Arduino'.")
            print("Note: Only some of the cameras have this option;")
            print("the others are automatically OK in this regard.")
        self.set_signature("SIG1")

    def set_signature(self, signature_name):
        self.low_level_camera.mode = signature_name

    def get_biggest_blob(self):
        """
        A "blob" is a collection of connected pixels that are all in the color
        range specified by a color "signature".  A Blob object stores the Point
        that is the center (actually, centroid) of the blob along with the
        width and height of the blob.  For a Pixy camera, the x-coordinate is
        between 0 and 319 (0 left, 319 right) and the y-coordinate is between
        0 and 199 (0 TOP, 199 BOTTOM).  See the Blob class below.

        A Camera returns the largest Blob whose pixels fall within the Camera's
        current color signature.  A Blob whose width and height are zero
        indicates that no large enough object within the current color signature
        was visible.

        The Camera's color signature defaults to "SIG1", which is the color
        signature set by selecting the RED light when training the Pixy camera.
        """
        return Blob(Point(self.low_level_camera.value(1),
                          self.low_level_camera.value(2)),
                    self.low_level_camera.value(3),
                    self.low_level_camera.value(4))


###############################################################################
# Point (for the Camera class, as well as for general purposes.
###############################################################################
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


###############################################################################
# Blob (for the Camera class).
###############################################################################
class Blob(object):
    """
    Represents a rectangle in the form that a Pixy camera uses:
      upper-left corner along with width and height.
    """

    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height
        self.screen_limits = Point(320, 240)  # FIXME

    def __repr__(self):
        return "center: ({:3d}, {:3d})  width, height: {:3d} {:3d}.".format(
            self.center.x, self.center.y, self.width, self.height)

    def get_area(self):
        return self.width * self.height

    def is_against_left_edge(self):
        return self.center.x - (self.width + 1) / 2 <= 0

    def is_against_right_edge(self):
        return self.center.x + (self.width / 2 + 1) / 2 >= self.screen_limits.x

    def is_against_top_edge(self):
        return self.center.y - (self.height + 1) / 2 <= 0

    def is_against_bottom_edge(self):
        return self.center.y + (self.height + 1) / 2 >= self.screen_limits.y

    def is_against_an_edge(self):
        return (self.is_against_left_edge()
                or self.is_against_right_edge()
                or self.is_against_top_edge()
                or self.is_against_bottom_edge())


###############################################################################
# -----------------------------------------------------------------------------
# SoundSystem classes
# -----------------------------------------------------------------------------
###############################################################################

###############################################################################
# Beeper
###############################################################################
class Beeper(object):
    # Future enhancements: Add volume to all the SoundSystem classes.
    def __init__(self):
        self._beeper = ev3.Sound

    def beep(self):
        """
        Starts playing a BEEP sound.

        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. Returns a subprocess.Popen,
        so if you want the sound-playing to block until the sound is completed
        (e.g. if the next statement will immediately make another sound),
        then use   beep  like this:
             beeper = Beeper()
             beeper.beep().wait()

        :rtype subprocess.Popen
        """
        return self._beeper.beep()


###############################################################################
# ToneMaker
###############################################################################
class ToneMaker(object):
    def __init__(self):
        self._tone_maker = ev3.Sound

    def play_tone(self, frequency, duration):
        """
        Starts playing a tone at the given frequency (in Hz) for the given
        duration (in milliseconds).

        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. Returns a subprocess.Popen,
        so if you want the sound-playing to block until the sound is completed
        (e.g. if the next statement will immediately make another sound),
        then use   tone  like this:
             tone_player = ToneMaker()
             tone_player.play_tone(400, 500).wait()

        :rtype subprocess.Popen
        """
        return self._tone_maker.tone(frequency, duration)

    def play_tone_sequence(self, tones):
        """
        Starts playing a sequence of tones, where each tone is a 3-tuple:
          (frequency, duration, delay_until_next_tone_in_sequence)
        Does NOT block; see   play_tone  above.

        Here is a cheerful example, from the ev3 documentation::
            tone_player = ToneMaker()
            tone_player.play_tone_sequence([
        (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
        (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
        (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
        (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100),
        (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
        (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
        (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
        (554.36, 350, 100),
        (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100),
        (440, 25, 100),
        (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
        (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100),
        (392, 250, 100),
        (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100),
        (392, 250, 100),
        (392, 25, 100), (784, 350, 100), (739.98, 250, 100),
        (698.46, 25, 100),
        (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
        (415.3, 25, 200),
        (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
        (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400),
        (311.13, 25, 200),
        (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
        (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
        ]).wait()

          :rtype subprocess.Popen
        """
        return self._tone_maker.tone(tones)


###############################################################################
# SpeechMaker
###############################################################################
class SpeechMaker(object):
    def __init__(self):
        self._speech_maker = ev3.Sound

    def speak(self, phrase):
        """
        Speaks the given phrase aloud.
        The phrase must be short.

        Does NOT block, that is, continues immediately to the next statement
        while the sound is being played. Returns a subprocess.Popen,
        so if you want the sound-playing to block until the sound is completed
        (e.g. if the next statement will immediately make another sound),
        then use   speak  like this:
             speech_player = SpeechMaker()
             speech_player.speak().wait()

        IMPORTANT:  speak().wait()  does not appear to work correctly in all
        circumstances.  Put a   time.sleep()  after a   speak  as needed.

        :type  phrase:  str
        :rtype subprocess.Popen
        """
        return self._speech_maker.speak(phrase)


###############################################################################
# SongMaker
###############################################################################
class SongMaker(object):
    pass


###############################################################################
# -----------------------------------------------------------------------------
# LEDSystem classes:
# -----------------------------------------------------------------------------
###############################################################################

###############################################################################
# LED
###############################################################################
class LED(object):
    """
    Each LED has a RED and a GREEN component.
    """

    def __init__(self, left_or_right):  # Must be "left" or "right"
        self.which_led = left_or_right

        if self.which_led == "left":
            self.which_led_code = ev3.Leds.LEFT
        elif self.which_led == "right":
            self.which_led_code = ev3.Leds.RIGHT

        # Some common colors for an LED.  The two-tuple specifies the
        # brightness of the RED and GREEN components of the LED, respectively.
        self.BLACK = (0, 0)
        self.RED = (1, 0)
        self.GREEN = (0, 1)
        self.AMBER = (1, 1)
        self.ORANGE = (1, 0.5)
        self.YELLOW = (0.1, 1)

    def turn_on(self):
        """
        Sets this LED to 100% of its RED and GREEN, which results in AMBER.
        """
        self.set_color_by_name(self.AMBER)

    def turn_off(self):
        """ Turns this LED off. """
        self.set_color_by_name(self.BLACK)

    def set_color_by_name(self, color_name):
        """
        Sets this LED to the given color (as a name or tuple).  For example:
          left_led = LED("left")
          left_led.set_color_by_name(self.GREEN)
          left_led.set_color_by_name((0.5, 0.33))
        """
        ev3.Leds.set_color(self.which_led_code, color_name)

    def set_color_by_fractions(self, fraction_red, fraction_green):
        """
        Sets the brightness of this LED to the specified amount of
        RED and GREEN, respectively, where each argument is a number
        between 0 (none) and 1 (full brightness).

        Example:
          left_led = LED()
          left_led.set_color(0.5, 0.33)
        """
        self.set_color_by_name((fraction_red, fraction_green))


###############################################################################
# -----------------------------------------------------------------------------
# BeaconSystem classes
# -----------------------------------------------------------------------------
###############################################################################
class BeaconButton(object):
    pass


###############################################################################
# -----------------------------------------------------------------------------
# DisplaySystem classes
# -----------------------------------------------------------------------------
###############################################################################
class BrickButton(object):
    pass