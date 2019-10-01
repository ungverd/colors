from tkinter import *
import numpy as np
from PIL import Image, ImageTk


import Usbhost # https://github.com/notiel/usbhost

def to_rgb(h, s, v):
    hi = (h // 60) % 6
    v_min = (100 - s) * v / 100
    a = (v - v_min) * (h % 60) / 60
    v_inc = v_min + a
    v_dec = v - a
    if hi == 0:
        r = v
        g = v_inc
        b = v_min
    elif hi == 1:
        r = v_dec
        g = v
        b = v_min
    elif hi == 2:
        r = v_min
        g = v
        b = v_inc
    elif hi == 3:
        r = v_min
        g = v_dec
        b = v
    elif hi == 4:
        r = v_inc
        g = v_min
        b = v
    elif hi == 5:
        r = v
        g = v_min
        b = v_dec
    r = round(r * 2.55)
    g = round(g * 2.55)
    b = round(b * 2.55)
    return r, g, b

def draw_hue(c, w, h):
    img =  ImageTk.PhotoImage(image=Image.fromarray(array))
    for i in range(w):
        hue = i/w * 360
        r,g,b = to_rgb(hue, 100, 100)
        rgb = "#" + hex(r*256*256 + g*256 + b)[2:]
        c.create_rectangle(50, 25, 150, 75, fill="blue")



window = Tk()
window.title("Colors")
sl_H = Scale(window, variable = h)
   
window.mainloop()
