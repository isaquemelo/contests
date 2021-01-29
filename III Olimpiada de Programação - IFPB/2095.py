marker = 0

def binarySearch(needle, size, bucket):
    global marker

    l = size - 1; 
    found = False

    while marker <= l:
        middle = int((marker + l) / 2)

        if needle <= bucket[middle]:
            l = middle - 1
        elif needle > bucket[middle]:
            found = True
            marker += 1
            break

    if found:
        return 1
    else:
        return 2



quantityOfMen = int(input())

armyA = [ int(i) for i in input().split() ]
armyB = [ int(i) for i in input().split() ]

armyA.sort() 
armyB.sort()


k = 0
count = 0

for i in range(quantityOfMen):
    k = binarySearch(armyB[i], quantityOfMen, armyA)
    
    if k == 1:
        count += 1

print(count)