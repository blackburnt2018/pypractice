def add(a,b):
	c = a+b
	return c
def multiply(a,b):
	c = 0
	for x in range(a):
		c = add(c,b)
	return c
def pow(a,b):
	c = 1
	for x in range(b):
		print(c,"pow")
		c = multiply(a,c)
		
	return c
	

x = pow(6,2)
y = pow(1,2)
z = pow(3,4)
print(x,y,z)
