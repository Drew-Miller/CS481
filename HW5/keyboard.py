try:
    from Tkinter import *
except:
    from tkinter import *

from layout import layout

block = 5

class Keyboard(Frame):
    def __init__(self, parent, callback):
        Frame.__init__(self, parent, height=5*block, width=11*block)
        self.__shift = 0
        self.__caps = 0
        self.__initwidgets__(callback)

    def __initwidgets__(self, callback):
        for i,row in enumerate(layout):
            j = 0
            for column in row:
                b = KeyButton(self, column[0], callback, "letter")
                b.config(height=block, width=column[1]*block)
                b.grid(row=i, column=j, columnspan=column[1], sticky=N+E+W+S)
                j += column[1]

class KeyButton(Button):
    def __init__(self, parent, t, callback, buttonType):
        Button.__init__(self, parent, text = t, command= lambda:callback(t))

        __call = callback

        if "\n" in t:
            val = t.split("\n")
            __val1 = val[0]
            __val2 = val[1]
        else:
            __val1 = t
            __val2 = t

        __type = buttonType

    def __determineOutput__(self):
        __call(__val1)
