# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
import mqtt_remote_method_calls as com
import tkinter
from tkinter import *
import time
import random


#assign the module to a var
tk = Tk()

#set global vars
Height = 500
Width = 500

canvas = Canvas(tk, width=Width, height=Height)
tk.title("Graphics")
canvas.pack()

ball = canvas.create_oval(0, 0, 100, 100, fill='red')
hat = canvas.create_text(10, 50, text="hotdog")
xspeed = 5
yspeed = 5

while True:
    canvas.move(hat, xspeed, yspeed)

    tk.update()
    time.sleep(0.1)
