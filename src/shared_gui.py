"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Alexander Wolfe, Haiden Smith, Alexander Tabuyo.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk

import time


def get_drive_system_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Drive System")
    frame_label.grid(row=0, column=2)

    # display_camera_data_button = ttk.Button(frame, text='Display Camera data on GUI')
    # display_camera_data_button.grid(row=25, column=1)

    intensity_box_1_label = ttk.Label(frame, text="Intensity")
    intensity_box_1_label.grid(row=1, column=0)
    speed_box_3_label = ttk.Label(frame, text="Speed")
    speed_box_3_label.grid(row=1, column=1)

    intensity_box_1 = ttk.Entry(frame, width=8)
    intensity_box_1.grid(row=2, column=0)
    speed_box_3 = ttk.Entry(frame, width=8)
    speed_box_3.grid(row=2, column=1)

    go_straight_until_intensity_is_less_than_button = ttk.Button(frame, text="Straight until intensity is less than")
    go_straight_until_intensity_is_less_than_button.grid(row=2, column=2)

    intensity_box_2_label = ttk.Label(frame, text='Intensity')
    intensity_box_2_label.grid(row=3, column=0)
    speed_box_5_label = ttk.Label(frame, text='Speed')
    speed_box_5_label.grid(row=3, column=1)

    intensity_box_2 = ttk.Entry(frame, width=8)
    intensity_box_2.grid(row=4, column=0)
    speed_entry_box_5 = ttk.Entry(frame, width=8)
    speed_entry_box_5.grid(row=4, column=1)

    handle_go_straight_until_intensity_is_greater_than_button = ttk.Button(frame, text="Straight until intensity "
                                                                                       "is greater than")
    handle_go_straight_until_intensity_is_greater_than_button.grid(row=4, column=2)

    color_box_1_label = ttk.Label(frame, text="Color")
    color_box_1_label.grid(row=5, column=0)
    speed_entry_box_6_label = ttk.Label(frame, text="Speed")
    speed_entry_box_6_label.grid(row=5, column=1)

    color_box_1 = ttk.Entry(frame, width=8)
    color_box_1.grid(row=6, column=0)
    speed_entry_box_6 = ttk.Entry(frame, width=8)
    speed_entry_box_6.grid(row=6, column=1)

    handle_go_straight_until_color_is_button = ttk.Button(frame, text="Straight until color is")
    handle_go_straight_until_color_is_button.grid(row=6, column=2)

    color_box_2_label = ttk.Label(frame, text="Color")
    color_box_2_label.grid(row=7, column=0)
    speed_entry_box_7_label = ttk.Label(frame, text='Speed')
    speed_entry_box_7_label.grid(row=7, column=1)

    color_box_2 = ttk.Entry(frame, width=8)
    color_box_2.grid(row=8, column=0)
    speed_entry_box_7 = ttk.Entry(frame, width=8)
    speed_entry_box_7.grid(row=8, column=1)

    handle_go_straight_until_color_is_not_button = ttk.Button(frame, text="Straight until color is not")
    handle_go_straight_until_color_is_not_button.grid(row=8, column=2)

    inches_entry_box_4_label = ttk.Label(frame, text='Inches')
    inches_entry_box_4_label.grid(row=9, column=0)
    speed_entry_box_4_label = ttk.Label(frame, text='Speed')
    speed_entry_box_4_label.grid(row=9, column=1)

    inches_entry_box_4 = ttk.Entry(frame, width=8)
    inches_entry_box_4.grid(row=10, column=0)
    speed_entry_box_4 = ttk.Entry(frame, width=8)
    speed_entry_box_4.grid(row=10, column=1)

    pick_up_frame = ttk.Frame()

    handle_go_forward_until_distance_is_less_than_button = ttk.Button(frame, text='Straight until '
                                                                                  'distance is less than')
    handle_go_forward_until_distance_is_less_than_button.grid(row=10, column=2)

    inches_entry_box_3_label = ttk.Label(frame, text="Inches")
    inches_entry_box_3_label.grid(row=11, column=0)
    inches_entry_box_3 = ttk.Entry(frame, width=8)
    inches_entry_box_3.grid(row=12, column=0)
    speed_entry_box_8_label = ttk.Label(frame, text='Speed')
    speed_entry_box_8_label.grid(row=11, column=1)
    speed_entry_box_8 = ttk.Entry(frame, width=8)
    speed_entry_box_8.grid(row=12, column=1)
    handle_go_backward_until_distance_is_greater_than_button = ttk.Button(frame, text="Backward until distance"
                                                                                      " is greater than")
    handle_go_backward_until_distance_is_greater_than_button.grid(row=12, column=2)

    delta_entry_box_1_label = ttk.Label(frame, text='Delta')
    delta_entry_box_1_label.grid(row=13, column=0)
    delta_entry_box_1 = ttk.Entry(frame, width=8)
    delta_entry_box_1.grid(row=14, column=0)
    inches_entry_box_5_label = ttk.Label(frame, text="Inches")
    inches_entry_box_5_label.grid(row=13, column=1)
    inches_entry_box_5 = ttk.Entry(frame, width=8)
    inches_entry_box_5.grid(row=14, column=1)
    speed_entry_box_9_label = ttk.Label(frame, text="Speed")
    speed_entry_box_9_label.grid(row=13, column=3)
    speed_entry_box_9 = ttk.Entry(frame, width=8)
    speed_entry_box_9.grid(row=14, column=3)

    handle_go_until_distance_is_within_button = ttk.Button(frame, text="Straight until distance is within")
    handle_go_until_distance_is_within_button.grid(row=14, column=2)

    speed_entry_box_13_label = ttk.Label(frame, text="Speed")
    speed_entry_box_13_label.grid(row=15, column=1)
    area_entry_box_1_label = ttk.Label(frame, text="Area")
    area_entry_box_1_label.grid(row=15, column=0)
    speed_entry_box_13 = ttk.Entry(frame, width=8)
    speed_entry_box_13.grid(row=16, column=1)
    area_entry_box_1 = ttk.Entry(frame, width=8)
    area_entry_box_1.grid(row=16, column=0)
    handle_spin_clockwise_until_sees_object_button = ttk.Button(frame, text="Spin clockwise until object")
    handle_spin_clockwise_until_sees_object_button.grid(row=16, column=2)

    speed_entry_box_14_label = ttk.Label(frame, text="Speed")
    speed_entry_box_14_label.grid(row=17, column=1)
    speed_entry_box_14 = ttk.Entry(frame, width=8)
    speed_entry_box_14.grid(row=18, column=1)
    area_entry_box_2_label = ttk.Label(frame, text="Area")
    area_entry_box_2_label.grid(row=17, column=0)
    area_entry_box_2 = ttk.Entry(frame, width=8)
    area_entry_box_2.grid(row=18, column=0)

    handle_spin_counterclockwise_until_sees_object_button = ttk.Button(frame, text="Spin counter "
                                                                                   "clockwise until object")
    handle_spin_counterclockwise_until_sees_object_button.grid(row=18, column=2)

    # Call back to buttons ################################################################
    # display_camera_data_button["command"] = lambda: handle_display_camera_data(mqtt_sender)
    go_straight_until_intensity_is_less_than_button["command"] = lambda:\
        handle_go_straight_until_intensity_is_less_than(intensity_box_1, speed_box_3, mqtt_sender)
    handle_go_straight_until_intensity_is_greater_than_button["command"] = lambda: \
        handle_go_straight_until_intensity_is_greater_than(intensity_box_2, speed_entry_box_5, mqtt_sender)
    handle_go_straight_until_color_is_button["command"] = lambda: handle_go_straight_until_color_is(
        color_box_1, speed_entry_box_6, mqtt_sender)
    handle_go_straight_until_color_is_not_button["command"] = lambda: handle_go_straight_until_color_is_not(
        color_box_2, speed_entry_box_7, mqtt_sender)
    handle_go_forward_until_distance_is_less_than_button["command"] = lambda: \
        handle_go_forward_until_distance_is_less_than(inches_entry_box_4, speed_entry_box_4, mqtt_sender)
    handle_go_backward_until_distance_is_greater_than_button["command"] = lambda: \
        handle_go_backward_until_distance_is_greater_than(inches_entry_box_3, speed_entry_box_8, mqtt_sender)
    handle_go_until_distance_is_within_button["command"] = lambda: handle_go_until_distance_is_within(
        delta_entry_box_1, inches_entry_box_5, speed_entry_box_9, mqtt_sender)
    handle_spin_clockwise_until_sees_object_button["command"] = lambda: handle_spin_clockwise_until_sees_object(
        speed_entry_box_13, area_entry_box_1, mqtt_sender)
    handle_spin_counterclockwise_until_sees_object_button["command"] = lambda: \
        handle_spin_counterclockwise_until_sees_object(speed_entry_box_14, area_entry_box_2, mqtt_sender)

    return frame


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Go forward for seconds gui buttons
    for_seconds_label = ttk.Label(frame, text="Go Forward for Seconds")
    for_seconds_label.grid(row=6, column=0)
    seconds_entry_box = ttk.Entry(frame, width=8)
    seconds_entry_box.grid(row=7, column=0)

    for_seconds_speed_label = ttk.Label(frame, text="For Seconds Speed (0 to 100)")
    for_seconds_speed_label.grid(row=6, column=2)
    speed_entry_box = ttk.Entry(frame, width=8)
    speed_entry_box.grid(row=7, column=2)

    for_seconds_speed_button = ttk.Button(frame, text="Forward for Seconds")
    for_seconds_speed_button.grid(row=8, column=1)

    # Go forward for inches using time buttons
    using_time_label = ttk.Label(frame, text="Inches using Time")
    using_time_label.grid(row=9, column=0)
    inches_entry_box_1 = ttk.Entry(frame, width=8)
    inches_entry_box_1.grid(row=10, column=0)

    using_time_speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    using_time_speed_label.grid(row=9, column=2)
    speed_entry_box_1 = ttk.Entry(frame, width=8)
    speed_entry_box_1.grid(row=10, column=2)

    using_time_button = ttk.Button(frame, text="Forward Inches Using Time")
    using_time_button.grid(row=11, column=1)

    # Go straight for inches using encoder
    using_encoder_label = ttk.Label(frame, text="Inches using Encoder")
    using_encoder_label.grid(row=12, column=0)
    inches_entry_box_2 = ttk.Entry(frame, width=8)
    inches_entry_box_2.grid(row=13, column=0)

    using_encoder_speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    using_encoder_speed_label.grid(row=12, column=2)
    speed_entry_box_2 = ttk.Entry(frame, width=8)
    speed_entry_box_2.grid(row=13, column=2)

    using_encoder_button = ttk.Button(frame, text="Forward Inches Using Encoder")
    using_encoder_button.grid(row=14, column=1)

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # BEEP BUTTONS
    beep_label = ttk.Label(frame, text="Number of times to beep")
    beep_label.grid(row=15, column=0)
    number = ttk.Entry(frame, width=12)
    number.grid(row=16, column=0)

    beeper_button = ttk.Button(frame, text="Beep number of times")
    beeper_button.grid(row=16, column=2)

    # TONE BUTTONS
    tone_frequency_label = ttk.Label(frame, text="Tone frequency")
    tone_frequency_label.grid(row=17, column=0)
    frequency = ttk.Entry(frame, width=8)
    frequency.grid(row=18, column=0)
    tone_duration_label = ttk.Label(frame, text="Tone duration")
    tone_duration_label.grid(row=17, column=1)
    duration = ttk.Entry(frame, width=8)
    duration.grid(row=18, column=1)
    tone_button = ttk.Button(frame, text="Tone")
    tone_button.grid(row=18, column=2)

    # SPEECH BUTTONS
    speech_label = ttk.Label(frame, text="Speech Text")
    speech_label.grid(row=19, column=0)
    s = ttk.Entry(frame, width=12)
    s.grid(row=20, column=0)
    speech_button = ttk.Button(frame, text="Speak Speech")
    speech_button.grid(row=20, column=2)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)
    for_seconds_speed_button["command"] = lambda: handle_go_for_seconds(
        seconds_entry_box, speed_entry_box, mqtt_sender)
    using_time_button["command"] = lambda: handle_inches_using_time(
        inches_entry_box_1, speed_entry_box_1, mqtt_sender)
    using_encoder_button["command"] = lambda: handle_inches_using_encoder(
        inches_entry_box_2, speed_entry_box_2, mqtt_sender)
    beeper_button["command"] = lambda: handle_beeper(number, mqtt_sender)
    tone_button["command"] = lambda: handle_tone(frequency, duration, mqtt_sender)
    speech_button["command"] = lambda: handle_speech(s, mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame

def get_pick_up_frame(window,mqtt_sender):
    frame = ttk.Frame(window,padding = 10,borderwidth = 5)
    frame.grid()
    frame_label = ttk.Label(frame,text='Pick up object')
    frame_label.grid()
    speed_entry = ttk.Entry(frame)
    speed_entry.grid()
    pick_up_button = ttk.Button(frame, text='Pick Up object')
    pick_up_button.grid()
    pick_up_button['command'] = lambda: handle_pick_up_object(speed_entry,mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################


def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('forward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('forward', [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('backward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('backward', [left_entry_box.get(), right_entry_box.get()])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('turn left', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('left', [left_entry_box.get(), right_entry_box.get()])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('turn right', left_entry_box.get(), '-', right_entry_box.get())
    mqtt_sender.send_message('right', [left_entry_box.get(), right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('stop')
    mqtt_sender.send_message('stop', [])


def handle_go_for_seconds(seconds_entry_box, speed_entry_box, mqtt_sender):
    """
      :type  seconds_entry_box:   ttk.Entry
      :type  speed_entry_box:  ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print('go forward for', seconds_entry_box.get(), " seconds at", speed_entry_box.get())
    mqtt_sender.send_message('go_forward_for_seconds', [seconds_entry_box.get(), speed_entry_box.get()])


def handle_inches_using_time(inches_entry_box_1, speed_entry_box_1, mqtt_sender):
    """
      :type  inches_entry_box_1:   ttk.Entry
      :type  speed_entry_box_1:  ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print('go forward for', inches_entry_box_1.get(), "inches at", speed_entry_box_1.get())
    mqtt_sender.send_message('go_inches_using_time', [inches_entry_box_1.get(), speed_entry_box_1.get()])


def handle_inches_using_encoder(inches_entry_box_2, speed_entry_box_2, mqtt_sender):
    """
      :type  inches_entry_box_2:   ttk.Entry
      :type  speed_entry_box_2:  ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print('go forward for', inches_entry_box_2.get(), "inches at", speed_entry_box_2.get())
    mqtt_sender.send_message('go_inches_using_encoder', [inches_entry_box_2.get(), speed_entry_box_2.get()])


def handle_beeper(number, mqtt_sender):
    """
      :type  number:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print('I will beep', number.get(), 'times')
    mqtt_sender.send_message('beep_n', [number.get()])


def handle_tone(frequency, duration, mqtt_sender):
    """
      :type  frequency:   ttk.Entry
      :type  duration:  ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print('I will play a tone at frequency', frequency.get(), 'for the duration', duration.get())
    mqtt_sender.send_message('tone', [frequency.get(), duration.get()])


def handle_speech(s, mqtt_sender):
    """
      :type  s:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will speak phrase", s.get())
    mqtt_sender.send_message('speech', [s.get()])


##############################################################################
# More drive system functions put into another frame
##############################################################################


def handle_go_straight_until_intensity_is_less_than(intensity_box_1, speed_box_3, mqtt_sender):
    """
      :type  intensity_box_1:   ttk.Entry
      :type  speed_box_3:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will go straight at speed ", speed_box_3.get(), "until intensity is less than ", intensity_box_1.get())
    mqtt_sender.send_message('go_straight_until_intensity_is_less_than', [intensity_box_1.get(), speed_box_3.get()])


def handle_go_straight_until_intensity_is_greater_than(intensity_box_2, speed_entry_box_5, mqtt_sender):
    """
      :type  intensity_box_2:   ttk.Entry
      :type  speed_entry_box_5:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will go straight at speed ", speed_entry_box_5.get(), "until intensity is greater than ",
          intensity_box_2.get())
    mqtt_sender.send_message('go_straight_until_intensity_is_greater_than',
                             [intensity_box_2.get(), speed_entry_box_5.get()])


def handle_go_straight_until_color_is(color_box_1, speed_entry_box_6, mqtt_sender):
    """
      :type  color_box_1:   ttk.Entry
      :type  speed_entry_box_6:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will go straight at speed ", speed_entry_box_6.get(), "until the color is ", color_box_1.get())
    mqtt_sender.send_message('go_straight_until_color_is', [color_box_1.get(), speed_entry_box_6.get()])


def handle_go_straight_until_color_is_not(color_box_2, speed_entry_box_7, mqtt_sender):
    """
      :type  color_box_2:   ttk.Entry
      :type  speed_entry_box_7:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will go straight until the color is not ", color_box_2.get(), "at speed ", speed_entry_box_7.get())
    mqtt_sender.send_message('go_straight_until_color_is_not', [color_box_2.get(), speed_entry_box_7.get()])


def handle_go_forward_until_distance_is_less_than(inches_entry_box_4, speed_entry_box_4, mqtt_sender):
    """
      :type  inches_entry_box_4:   ttk.Entry
      :type  speed_entry_box_4:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will go straight at speed ", speed_entry_box_4.get(), "until distance is less than "
                                                                   "", inches_entry_box_4.get())
    mqtt_sender.send_message('go_forward_until_distance_is_less_than', [inches_entry_box_4.get(),
                                                                        speed_entry_box_4.get()])


def handle_go_backward_until_distance_is_greater_than(inches_entry_box_3, speed_entry_box_8, mqtt_sender):
    """
      :type  inches_entry_box_3:   ttk.Entry
      :type  speed_entry_box_8:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will go backward at speed ", speed_entry_box_8.get(), "until the distance is greater than",
          inches_entry_box_3.get())
    mqtt_sender.send_message('go_backward_until_distance_is_greater_than', [inches_entry_box_3.get(),
                                                                            speed_entry_box_8.get()])


def handle_go_until_distance_is_within(delta_entry_box_1, inches_entry_box_5, speed_entry_box_9, mqtt_sender):
    """
      :type  delta_entry_box_1:    ttk.Entry
      :type  inches_entry_box_5:   ttk.Entry
      :type  speed_entry_box_9:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will go forward until the distance is within", inches_entry_box_5.get(), "at speed ",
          speed_entry_box_9.get())
    mqtt_sender.send_message('go_until_distance_is_within', [delta_entry_box_1.get(), inches_entry_box_5.get(),
                                                             speed_entry_box_9.get()])


# def handle_spin_clockwise_until_beacon_heading_is_nonnegative(speed_entry_box_10, mqtt_sender):
#     """
#       :type  speed_entry_box_10:   ttk.Entry
#       :type  mqtt_sender:  com.MqttClient
#     """
#     print("I will spin clockwise until the beacon heading is nonnegative at speed", speed_entry_box_10.get())
#     mqtt_sender.send_message('spin_clockwise_until_beacon_heading_is_nonnegative', [speed_entry_box_10.get()])
#
#
# def handle_spin_counterclockwise_until_beacon_heading_is_nonpositive(speed_entry_box_11, mqtt_sender):
#     """
#       :type  speed_entry_box_11:   ttk.Entry
#       :type  mqtt_sender:  com.MqttClient
#     """
#     print("I will spin counterclockwise until the beacon heading is nonpositive at speed", speed_entry_box_11.get())
#     mqtt_sender.send_message('spin_counterclockwise_until_beacon_heading_is_nonpositive', [speed_entry_box_11.get()])
#
#
# def handle_go_straight_to_the_beacon(inches_entry_box_6, speed_entry_box_12, mqtt_sender):
#     """
#       :type  inches_entry_box_6:   ttk.Entry
#       :type  speed_entry_box_12:   ttk.Entry
#       :type  mqtt_sender:  com.MqttClient
#     """
#     print("I will go straight until the beacon reads less than", inches_entry_box_6.get(), 'at speed',
#           speed_entry_box_12.get())
#     mqtt_sender.send_message('go_straight_to_the_beacon', [inches_entry_box_6.get(), speed_entry_box_12.get()])


def handle_display_camera_data(mqtt_sender):
    """
      :type  mqtt_sender:  com.MqttClient
    """
    print("Display camera data on the gui")
    mqtt_sender.send_message('display_camera_data')


def handle_spin_clockwise_until_sees_object(speed_entry_box_13, area_entry_box_1, mqtt_sender):
    """
      :type  area_entry_box_1:   ttk.Entry
      :type  speed_entry_box_13:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will spin clockwise until the camera sees the object at speed", speed_entry_box_13.get())
    mqtt_sender.send_message('spin_clockwise_until_sees_object', [speed_entry_box_13.get(), area_entry_box_1.get()])


def handle_spin_counterclockwise_until_sees_object(speed_entry_box_14, area_entry_box_2, mqtt_sender):
    """
      :type  area_entry_box_2:   ttk.Entry
      :type  speed_entry_box_14:   ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print("I will spin counterclockwise until I see an object at speed ", speed_entry_box_14.get())
    mqtt_sender.send_message('spin_counterclockwise_until_sees_object', [speed_entry_box_14.get(),
                                                                         area_entry_box_2.get()])

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################


def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('raising arm')
    mqtt_sender.send_message('raise_arm', [])


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("lowering arm")
    mqtt_sender.send_message('lower_arm', [])


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("calibrate arm")
    mqtt_sender.send_message('calibrate_arm')


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("move arm to position")
    mqtt_sender.send_message('move_arm_to', [arm_position_entry.get()])


def handle_pick_up_object(speed_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  speed_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    mqtt_sender.send_message('pick_up_object',[speed_entry.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################


def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print("exit")
    handle_quit(mqtt_sender)
    exit()
