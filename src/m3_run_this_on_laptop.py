"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Haiden Smith.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project, Winter 2018-19, Robot 11")
    #
    # root1 = tkinter.Tk()
    # root1.title("Haiden's final Mario graphic")
    # root1.geometry("500x500")

    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    # canvas = tkinter.Canvas(root1, width='800', height='800', bg='tan')
    # canvas.grid()
    # mario = canvas.create_rectangle(225, 225, 300, 300, fill='red')

    teleop_frame, arm_frame, control_frame, drive_system_frame, haiden_frame, mario_frame = get_shared_frames(
        main_frame, mqtt_sender)

    grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, haiden_frame, mario_frame)

    main_frame.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    haiden_frame = shared_gui.get_haiden_frame(main_frame, mqtt_sender)
    mario_frame = shared_gui.get_mario_drive_system(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, drive_system_frame, haiden_frame, mario_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, haiden_frame, mario_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=1, column=1)
    drive_system_frame.grid(row=0, column=1)
    haiden_frame.grid(row=0, column=2)
    mario_frame.grid(row=1, column=2)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------


main()
