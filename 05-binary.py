def binarySearch(items, target):
	i, j = 0, len(items)-1
	mid = 0
	while i <= j:
		mid = (i+j) // 2
		if items[mid] == target:
			return mid
		elif items[mid] < target:
			i = mid + 1
		else:
			j = mid - 1
	return -1

print(binarySearch([1,2,3,4,5,6], 6))