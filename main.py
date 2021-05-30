from LSysGen import next_gen
import turtle
skk = turtle.Turtle()
rule = next_gen
skk.speed(0)
skk.penup()
skk.setx(-100)
skk.sety(100)
skk.pendown()
for i in rule:
    if i == "F":
        skk.forward(10)
    if i == "+":
        skk.right(90)
    if i == "-":
        skk.left(90)
     
turtle.done()