#Draws polygons with different number of sides in a circle

import turtle

turtle.color("red")
size = 100
#n = 13

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

  
def mov(len):
  back(-1*len)

def polygon(m, size1):
  for i in range(m):
    turtle.forward(size1)
    turtle.left(360/m)



#circle of polygons

for n in range (3,10):
  mov(50)
  polygon(n, size/n)
  back(50)
  turtle.right(360/7)
   
