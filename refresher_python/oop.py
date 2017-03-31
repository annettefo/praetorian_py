import random
import sys
import os
#OBJECT ORIENTED PROGRAMMING, ATTRIBUTES. CLASSES

class Animal:
## __ means this is private --if we change values, use function inside class or if we need to use outside the class need to define function inside class
##SETTERS AND GETTERS
## CONTSTRUCTOR __ initializes OBJECT and makes it private
    def __init__(self, name, height, weight, sound):
## THEN WE WANT TO CHANGE OR DEFINE
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound
## SELF allows object to refer itself, want to change itself
    def set_name(self, name):
        self.name = name
    def set_height(self, height):
        self.height = height
    def set_weight(self, weight):
        self.weight = weight
    def set_sound(self, sound):
        self.sound = sound

    def get_name(self):
        return self.name
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_sound(self):
        return self.sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} killograms and say {}".format(self.name,self.height,self.weight,self.sound)

#CREATE OBJECT
dog = Animal("Bella", 33, 10, "Bark")
print dog.toString()

## INHERITANCE FROM OTHER CLASS ANIMAL
class Dog(Animal):
## overwrite constructor more specific
    def __init__(self, name, height, weight, sound, owner):
## if i want to use constructor above
        super(Dog, Animal).__init__(name, height, weight, sound)
        self.__owner = owner

    def set_owner(self, owner):
        self.__owner = owner
    def get_owner(self):
        return self.__owner
    def get_type(self):
        print("Bella is the baby")
    def toString(self):
        return "{} is {} cm tall and {} killograms and say {}, I love my mom".format(self.get_name,self.get_height,self.get_weight,self.get_sound, self.__owner)

## METHOD OVERLOADING -
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)
