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
        self.caps = False
        self.__initwidgets__(callback)

    def __initwidgets__(self, callback):
        for i,row in enumerate(layout):
            j = 0
            for column in row:
                b = KeyButton(self, column[0], callback)
                b.config(height=block, width=column[1]*block)
                b.grid(row=i, column=j, columnspan=column[1], sticky=N+E+W+S)
                j += column[1]

    def changeCase(self):
        #for child in self.winfo_children():
        print("changed")    


class KeyButton(Button):
    def __init__(self, parent, t, callback):
        self.__call = callback
        Button.__init__(self, parent, command= lambda:self.__determineOutput__(parent))
        self.__type = "special"

        if "\n" in t:
            val = t.split("\n")
            self.__val1 = val[0]
            self.__val2 = val[1]
            self.__type = "dual"

        else:
            self.__val1 = t
            self.__val2 = t

        if self.__val1.isalpha() and len(self.__val1) is 1:
            self.__type = "letter"

        if self.__val1 == "Shift":
            self.__type = "Shift"

        if self.__val1 == "CapsLock":
            self.__type = "Caps"

        self.config(text=self.__val1)

    #check type, parent.shift and parent.caps for the output
    #set shift to false after using the shifted key
    def __determineOutput__(self, parent):
        #for letters
        if self.__type is "letter":
            if bool(parent.shift) ^ bool(parent.caps):
                self.__call(str(self.__val2.upper()))
            else:
                self.__call(str(self.__val2.lower()))

            parent.shift = False

        elif self.__type is "dual":
            if parent.shift:
                self.__call(str(self.__val1))
            else:
                self.__call(str(self.__val2))

            parent.shift = False

        elif self.__type is "special":
            self.__call(str(self.__val1))


        elif self.__type is "Shift":
            parent.shift = not parent.shift
            parent.changeCase()

        elif self.__type is "Caps":
            parent.caps = not parent.caps
            parent.changeCase()
