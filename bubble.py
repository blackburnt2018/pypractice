import swap

nums = [4,1,8,3,2]
print(nums)
x = 0
while(x < len(nums)):
	if(x+1 < len(nums)):
		if(nums[x] > nums[x + 1]):
			nums[x],nums[x+1] = swap.swap(nums[x],nums[x+1])
			x = 0
	x=x+1
print(nums)
