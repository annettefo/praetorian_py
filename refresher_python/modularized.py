import random
import sys
import os
#OBJECT ORIENTED PROGRAMMING, ATTRIBUTES. CLASSES

class Animal:
    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound

    def __str__(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.name,self.height,self.weight,self.sound)

class Dog(Animal):
    def __init__(self, name, height, weight, sound, owner):
        super(Dog, self).__init__(name, height, weight, sound)
        self.owner = owner

    def __str__(self):
        return super(Dog, self).__str__() + ". His/her owner is {}".format(self.owner)

    def multiple_sounds(self, how_many=1):
        print self.sound * how_many

bella = Dog('Bella', 53, 27, "Ruff!", "Annette")
print bella
