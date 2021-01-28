# Recebe comprimento do tubo e dps a quantidade

# 2 2

# 10 5

# tapetes = [ x0, x1, x2, x3, x4 ]

# A soma de todos os tapetes tem que dar no maximo 10

# x0 + x1 + x2 + x3 + x4 = 10

# cada x vai até no maximo 10

# 1 + 1 + 2 + 4 + 2 = 10 

# comecar atribuindo valor maximo menos numero para completar
# ex. max = 10, eu preciso preencher 4 então (10 - 4) = 6

# 6 + 1 + 1 + 1 + 1 = 10

# Se a quantidade de valores que eu tenho a frente excede o numero de tapetes que eu poderia formar

# (x > x1) então (x^2 > x1^2). Se x1 == x2 == x3 ... xn, e xn = 1, x^2 > (sum(x, 1, n))^2


tubeSize, quantity = (int(i) for i in input().split())
maxCarpet = tubeSize - (quantity - 1)
print( (maxCarpet** 2) + quantity - 1)