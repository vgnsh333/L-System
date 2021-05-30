base = "F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F"
rule = 'F+F-F-FF+F+F-F'
next_gen = ""
for i in base:
    if i == "F":
        next_gen+=rule
    else:
        next_gen+=i
