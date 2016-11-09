#!/usr/bin/env python3

try:
    from Tkinter import Tk
    from Tkinter import Label
    from Tkinter import Frame
except ImportError:
    from tkinter import Tk
    from tkinter import Label
    from tkinter import Frame

root = Tk()
root.wm_title("Magic Calculator")
root.geometry('{}x{}'.format(1000, 800))
baseFrame = Frame(root, height=400,width=400)

root.mainloop()
