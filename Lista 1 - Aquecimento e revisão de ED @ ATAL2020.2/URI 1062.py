while True:
	n = int(input())

	if n == 0: break

	while True:
		array = [ int(i) for i in input().split() ]

		if array[0] == 0:
			break

		stack = []
		current = 0

		for i in range(1, n + 1):
			stack.append(i)

			while len(stack) > 0 and array[current] == stack[-1]:
				current += 1
				stack.pop()

		if len(stack) == 0:
			print("Yes")
		else:
			print("No")

	print()
