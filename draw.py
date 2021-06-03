import turtle
from LSysGen import lsysgen
def create_turtle(screen_height,screen_width,speed,heading,x,y,size,iterations,line_length,angle,axiom,rules):
    turtle.screensize(screen_width,screen_height)
    oogway = turtle.Turtle()
    oogway.speed(speed)
    oogway.penup()
    oogway.setheading(heading)
    oogway.setx(x)
    oogway.sety(y)
    oogway.pendown()
    oogway.resizemode('auto')
    oogway.turtlesize(size)
    draw(oogway,iterations,line_length,angle,axiom,rules)
angle = 60
axiom = "YF"
rules = {
'X -> YF+XF+Y',
'Y -> XF-YF-X'
}
def draw(oogway,iterations,line_length,angle,axiom,rules):
    oogway.fillcolor('blue')
    drawStr = lsysgen(axiom,rules,iterations)
    stack = []
    for i in drawStr:
        if i == "F":
            oogway.pendown()
            oogway.forward(line_length)
        elif i == "f":
            oogway.penup()
            oogway.forward(line_length)
        elif i == "|":
            oogway.penup()
            oogway.left(180)
        elif i == "[":
            stack.append((oogway.heading(),oogway.position()))
        elif i == "]":
            oogway.penup()
            heading,position = stack.pop()
            oogway.goto(position)
            oogway.setheading(heading)
            oogway.pendown()
        elif i == "#":
            pass
        elif i == "{":
            oogway.begin_fill()
        elif i == "}":
            oogway.end_fill()
        elif i == "<":
            pass
        elif i == ">":
            line_length *= 1
        elif i == "&":
            pass
        elif i == "(":
            pass
        elif i == ")":
            pass
        elif i == "+":
            oogway.left(angle)
        elif i == "-":
            oogway.right(angle)
        else:
            pass
    turtle.done()