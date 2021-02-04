while True:
	numberOfReviwers = int(input())

	if numberOfReviwers == 0:
		break
	
	reviwers = [
		# {'total-articles': 0, 'max-articles': 2},
		# {'total-articles': 0, 'max-articles': 1},
		# {'total-articles': 0, 'max-articles': 2},
	]

	availableReviewsSlots = 0

	for i in range(numberOfReviwers):
		maxArticles = int(input())

		reviwers.append({
			'total-articles': 0,
			'max-articles': maxArticles
		})

		availableReviewsSlots += maxArticles

	reviwers = sorted(reviwers, key=lambda k: k['max-articles'], reverse=True) 
	numberOfArticles = int(input())

	if numberOfArticles > availableReviewsSlots:
		print("Impossible")
		continue

	while numberOfArticles > 0:
		for reviewer in reviwers:
			if reviewer['total-articles'] + 1 <= reviewer['max-articles'] and numberOfArticles > 0:
				reviewer['total-articles'] += 1
				numberOfArticles -= 1

	for reviewer in reviwers:
		print(reviewer['total-articles'])

