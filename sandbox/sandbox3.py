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
minWidth = 0

canvas = Canvas(tk, width=Width, height=Height)
tk.title("Graphics")
canvas.pack()

ball = canvas.create_oval(0, 0, 100, 100, fill='red')
hat = canvas.create_text(250, 250, text="YOOOO HOMIE")
xspeed = 10
yspeed = 10

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball) #[left,top,right,bottom]
    n=4
    if pos[2] >= Width:
        print(pos[2])
        xspeed = -xspeed - n
        n = n +6
    if pos[0] <= 0:
        print(pos[0])
        xspeed = abs(xspeed)
        n = -2
    if pos[3] >= Height:
        print(pos[3])
        yspeed = -yspeed - n + 2
        n = 18
    if pos[1] <= 0:
        print(pos[1])
        yspeed = abs(yspeed)


    tk.update()
    time.sleep(0.1)
    # need these two for moving only one direction
