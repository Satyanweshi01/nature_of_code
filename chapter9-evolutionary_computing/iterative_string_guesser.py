import random

theString = "c"

wordPool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']
guessing = True
gen = 0
while guessing:
    guessedString = ""
    for i in range(len(theString)):
        randomChar = random.choice(wordPool)
        guessedString+=randomChar
    print(f"gen {gen}: {guessedString}")
    gen+=1
    if guessedString == theString:
        guessing == False
    