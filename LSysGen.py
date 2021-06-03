axiom = "FX"
iterations=5
rules = {
    "X":">[-FX]+FX"
}
def lsysgen(axiom,rules,iterations):
    next_gen = ''
    axiom=axiom
    for i in range(iterations):
        next_gen=''
        for x in axiom:
            if x in rules:
                print(x,rules[x])
                next_gen+=rules[x]
            else:
                #print(x)
                next_gen+=x
            axiom = next_gen
    if iterations==0:
        next_gen=axiom 
    print(next_gen)
    return next_gen
lsysgen(axiom,rules,iterations)