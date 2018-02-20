import random

answer = random.randit(0,5)

guess = int(raw_input("enter a number, 0-5:"))

print(answer,guess)

if(guess > answer):
	print("your number is too high")
	guess = int(raw_input("enter a number, 0-5:"))
	if(guess > answer):
		print("your number is still too hight")
	elif(guess < answer):
		print("your number is too low")
	elif(guess == answer):
		print("good job! you got my number!")

answer = random.randit(0,5)

guess = int(raw_input("enter a number, 0-5:"))

elif(guess < answer):
	print("your number is too low")
	guess = int(raw_input("enter a number, 0-5:"))
	elif(guess < answer):
		print("your number is till too low")
	elif(guess > answer):
		print("your number is too high")
	elif(guess == answer):
		print("good job! you got my number!")

elif(guess == answer):
	print("yes, you guessed my number")

