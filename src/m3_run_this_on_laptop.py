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
from tkinter import *
import shared_gui
import time


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
    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project, Winter 2018-19, Robot 11")
    root1 = tkinter.Tk()
    root1.title("Haiden's final Mario graphic")
    root1.geometry("500x500")
    canvas = tkinter.Canvas(root1, width='800', height='800', bg='tan')
    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
    canvas.grid()
    mario = canvas.create_rectangle(225, 225, 300, 300, fill='red')

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_system_frame, haiden_frame = get_shared_frames(
        main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, haiden_frame)
    # xspeed = 200
    # yspeed = 0
    #
    # while True:
    #     canvas.move(mario, xspeed, yspeed)
    #     pos = canvas.coords(mario)  # [left,top,right,bottom]
    #     if pos[2] >= 800:
    #         xspeed = -xspeed
    #     if pos[0] <= 0:
    #         break

    main_frame.mainloop()



def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    haiden_frame = shared_gui.get_haiden_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, drive_system_frame, haiden_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, haiden_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=1, column=1)
    drive_system_frame.grid(row=0, column=1)
    haiden_frame.grid(row=0, column=2)


def graphics(Height, Width, xspeed, yspeed):
    tk = Tk()
    canvas = Canvas(tk, width=Width, height=Height)
    ttk.Label("Graphics")
    canvas.pack()

    ball = canvas.create_oval(0, 0, 100, 100, fill='red')

    while True:
        canvas.move(ball, xspeed, yspeed)
        pos = canvas.coords(ball)  # [left,top,right,bottom]
        if pos[2] >= Width:
            print(pos[2])
            xspeed = -xspeed
        if pos[0] <= 0:
            print(pos[0])
            xspeed = abs(xspeed)

        tk.update()
        time.sleep(0.1)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
graphics(500, 500, 10, 0)
