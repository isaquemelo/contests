def makeMove(deck):
	removedItem = deck.pop(0)
	deck.append(deck[0])
	deck.pop(0)

	return (deck, removedItem)

while True:
	quantityOfCards = int(input())
	
	# End of cases
	if quantityOfCards == 0:
		break

	# Create deck and removed cards
	deck = [i for i in range(1, quantityOfCards + 1)]
	removedItens = []

	while len(deck) >= 2:
		deck, removedItem = makeMove(deck)
		removedItens.append(removedItem)
	
	print("Discarded cards: ", end="" )

	for i in range(len(removedItens)):
		if i == len(removedItens) - 1:
			print(str(removedItens[i]), end="")
		else:
			print(str(removedItens[i]) + ", ", end="")

	print("\nRemaining card:", deck[0])
	# print(deck, removedItens);

	#break;
	
	
