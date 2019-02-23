"""
this is a bot that I have made. All it does is spam a message in a message box.
You will, however, need to know the coordinates of where you want the bot to click.
Also, this program can be freely manipulated/edited. Makes something of it. 
Maybe even make it so that it can detetect message boxes and turn it into something cooler.
"""
# Requirements: Python, pip, PyUserInput
# You will need to install PyUserInput using pip
import time, sys
from pymouse import PyMouse
from pykeyboard import PyKeyboard

def spamclick():
    for spamtime in range(0,++times):
        MouseObject.click(x, y)
        time.sleep(FireOffTimer)
        KeyboardObject.type_string(myMessage)
        KeyboardObject.tap_key(KeyboardObject.enter_key)
        time.sleep(FireOffTimer)
        print(f"That was run {spamtime}.")

MouseObject = PyMouse()
KeyboardObject = PyKeyboard()

myMessage = input("""Your message\n> """)

x = int(input("Type X position\n> "))
y = int(input("Type Y position\n> "))
WARNING = input("!!!WARNING!!!\nIF YOU PUT ON A BIG NUMBER OF TIMES FOR THIS TO GO OFF YOU COULD POTENTIALLY BREAK SOMETHING!!!\nSTART OFF SMALL AND KNOW WHAT YOU ARE DOING!!!\nPRESS ENTER TO AGREE AND CONTINUE OR CTRL-C TO ABORT\n> ")

FireOffTimer = float(input("\nHow fast you want this to go(seconds)\n> "))
times = int(input("How many times you want this to repeat itself\n> "))

print("And were off!!!")
time.sleep(0.5)
MouseObject.click(x, y)
spamclick()
