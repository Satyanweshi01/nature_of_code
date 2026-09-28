# alphabets - A,B

oldstring = "A" #axiom
newstring = ""

# l system's rules -
#replace a with ab
#replay b with a

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
        
        
        

gen(10,newstring,oldstring)