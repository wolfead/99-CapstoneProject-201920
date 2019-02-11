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


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
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

    # Go forward for seconds gui buttons
    for_seconds_label = ttk.Label(frame, text="Go Forward for Seconds")
    for_seconds_label.grid(row=6, column=0)
    for_seconds = ttk.Entry(frame, width=8)
    for_seconds.grid(row=7, column=0)

    for_seconds_speed_label = ttk.Label(frame, text="For Seconds Speed (0 to 100)")
    for_seconds_speed_label.grid(row=6, column=2)
    for_seconds_speed = ttk.Entry(frame, width=8)
    for_seconds_speed.grid(row=7, column=2)

    for_seconds_speed_button = ttk.Button(frame, text="Forward for Seconds")
    for_seconds_speed_button.grid(row=8, column=1)

    # Go forward for inches using time buttons
    using_time_label = ttk.Label(frame, text="Inches using Time")
    using_time_label.grid(row=9, column=0)
    using_time = ttk.Entry(frame, width=8)
    using_time.grid(row=10, column=0)

    using_time_speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    using_time_speed_label.grid(row=9, column=2)
    using_time_speed = ttk.Entry(frame, width=8)
    using_time_speed.grid(row=10, column=2)

    using_time_button = ttk.Button(frame, text="Forward Inches Using Time")
    using_time_button.grid(row=11, column=1)

    # Go straight for inches using encoder
    using_encoder_label = ttk.Label(frame, text="Inches using Encoder")
    using_encoder_label.grid(row=12, column=0)
    using_encoder = ttk.Entry(frame, width=8)
    using_encoder.grid(row=13, column=0)

    using_encoder_speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    using_encoder_speed_label.grid(row=12, column=2)
    using_encoder_speed = ttk.Entry(frame, width=8)
    using_encoder_speed.grid(row=13, column=2)

    using_encoder_button = ttk.Button(frame, text="Forward Inches Using Encoder")
    using_encoder_button.grid(row=14, column=1)

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
    print('turn left', '1', left_entry_box.get(), right_entry_box.get())
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


def handle_go_for_seconds(inches_entry_box, speed_entry_box, mqtt_sender):
    """
      :type  inches_entry_box:   ttk.Entry
      :type  speed_entry_box:  ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print('go forward for', inches_entry_box.get(), "at", speed_entry_box.get())
    mqtt_sender.send_message('go_forward_for_seconds', [inches_entry_box.get(), speed_entry_box.get()])


def handle_inches_using_time(inches_entry_box, speed_entry_box, mqtt_sender):
    """
      :type  inches_entry_box:   ttk.Entry
      :type  speed_entry_box:  ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print('go forward for', inches_entry_box.get(), "at", speed_entry_box.get())
    mqtt_sender.send_message('go_inches_using_time', [inches_entry_box.get(), speed_entry_box.get()])


def handle_inches_using_encoder(inches_entry_box, speed_entry_box, mqtt_sender):
    """
      :type  inches_entry_box:   ttk.Entry
      :type  speed_entry_box:  ttk.Entry
      :type  mqtt_sender:  com.MqttClient
    """
    print('go forward for', inches_entry_box.get(), "at", speed_entry_box.get())
    mqtt_sender.send_message('go_inches_using_encoder', [inches_entry_box.get(), speed_entry_box.get()])

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

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################


def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    # print('quit')
    # mqtt_sender.send_message('quit', [])


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
