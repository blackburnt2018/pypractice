RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'
YELLOW = '\033[93m'



def printred(message):
	print(RED + message + RESET)

def printgreen(message):
	print(GREEN + message + RESET)

def printyellow(message):
	print(YELLOW + message + RESET)

def printrgy(message):
	letterIndex = 0
	newmessage = ""
	while(letterIndex < len(message)):
		if(letterIndex % 3 == 0):
			newmessage += RED
		elif(letterIndex % 3 == 1):
			newmessage += GREEN
		elif(letterIndex % 3 == 2):
			newmessage += YELLOW 
		newmessage = newmessage + message[letterIndex]
		letterIndex +=1
	print(newmessage + RESET)
printrgy("jingle bells is an old song and i'm really tired")
for x in range(10):
	printyellow("hello")
	printyellow("goodbye")
