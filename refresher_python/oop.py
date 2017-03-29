import random
import sys
import os as

#OBJECT ORIENTED PROGRAMMING, ATTRIBUTES. CLASSES

class Animal:
## __ means this is private --if we change values, use function inside class or if we need to use outside the class need to define function inside class
    __name = "" # or "" or None
    __height = 0
    __weight = 0
    __sound = 0

##SETTERS AND GETTERS
## CONTSTRUCTOR __ initializes OBJECT
    def __init__(self, name, height, weight, sound):
## THEN WE WANT TO CHANGE OR DEFINE
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound


## SELF allows object to refer itself, want to change itself
    def set_name(self, name):
        self.__name = name
    def set_height(self, height):
        self.__height = height
    def set_weight(self, weight):
        self.__weight = weight
    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name
    def get_height(self):
        return self.__height
    def get_weight(self):
        return self.__weight
    def get_sound(self):
        return self.__sound
