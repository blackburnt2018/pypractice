import min

numbers = [5,4,3,5,1,5,2]


ordered = []
while(len(numbers) > 0):
	smallest = min.min(numbers)
	ordered.append(smallest)
	numbers.remove(smallest)

print(ordered)
