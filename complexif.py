name = raw_input("enter your first name")
password = raw_input("enter your password")

if((name == "omer" and password == "dinosaur") or(name == "pan" and password == "matter")):
	print("you are logged in")
else:
	print("access denied")


if(not(name == "omer" or name == "tom" or name == "trent")):
	print("that's a cool name")
else:
	print("hmm I don't know that name")
