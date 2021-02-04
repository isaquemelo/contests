baseSet = {
	'W': 1,
	'H': 0.5,
	'Q': 0.25,
	'E': 0.125,
	'S': 0.0625,
	'T': 0.03125,
	'X': 0.015625
};

while True:
	data = input();

	if data == '*':
		break

	case = data.strip('/').split("/");
	successfulBranches = 0

	for branch in case:
		branchSum = 0

		for time in branch:
			branchSum += baseSet[time]

		if branchSum == 1:
			successfulBranches += 1

	print(successfulBranches)