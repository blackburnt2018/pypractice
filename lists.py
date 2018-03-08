socks = "socks"
jeans = "jeans"
laptop = "laptop"
toiletries = "toiletries"
shirts = "shirts"

luggage = []

done = "n"
while(done != "y"):
	item1 = raw_input("what would you like to pack?")
	luggage.append(item1)
	done = raw_input("add another item? y/n")


for items in luggage:
	print(items.upper())















#item2 = raw_input("what else would you like to pack?")
#luggage.append(item2)

#item3 = raw_input("what else would you like to pack?")
#luggage.append(item3)

#item4 = raw_input("what else would you like to pack?")
#luggage.append(item4)

#item5 = raw_input("what final item would you like to pack?")
#luggage.append(item5)

#print(luggage)
#print(luggage[0,4])







grades = [
96.0,
100.0,
75.5,
89.5
]

sum = 0
for grade in grades:
	sum = sum + grade
	print(sum)
