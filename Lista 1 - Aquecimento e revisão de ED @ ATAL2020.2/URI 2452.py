def mergeIntervals(arr):     
        # Sorting based on the increasing order  
        # of the start intervals 
		# arr.sort(key = lambda x: x[0])  

        # array to hold the merged intervals 
		m = [] 
		s = -10000
		max = -10000

		for i in range(len(arr)): 
			a = arr[i] 
			# print("COMPARE", a[0], max)
			if a[0] - 1 > max: 
				if i != 0: 
					m.append([s,max]) # [2,2], [6,6]
				max = a[1] # 2  6
				s = a[0]  # 2  6
			else: 
				if a[1] >= max: 
					max = a[1]
		if max != -100000 and [s, max] not in m: 
			m.append([s, max]) 
			
		#'max' value gives the last point of  
		# that particular interval 
		# 's' gives the starting point of that interval 
		# 'm' array contains the list of all merged intervals 
		return m;


# print(tryMerge([[0,3], [1,8], [11,13]]))
# print(tryMerge([[0,9], [10,13]]))
# print(tryMerge([[1,1], [6,6], [13,13]]))


def genIntervals(filledPositions):
	intervals = []
	for i in range(len(filledPositions)):
		intervals.append([filledPositions[i], filledPositions[i]])

	return intervals

def processDay(intervals, totalSize):
	if len(intervals) == 1:
		if (intervals[0][0] == 1 and intervals[0][1] == totalSize):
			return True

	for i in range(len(intervals)):
		minValue = intervals[i][0]
		maxValue = intervals[i][1]

		if minValue - 1 >= 1:
			intervals[i][0] = minValue - 1
		else:
			intervals[i][0] = minValue

		if maxValue + 1 <= totalSize:
			intervals[i][1] = maxValue + 1
		else:
			intervals[i][1] = maxValue
	
	return mergeIntervals(intervals)



# baseIntervals = genIntervals([9, 10])
# totalSize = 10

# baseIntervals = genIntervals([2, 6, 13])
# totalSize = 13

# baseIntervals = genIntervals([1, 2, 3, 4])
# totalSize = 5


totalSize, _ = ( int(i) for i in input().split())
baseIntervals = genIntervals([int(i) for i in input().split()])

dayCount = 0

while True:
	# print(baseIntervals)
	baseIntervals = processDay(baseIntervals, totalSize)
	# print(baseIntervals)
	# print()	
	if baseIntervals == True:
		print(dayCount)
		break;

	dayCount += 1

# print(mergeIntervals([[1, 4], [4, 8], [11, 13]]))
