
# Recebe primeiro o numero de trabalhadores, dps a quantidade de etapas e por ultimo o array base


# 3 2 1 0 +
# 0 3 2 1 +
# 1 0 3 2
# ________


# Etapa = etapa + 1
# lista_base = [3, 0, 1, 0] 

# lista_base[0] = lista_base[0] + lista_base[3] -> Etapa 1
# lista_base[0] = lista_base[0] + lista_base[2] -> Etapa 2

# lista_base[1] = lista_base[1] + lista_base[0]
# lista_base[1] = lista_base[1] + lista_base[3]

# lista_base[2] = lista_base[2] + lista_base[1] (sempre o anterior?)
# lista_base[2] = lista_base[1] + lista_base[0]

# lista_base[3] = lista_base[3] + lista_base[2] (sempre o anterior!)
# lista_base[3] = lista_base[1] + lista_base[1]

# 2, 3, 0, 1 qual o padrão?

# (index + etapa) % total



# lista_base[i] = lista_base[i] + lista_base[(i - 1) % total]
# lista_base[i] = lista_base[i] + lista_base[(index + etapa) % total]



workersQuantity, steps  = (int(i) for i in input().split())
baseNumbers = [int(i) for i in input().split()]
newArray = [i for i in baseNumbers]

# print(baseNumbers)

for step in range(1, steps):
    # print(step)
    if step == 1:
        for i in range(workersQuantity):
            newArray[i] = baseNumbers[i] + baseNumbers[(i - 1) % workersQuantity]
    else:
        for i in range(workersQuantity):
            newArray[i] = newArray[i] + baseNumbers[(i + step) % workersQuantity]

for i in range(workersQuantity):
    print(newArray[i], end=" ")
# print(newArray)