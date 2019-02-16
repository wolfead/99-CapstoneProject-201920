"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Alex Wolfe.
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

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project, Winter 2018-19, Robot 11")
    root2 = tkinter.Tk()
    root2.title("Sprint III for Alexander Wolfe")
    root2.geometry("500x500")
    canvas = tkinter.Canvas(root2,width='500',height='500',bg='cyan')
    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()
    canvas.grid()
    canvas.create_rectangle(200,200,300,300,fill='black')
    canvas.create_text(250,150,text='Forward',font='Arial')
    canvas.create_text(250, 350, text='Reverse', font='Arial')
    canvas.create_text(150, 250, text='Left', font='Arial')
    canvas.create_text(350, 250, text='Right', font='Arial')

    canvas.bind('<Button-1>', lambda event: left_mouse_click(event,mqtt_sender))

    canvas.bind('<B1-ButtonRelease>',
                lambda event: left_mouse_release(mqtt_sender))
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_system_frame, wolfe_frame = get_shared_frames(main_frame, mqtt_sender)
    # pick_up_m1_frame = ttk.Frame(root, padding=20, borderwidth=5,relief='groove')
    # m1frame_label = ttk.Label(pick_up_m1_frame, text="M1 Pick up Object")
    # m1frame_label.grid(row=0, column=2)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, wolfe_frame)
    # pick_up_m1_frame.grid(row=0,column=2)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    main_frame.mainloop()

def left_mouse_click(event, mqtt_sender):
    x = event.x
    y = event.y
    if x > 200 and x < 300 and y > 50 and y < 200:
        print('m1forward')
        mqtt_sender.send_message('forward', [100,100])
    elif x > 200 and x < 300 and y > 300 and y < 450:
        print('backward')
        mqtt_sender.send_message('backward', [100,100])
    elif x > 50 and x < 200 and y > 200 and y < 300:
        print('left')
        mqtt_sender.send_message('left', [75,75])
    elif x > 300 and x < 450 and y > 200 and y < 300:
        print('right')
        mqtt_sender.send_message('right', [75,75])

def left_mouse_release(mqtt_sender):
    print('stop')
    mqtt_sender.send_message('stop',[])

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    wolfe_frame = shared_gui.get_wolfe_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, drive_system_frame, wolfe_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, wolfe_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=1, column=1)
    drive_system_frame.grid(row=0, column=1)
    wolfe_frame.grid(row=0, column=2)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()