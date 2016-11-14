#!/usr/bin/env python3

try:
  from Tkinter import *
  root = Tk()
except:
  from tkinter import *
  root = Tk()

class CellArray:
    def __init__(self, row, col):
      self.__array = []
      self.__row = row
      self.__col = col

      for r in range(0, row):
          new = []
          self.__array.append(new)
          for y in range(0, col):
              self.__array[r].append(0)

    def Print(self):
        for r, row in enumerate(self.__array):
            for x, col in enumerate(row):
                print("[" + str(col) + "]", end="")

            print("")

    def step(self):
        cpy = self.__array

        rows = len(self.__array)
        columns = len(self.__array[0])

        for x in range(0, rows):
            for y in range(0, columns):
                n = self.neighbors(x,y)

                if self.__array[x][y] == 1:
                    if n != 2 and n != 3:
                        cpy[x][y] = 0

                elif self.__array[x][y] == 0:
                    if n == 3:
                        cpy[x][y] = 1
                else:
                    self.__array[x][y] = 0


        self.__array = cpy

    def neighbors(self, r, c):
        rows = len(self.__array)
        columns = len(self.__array[0])

        if r < 0 or r >= rows:
            return 0

        if c < 0 or c >= columns:
            return 0

        count = 0

        for x in range(r-1,r+2):
            for y in range(c-1, c+2):
                if not (r == x and c == y):
                    count += self.isAlive(x, y)

        return count


    def isAlive(self, r, c):
        rows = len(self.__array)
        columns = len(self.__array[0])

        if r < 0 or r >= rows:
            return 0

        if c < 0 or c >= columns:
            return 0

        return self.__array[r][c]


    def flip(self, r, c):
        val = 0

        if self.__array[r][c] is 0:
            val = 1

        self.__array[r][c] = val

class CellCanvas(Canvas):
    def __init__(self, array):
        self.__array = array

c = CellArray(20,20)
c.Print()
