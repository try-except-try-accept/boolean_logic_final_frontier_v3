from random import randint, choice, randrange, shuffle

gates = ["AND", "OR"]
terms = ["A", "B", "C"]

def gen(gates, terms, nots, exp, gates_left):
    try:
        t = terms.pop(0)
        if randint(0, 1) and nots > 0:
            t = "NOT " + t
            nots -= 1
    except (ValueError, IndexError):
        return exp
    g = choice(gates)

    if randint(0, 2) == 0 and len(exp) > 1 or gates_left == 0:
        if randint(0, 1) or nots == 0:
            return exp
        else:
            nots -= 1
            return "NOT " + exp
    elif randint(0, 1) == 0:
        gates_left -= 1
        return gen(gates, terms, nots, f"({exp} {g} {t})", gates_left)
    else:
        gates_left -= 1
        return gen(gates, terms, nots, f"({t} {g} {exp})", gates_left)


    

def generate_expression(stage, gates_left):

    nots = 0

    t = list(terms)
    g = list(gates)



    

    if stage == 1:
        t.pop(0)
        

    if stage > 5:
        g.append("NAND")
    if stage > 6:
        g.append("NOR")
    if stage > 7:
        g.append("XOR")


    t.sort()
        
            

    if stage == 3:
        nots = 1
    elif stage == 4 or stage == 10:
        nots = 2
    elif stage == 5 or stage == 11:
        nots = 3
    elif stage > 11:
        nots += stage-11
        
    
    
    
    first_term = t.pop(0)

    print(gen(g, t, nots, first_term, gates_left // 2))


for _ in range(2):
    
    for i in range(1, 15):

        print(f"stage {i}")
        for j in range(10):
            generate_expression(i, j)
        
        print()
        input()
        
