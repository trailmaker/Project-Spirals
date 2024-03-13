#Project in Python Spiraling n sided polygons
#Roxana Chowdhury 3/12/2024

import turtle
turtle.color("red")

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

#foward helper function
def move(len):
  back(-1 * len)

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360/num)
    
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
 
   
spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)
move(150)
turtle.color("green")
spiral(85, 72)
  
    
#polygon(3, 100)
#back(125)
#polygon(4,100)

#draws the 7 different shapes in a clock face
#for n in range (3, 10):
 #  move(50)
 # polygon(n, 100/n)
 # back(50)
 # turtle.right(360 / 7)
