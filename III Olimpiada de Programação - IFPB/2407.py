# Soma dos N números em:
# - Linha
# - Coluna
# - Diagonal principal

# tem que ter o mesmo valor, não pode ter numeros repetidos.


def checkMagic(matrix, magicNumber):
    diagonalSum = 0

    # Check diagonal
    for i in range(n):
        diagonalSum += matrix[i][i]

    if diagonalSum != magicNumber:
        print('0')
        return


    # Check row / line
    for line in matrix:
        if sum(line) != magicNumber:
            print('0')
            return

    # Check column
    for i in range(n):
        columnSum = 0

        for j in range(n):
            columnSum += matrix[j][i]
        
        if columnSum != magicNumber:
            print('0') 
            return

    print(magicNumber)

n = int(input())
matrix = []
magicNumber = 0
numbers = {  }
flag = False

for i in range(n):
    line = [int(i) for i in input().split(" ")]
    matrix.append(line)

    for number in line:
        if number in numbers:
            flag = True
        else:
            numbers[number] = 1

    if i == 0:
        magicNumber = sum(line)

if flag:
    print('0')
else:
    checkMagic(matrix, magicNumber)