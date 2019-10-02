from tkinter import *
import numpy as np
from PIL import Image, ImageTk


#import Usbhost # https://github.com/notiel/usbhost

window = Tk()

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

def draw_hue(w, h):
    array = np.zeros((h,w,3), dtype=np.uint8)
    for i in range(w):
        hue = i/w * 360
        r,g,b = to_rgb(hue, 100, 100)
        array[:,i,0] = r
        array[:,i,1] = g
        array[:,i,2] = b
    img =  ImageTk.PhotoImage(image=Image.fromarray(array, mode='RGB'))
    canvas = Canvas(window,width=w,height=h)
    canvas.create_image(0,0, image=img, anchor='nw')
    canvas.image = img
    return canvas

def my_canvas(w, h):
    array = np.zeros((h,w,3), dtype=np.uint8)
    canvas = Canvas(window,width=w,height=h)
    canvas.array = array
    return canvas

def update_s(canvas, h, v):
    array = canvas.array
    for i in range(w):
        s = i/w * 100
        r,g,b = to_rgb(h, s, v)
        array[:,i,0] = r
        array[:,i,1] = g
        array[:,i,2] = b
    img =  ImageTk.PhotoImage(image=Image.fromarray(array, mode='RGB'))
    canvas.create_image(0,0, image=img, anchor='nw')
    canvas.image = img
    return canvas

def update_v(canvas, h, s):
    array = canvas.array
    for i in range(w):
        v = i/w * 100
        r,g,b = to_rgb(h, s, v)
        array[:,i,0] = r
        array[:,i,1] = g
        array[:,i,2] = b
    img =  ImageTk.PhotoImage(image=Image.fromarray(array, mode='RGB'))
    canvas.create_image(0,0, image=img, anchor='nw')
    canvas.image = img
    return canvas

window.title("Colors")
canvas = draw_hue(100, 10)
canvas.pack()
#sl_H = Scale(window, variable = h)
   
window.mainloop()
