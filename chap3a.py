import random
import sys
import os
import math

print(random.randint(1,10))

print(sys.path)
#pip install pyperclip (3rd party library)
import pyperclip

pyperclip.copy('Hello World!')
print(pyperclip.paste())


sys.exit() #terminates the program.
print("this wont be printed xD")