try:
    from Tkinter import *
except:
    from tkinter import *

from layout import layout

block = 5

class Keyboard(Frame):
    def __init__(self, parent, callback):
        Frame.__init__(self, parent, height=5*block, width=11*block)
        self.shift = False
        self.caps = True
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
        self.__call = callback
        Button.__init__(self, parent, text = t, command= lambda:self.__determineOutput__(parent))

        if "\n" in t:
            val = t.split("\n")
            self.__val1 = val[0]
            self.__val2 = val[1]
        else:
            self.__val1 = t
            self.__val2 = t

        __type = buttonType

    #check type, parent.shift and parent.caps for the output
    #set shift to false after using the shifted key
    def __determineOutput__(self, parent):
        #for letters
        if self.__type is "letter":
            if bool(parent.shift) ^ bool(parent.caps):
                self.__call(toStr(self.__val2))

        elif self.type is "shift":
            parent.shift = True
            self.__call("Shifted " + toStr(parent.Shift))

        elif self.type is "shift":
            parent.shift = True
            self.__call("Caps " + toStr(parent.Shift))

        elif self.type is "caps":
            parent.shift = True
            self.__call("Shifted " + toStr(parent.Shift))
