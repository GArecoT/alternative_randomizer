import random

def alternative_generator(a, b, c, d):
    alternative = random.randint(0,4)

    if(alternative != a and alternative != b and alternative != c and alternative != d):
        return alternative
    else:
        return alternative_generator(a,b,c,d)

def alternative_translator(alternative):
    if alternative == 0:
        return "A"
    if alternative == 1:
        return "B"
    if alternative == 2:
        return "C"
    if alternative == 3:
        return "D"
    if alternative == 4:
        return "E"

alternativas = ["", "", "", "", ""]

while 1 < 2:
    print("\n\n---------- ENTRADA ----------\n\n")
    alternativas[0] = input("A) ")
    alternativas[1] = input("B) ")
    alternativas[2] = input("C) ")
    alternativas[3] = input("D) ")
    alternativas[4] = input("E) ")

    
    print("\n---------- SAÍDA FORMATADA ----------\n")
    a = alternative_generator(5,5,5,5)
    print("A)",alternativas[a])

    b = alternative_generator(a,5,5,5)
    print("B)",alternativas[b])

    c = alternative_generator(a,b,5,5)
    print("C)",alternativas[c])

    d = alternative_generator(a,b,c,5)
    print("D)",alternativas[d])

    e = alternative_generator(a,b,c,d)
    print("E)",alternativas[e])

    print("\n---------- SAÍDA ----------\n")

    print(alternativas[a])
    print(alternativas[b])
    print(alternativas[c])
    print(alternativas[d])
    print(alternativas[e])

    print("\n\n><><><><><><><><><><><><><><><><><><><><><><><><><><><><\n\n")

