axiom = "F+F+F+F"
rule = 'F+F-F-FF+F+F-F'
iterations=2
next_gen = ""

#print (next_gen)

def lsysgen(axiom,rule,iterations):
    next_gen = ''
    axiom=axiom
    rule=rule
    for i in range(iterations):
        next_gen=''
        for x in axiom:
            if x == "F":
                next_gen+=rule
            else:
                next_gen+=x
            axiom = next_gen
    if iterations ==0:
        next_gen=axiom 
    print(next_gen)
    return next_gen