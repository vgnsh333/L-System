
def rules_formatter(rules_unformatted):
    rules = {}
    for i in rules_unformatted:
        x = i.replace(' ','').split('->')
        rules[x[0]]=x[1]
    return rules
def lsysgen(axiom,rules_unformatted,iterations):
    next_gen = ''
    rules=rules_formatter(rules_unformatted)
    axiom=axiom
    for i in range(iterations):
        next_gen=''
        for x in axiom:
            if x in rules:
                #print(x,rules[x])
                next_gen+=rules[x]
            else:
                #print(x)
                next_gen+=x
            axiom = next_gen
    if iterations==0:
        next_gen=axiom 
    #print(next_gen)
    return next_gen


