from curses.ascii import islower
import string
from turtle import pos

with open("message.txt", "r") as file:
    content = file.read()
    
up_key = 'QWITJSYHXCNDFERMUKGOPVALBZ'
low_key = up_key.lower()

# print(up_key + low_key)

# ABCDEFGH
# QWITJSYHXCNDFERMUKGOPVALBZ

for character in content:
    if character.isupper():
        position = up_key.index(character)
        print(string.ascii_uppercase[position], end="")
    elif character.islower():
        position = low_key.index(character)
        print(string.ascii_lowercase[position], end="")
    else:
        print(character, end="")