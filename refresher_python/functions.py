from __future__ import print_function

import random
import sys
import os

def addNumber(fNum, lNum):
    sumNum = fNum + lNum #out of scope, stays there
    return sumNum

print(addNumber(1,4))
# string = addNumber(1, 4) #doesnt work

#PROGRAM TO RUN WHATS YOUR NAME
# print('What is your name')
# name = sys.stdin.readline()
# print('Hello', name)

long_string = "Ill catch you if you fall - The floor"
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + "be there")
print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))

# 3.x higher its capitalize
print(long_string.upper())
# .find returns -1 on failure, returns index in string
print(long_string.find("floor"))
# returns true or false if there is all characters in the string, no white space or special characters
print(long_string.isalpha())
# returns true or false if there is all numbers or not
print(long_string.isalnum())
