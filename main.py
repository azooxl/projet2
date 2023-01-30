from random import randint
x = 3
y = x
tableau = [[randint(0,1) for k in range(x)]for i in range(y)]

def aff():
    for i in range(len(tableau)):
        print(tableau[i])

def cel(x, y, tableau):
    return tableau[y][x]

# aff()
CopyTableau = tableau
for i in range(len(tableau)):
    for j in range(len(tableau[i])):
        print(tableau[i])
        print(tableau[i][j] == 1)
        weight = 0
        weight = int(weight)
        if tableau [i - 1][j - 1] == 1:
            weight = 1
            weight = int(weight)

        if tableau [i - 1][j] == 1:
            weight = weight + 1
            weight = int(weight)

        if tableau [i - 1][j + 1] == 1:
            weight = weight + 1
            weight = int(weight)

        if tableau [i + 1][j - 1] == 1:
            weight = weight + 1
            weight = int(weight)

        if tableau [i + 1][j + 1] == 1:
            weight = weight + 1
            weight = int(weight)

        if tableau [i + 1][j] == 1:
            weight = weight + 1
            weight = int(weight)

        if tableau [i + 1][j] == 1:
            weight = weight + 1
            weight = int(weight)

        if tableau [i][j + 1] == 1:
            weight = weight + 1
            weight = int(weight)
        
        if weight > 3:
            CopyTableau[i][j] = 0








