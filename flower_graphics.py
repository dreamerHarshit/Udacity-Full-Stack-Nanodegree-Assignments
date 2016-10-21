import sys
import turtle

def draw_rhombus(brad):
   for i in range(1,3):
      brad.forward(100)
      brad.left(45)
      brad.forward(100)
      brad.left(135)

window = turtle.Screen()
window.bgcolor("orange")
brad=turtle.Turtle()
brad.shape("turtle")
brad.speed(100)
brad.color("green")
for i in range(1,37):
   draw_rhombus(brad)
   brad.left(10)
brad.right(90)   
brad.forward(500)   
window.exitonclick()

#draw_square()   
