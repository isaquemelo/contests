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