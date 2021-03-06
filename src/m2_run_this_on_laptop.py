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
    pc_delegate = Laptop_Reciever()
    mqtt_sender = com.MqttClient(pc_delegate)
    mqtt_sender.connect_to_ev3()
    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project, Winter 2018-19, Robot 11")
    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    cup_remover_frame = get_shared_frames(
        main_frame, mqtt_sender)
    # teleop_frame, arm_frame, control_frame, drive_system_frame, tubuyo_frame,
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(cup_remover_frame)
    # teleop_frame, arm_frame, control_frame, drive_system_frame, tubuyo_frame,



    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    main_frame.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    # teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    # arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    # control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    # drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    # tubuyo_frame = shared_gui.get_tubuyo_frame(main_frame, mqtt_sender)
    # teleop_frame, arm_frame, control_frame, drive_system_frame, tubuyo_frame,
    cup_remover_frame = shared_gui.get_cup_remover(main_frame, mqtt_sender)
    return cup_remover_frame


def grid_frames(cup_remover_frame):
    # teleop_frame, arm_frame, control_frame, drive_system_frame, tubuyo_frame,
    # teleop_frame.grid(row=0, column=0)
    # arm_frame.grid(row=1, column=0)
    # control_frame.grid(row=1, column=1)
    # drive_system_frame.grid(row=0, column=1)
    # tubuyo_frame.grid(row=0, column=2)
    cup_remover_frame.grid(row=1, column=2)


class Laptop_Reciever(object):
    def print_cup_count(self, n):
        print('I have removed:', n, 'cups!')



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()