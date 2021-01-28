# Vetor N  de numeros diferentes
# Dois inteiros I e F
# Ver quantos pares então no intervalo de I até F 

quantity, minimum, maximum  = (int(i) for i in input().split())
values = [int(i) for i in input().split()]

# Inicialmente fiz usando 2 loops e calculando possibilididade a possibilidade, mas isso fica n^2. Podemos melhorar para nlogn como abaixo:

totalPars = 0
fixed = values[-1]
fixedIndex = quantity - 1
currentIndex = quantity - 2 # queremos o penultimo item

while fixedIndex != 0:
    while currentIndex != -1:
        prev = values[currentIndex]
        parSum = prev + fixed

        # print(fixed, "+", prev)
		
        if parSum >= minimum and parSum <= maximum:
            totalPars += 1
		
        currentIndex -= 1

    fixed = values[fixedIndex - 1]
    fixedIndex -= 1
    currentIndex = fixedIndex - 1 # queremos o penultimo item

print(totalPars)