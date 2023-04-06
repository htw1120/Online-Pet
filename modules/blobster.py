

import math
import time


class Pet:
    def __init__(self, name, color, radius, height):
        self.__radius = radius
        self.__height = height
        self.__color = color
        self.__name = name
        self.__time = time.time()
        self.__volume = (math.pi * pow(radius, 2) * self.__height)

    def feedBlobster(self, food):
        if food >= 0:
            self.__radius += food

    def blobsterSpeak(self):
        vitals, blobster_ok = self.vitalsOK()
        return ("My name is " + self.__name.capitalize() + ", and I am " + self.__color.lower()) + "\n" + \
               "My current happiness level is " + str(format(vitals, ".2%"))

    def vitalsOK(self):
        while True:
            volume1 = math.pi * pow(self.__radius - ((time.time() - self.__time) * .0002), 2) * self.__height
            vitals = volume1 / self.__volume
            if .9 < vitals < 1.1:
                return vitals, True
            else:
                return vitals, False

    def setColor(self, color):
        if type(color) == str:
            self.__color = color

    def setName(self, name):
        if type(name) == str:
            self.__name = name

    def getColor(self):
        return self.__color

    def getName(self):
        return self.__name
    