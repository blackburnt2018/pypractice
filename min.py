def min(nums):
	smallest = nums[0]
	for candidate in nums:
		if(candidate < smallest):
			smallest = candidate
	return smallest


#list_of_numbers = [5,1,6,8,3,4,9,-5,-3]
#print(min(list_of_numbers))

#list_of_floats = [5.3,4.0,0.2]
#smallest_float = min(list_of_floats)
#print(smallest_float)
