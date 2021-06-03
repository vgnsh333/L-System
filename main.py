from LSysGen import lsysgen
import turtle
skk = turtle.Turtle()

skk.speed(0)
skk.penup()
skk.setx(0)
skk.sety(0)
skk.pendown()
angle = 90

# Hardcoded values for now
axiom = "F+F+F+F"
rule = 'FF+F++F+F'
iterations = 2
line_length = 5
drawStr = lsysgen(axiom,rule,iterations)
stack = []
for i in drawStr:
    if i == "F":
        skk.forward(line_length)
    elif i == "f":
        skk.penup()
        skk.forward(line_length)
    elif i == "|":
        pass
    elif i == "[":
        pass
    elif i == "]":
        pass
    elif i == "#":
        pass
    elif i == "{":
        pass
    elif i == "}":
        pass
    elif i == "<":
        pass
    elif i == ">":
        pass
    elif i == "&":
        pass
    elif i == "(":
        pass
    elif i == ")":
        pass
    elif i == "+":
        skk.left(angle)
    elif i == "-":
        skk.right(angle)
    else:
        print(i,': Not recognized')
turtle.done()