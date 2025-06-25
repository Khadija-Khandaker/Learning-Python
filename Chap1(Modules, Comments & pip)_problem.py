
# 1) twinkle twinkle little star poem print
print('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')


# 2)Install an external module and use it to perform an operation of your interest

import pyttsx3
engine = pyttsx3.init()
engine.say("I'm very excited to learn python. What about you?")
engine.runAndWait()

# 4) write a python program to print the contents of a directory using the os model

import os

# Specify the directory path (you can change it as needed)
directory_path = "/learning python"

# Check if the path exists and is a directory
if os.path.isdir(directory_path):
    print(f"Contents of the directory '{directory_path}':")
    for item in os.listdir(directory_path):
        print(item)
else:
    print(f"The path '{directory_path}' is not a valid directory.")
