from random import randint
x = randint(1,10)
y = x
tableau = [[randint(0,1) for k in range(x)]for i in range(y)]

def aff():
    for i in range(len(tableau)):
        print(tableau[i])

def cel(x, y, tableau):
    return tableau[y][x]

aff()