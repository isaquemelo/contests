instanceCounter = 1

while True:
	signature = input()

	if signature == '0':
		break

	number = input()

	if instanceCounter != 1:
		print()
	
	print("Instancia", instanceCounter)

	if signature in number:
		print("verdadeira")
	else:
		print("falsa")
	
	instanceCounter += 1
