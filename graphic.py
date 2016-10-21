import sys
import turtle

def draw_square(brad):
   for i in range(4):
      brad.forward(100)
      brad.left(90)
 

window = turtle.Screen()
window.bgcolor("orange")
brad=turtle.Turtle()
brad.shape("turtle")
brad.speed(10)
brad.color("green")
for i in range(1,37):
   draw_square(brad)
   brad.left(10)

window.exitonclick()

#draw_square()   
