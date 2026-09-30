# alphabets - A,B

oldstring = "A" #axiom
newstring = ""

# l system's rules -
#replace a with ab
#replay b with a

def new_l_rule():
    global newstring,oldstring
    for i in oldstring:
        if i == 'A':
            newstring+='AB'
        if i == 'B':
            newstring+='A'

def gen2(num_gen):
    global newstring,oldstring
    for i in range(num_gen):
        new_l_rule()
        print(f"Generation {i} : {oldstring}")
        oldstring = newstring
        newstring = ""

def l_rule(newstring,oldstring):
    for i in oldstring:
        if i == 'A':
            newstring+='AB'
        if i == 'B':
            newstring+='A'
    return newstring

def gen(num_gen,newstring,oldstring):
    for i in range(num_gen):
        newstring = l_rule(newstring,oldstring)
        print(f"Generation {i} : {oldstring}")
        oldstring = newstring
        newstring = ""
        
        
        

#gen(10,newstring,oldstring)
gen2(10)