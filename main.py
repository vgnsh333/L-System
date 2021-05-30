from LSysGen import lsysgen
import turtle
skk = turtle.Turtle()

skk.speed(0)
skk.penup()
skk.setx(0)
skk.sety(0)
skk.pendown()
angle = 90

axiom = "F+F+F+F"
rule = 'FF+F++F+F'
iterations=2

drawStr = lsysgen(axiom,rule,iterations)
for i in drawStr:
    if i == "F":
        skk.forward(15)
    if i == "+":
        skk.left(angle)
    if i == "-":
        skk.right(angle)
     
turtle.done()