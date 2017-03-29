import random
import sys
import os

# WRITE TO FILE WITH WB
test_file = open("test.txt","wb")

print(test_file.mode)
print(test_file.name)
test_file.write(bytes("It's almost Easter\n?"))
test_file.close()

test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)

os.remove("test.txt")
