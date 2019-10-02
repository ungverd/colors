from tkinter import *
import numpy as np
from PIL import Image, ImageTk


import Usbhost # https://github.com/notiel/usbhost

window = Tk()

CANVAS_SIZE = (800, 10)
houses = ["Гриффиндор", "Слизерин", "Рейвенкло", "Хаффлпафф"]

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

def update_canvas(canvas, h, other, typ):
    array = canvas.array
    w = int(canvas.config()["width"][4])
    for i in range(w):
        var = i/w * 100
        if typ == "s":
            val = other
            sat = var
        elif typ == "v":
            sat = other
            val = var
        r,g,b = to_rgb(h, sat, val)
        array[:,i,0] = r
        array[:,i,1] = g
        array[:,i,2] = b
    img =  ImageTk.PhotoImage(image=Image.fromarray(array, mode='RGB'))
    canvas.create_image(0,0, image=img, anchor='nw')
    canvas.image = img
    return canvas

def update_h(i):
    def inner(val):
        #send command
        h[i] = float(val)
        update_canvas(canvases_s[i], h[i], v[i], "s")
        update_canvas(canvases_v[i], h[i], s[i], "v")
    return inner
def update_s(i):
    def inner(val):
        #send command
        s[i] = float(val)
        update_canvas(canvases_v[i], h[i], s[i], "v")
    return inner
def update_v(i):
    def inner(val):
        #send command
        v[i] = float(val)
        update_canvas(canvases_s[i], h[i], v[i], "s")
    return inner

window.title("Colors")
h = [0,130,240,60]
s = [100,100,100,100]
v = [50,50,50,50]
canvases_hue = [draw_hue(*CANVAS_SIZE) for i in range(4)]
canvases_s = [update_canvas(my_canvas(*CANVAS_SIZE), h[i], v[i], "s") for i in range(4)]
canvases_v = [update_canvas(my_canvas(*CANVAS_SIZE), h[i], s[i], "v") for i in range(4)]

scales_hue = [Scale(window, from_=0, to=360, orient=HORIZONTAL, resolution=0.1, length=CANVAS_SIZE[0], command = update_h(i)) for i in range(4)]
scales_s =   [Scale(window, from_=0, to=100, orient=HORIZONTAL, resolution=0.1, length=CANVAS_SIZE[0], command = update_s(i)) for i in range(4)]
scales_v =   [Scale(window, from_=0, to=100, orient=HORIZONTAL, resolution=0.1, length=CANVAS_SIZE[0], command = update_v(i)) for i in range(4)]



labels = [Label(window, text=houses[i]) for i in range(4)]

for i in range(4):

    labels[i].pack()
    scales_hue[i].set(h[i])
    scales_hue[i].pack()
    canvases_hue[i].pack()
    scales_s[i].set(s[i])
    scales_s[i].pack()
    canvases_s[i].pack()
    scales_v[i].set(v[i])
    scales_v[i].pack()
    canvases_v[i].pack()
    Label(window, text='').pack()

window.mainloop()
