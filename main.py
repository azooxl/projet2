from random import randint
import os 
x = 4
y = x
tableau = [[randint(0,1) for k in range(x)]for i in range(y)]

def aff():
    for i in range(len(tableau)):
        print(tableau[i])

def cel(x, y, tableau):
    return tableau[y][x]

# aff()

a = 1
a = int(a)
for i in range(len(tableau)):
    for j in range(len(tableau[i])):
        (tableau[i][j - 1] == 1)
        (tableau[i][j + 1] == 1)
        (tableau[i + 1][j + 1] == 1)
        (tableau[i + 1][j - 1] == 1)
        (tableau[i - 1][j + 1] == 1)
        (tableau[i - 1][j - 1] == 1)
        (tableau[i - 1][j] == 1)
        (tableau[i + 1][j] == 1)
        

#clear = lambda: os.system('cls')
#clear()





