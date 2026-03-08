import random as r
print(r.random())
print(r.randint(1,100))
print(r.randrange(0,100,10))


import sys as s
a=dir(s)
print(a)
print(s.path)
print("---------------------------------------")
print(s.version)
while True:
    print("1.Login\n2.Exit")
    c = int(input("Enter choice (1 / 2)"))
    if c==1:
        print("Logged in")
    elif c==2:
        print("Before exit")
        s.exit(0)
        print("After exit")

import socket
host=socket.gethostname()
print(host)

import pywhatkit
product = input("Enter search data :")
pywhatkit.search(product)

import webbrowser
webbrowser.open_new_tab("https://m.media-amazon.com/images/I/61RFlIUeaIL._SY575_.jpg")

import calendar as c
print(c.month(2023,8))
print(c.isleap(2023))
print(c.calendar(2026))

import time
print(time.ctime())
print("hi")
time.sleep(2)
print("bye")

l = ["Samsung","Lenovo","HP","Mac","Dell","Asus","Acer","VivoBook","Victus","Omen","MI"]
for i in l:
    time.sleep(2)
    print(i)

'''import sys as s
a=dir(s)
print(s.version)
print(s.path)


import socket
host=socket.gethostname()
print(host)'''
'''
import webbrowser
webbrowser.open_new_tab("https://www.w3schools.com/howto/default.asp")
import calendar as c
print(c.month(2023,8))
print(c.isleap(2023))
print(c.calendar(2025))

import time
print(time.ctime())
print("hii")
time.sleep(5)
print("hello")
for i in range(1,6,1):
    print(i)
    time.sleep(4)
import datetime as d
print(d.datetime.now())
import turtle
import time
star = turtle.Turtle()
star.right(75)
star.forward(100)
for i in range(4):
    time.sleep(2)
    star.right(144)
    star.forward(100)
turtle.done()
from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
import numpy as m
a=m.array([1,2,3,4,5])
print(type(a))
print(a)
print(m.min(a))
print(m.shape(a))
print(m.max(a))
print(m.sqrt(a))
print(m.mean(a))
print(m.median(a))

# Creating a 1D array
x = m.array([1, 2, 3])
# Creating a 2D array
y = m.array([[1, 2], [3, 4]])
# Creating a 3D array
z = m.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(x)
print(y)
print(z)

import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Addition
add = x + y  
print("Addition:",add)

# Subtraction
subtract = x - y 
print("substration:",subtract)

# Multiplication
multiply = x * y 
print("multiplication:",multiply)

# Division
divide = x / y  
print("division:", divide)'''
def image_display(value):
    import os
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
    import pygame
    icon = pygame.image.load(r"C:\Users\Live wire\Desktop\mounika\mounika python\icon.jpg")
    pygame.display.set_icon(icon)
    pygame.init()
    image = pygame.image.load(value)
    #screen = pygame.display.set_mode(image.get_size())
    screen = pygame.display.set_mode((400,400))
    screen.blit(image,(0,0))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
image_display(r"C:\Users\Live wire\Desktop\mounika\mounika python\img1.jpg")
  
