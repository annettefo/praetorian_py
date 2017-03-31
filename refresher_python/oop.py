import random
import sys
import os
#OBJECT ORIENTED PROGRAMMING, ATTRIBUTES. CLASSES

class Animal:
## __ means this is private --if we change values, use function inside class or if we need to use outside the class need to define function inside class
##SETTERS AND GETTERS
## CONTSTRUCTOR __ initializes OBJECT
    def __init__(self, name, height, weight, sound):
## THEN WE WANT TO CHANGE OR DEFINE
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
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

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} killograms and say {}".format(self.__name,self.__height,self.__weight,self.__sound)

#CREATE OBJECT
dog = Animal("Bella", 33, 10, "Bark")
print dog.toString()

## INHERITANCE
class Dog(Animal):
    __owner = ""
## overwrite constructor more specific
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
## if i want to use constructor above
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Bella is the baby")

    def toString(self):
        return "{} is {} cm tall and {} killograms and say {}, I love my mom".format(self.__name,self.__height,self.__weight,self.__sound, self.__owner)
