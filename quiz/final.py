import random #imports random
import csv #imports csv
import os #imports os

#defining the global variables
username = '' #used to store the username of the user
userIsAdmin = False #used to know if the user is an admin for creating the reports and stuff
score = 0 #score for use in the quiz
topic = '' #topic for saving and using the quiz
diff = '' #difficulty for saving and using the quiz

def login(): #The login function
	global username #Loading the global variables
	global userIsAdmin
	print("Login")
	userExists = False #Used to exit the while loop
	while userExists == False: #While the user does not exist to this code
		username = input("Username: ") #Asks for the user's username
		with open("userProfiles.csv", "r") as csvfile: #Opens the csv file that has the user information
			cs = csv.reader(csvfile, delimiter = ',')
			for row in cs: #For each row in the file do this code
				if username == row[0]: #if the username that the user entered equals the username slot in the file
					print("User Found")
					userExists = True #Changes the variable to exit the while loop
					userPassword = row[1] #Saves the password to a variable for later
					if row[3] == 'Admin': #Checks to see if the user is an admin
						userIsAdmin = True #Sets userIsAdmin to True if the user is the admin
		if userExists == False: #If the user doesn't exist do this code
			print("Couldn't find user profile, Try again")
	passCorrect = False #Used to exit the while loop
	while passCorrect == False: #While the password is wrong do this code
		password = input("Password: ") #Asks for the user's password
		if password == userPassword: #If the user entered the correct password was correct do this code
			print("Correct password")
			passCorrect = True #Changes the variable to exit the while loop
		else: #If the user ented the wrong password do this code
			print("Incorrect password, Try again")
	print("Welcome back ", username)

def signup(): #The singup command
	global username #Calling the global variable
	print("Signup")
	name = input("Name: ") #Asks for the user's name
	age = input("Age: ") #
	while not age.isnumeric():
		age = input("Only enter a number, Try again\nAge: ")
	year = input("Year: ")
	while not year.isnumeric():
		year = input("Only enter a number, Try again\nYear: ")
	password = input("Password: ")
	rePassword = input("Re-Enter Password: ")
	while not password == rePassword:
		password = input("Passwords didn't match, Try again\nPassword: ")
		rePassword = input("Re-Enter Password: ")
	count = 0
	for i in name:
		if count < 3:
			username += i
		count += 1
	username += str(age)
	print("Username: "+ username)
	with open("userProfiles.csv", "a", newline = '') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',')
		writer.writerow([username, password, name, year, age])

def quiz():
	global score
	global topic
	global diff
	topic = input("Would you like to do computer science (1) or history (2)?\n")
	while not(topic == '1' or topic == '2'):
		topic = input("Only enter 1 or 2\n")
	if topic == '1':
		topic = 'compSci'
	elif topic == '2':
		topic = 'his'
	diff = input("Would you like to play in easy (1), medium (2) or hard (3)?\n")
	while not(diff == '1' or diff == '2' or diff == '3'):
		diff = input("Only enter 1, 2 or 3\n")
	if diff == '1':
		diff = 'Easy'
	elif diff == '2':
		diff = 'Medium'
	elif diff == '3':
		diff = 'Hard'
	ansLocation = 0
	userAns = ''
	with open(topic+'.csv', 'r') as csvfile:
		cs = csv.reader(csvfile, delimiter = ',')
		for row in cs:
			question = row[0]
			ans = row[1]
			print(question)
			fake = True
			while fake == True:
				fake1 = random.randint(2, 4)
				fake2 = random.randint(2, 4)
				fake3 = random.randint(2, 4)
				if fake1 != fake2 and fake1 != fake3 and fake2 != fake3:
					fake = False
			if diff == 'Easy':
				ansLocation = random.randint(1, 2)
				if ansLocation == 1:
					print("1. ", ans)
					print("2. ", row[fake1])
				elif ansLocation == 2:
					print("1. ", row[fake1])
					print("2. ", ans)
			elif diff == 'Medium':
				ansLocation = random.randint(1, 3)
				if ansLocation == 1:
					print("1. ", ans)
					print("2. ", row[fake1])
					print("3. ", row[fake2])
				elif ansLocation == 2:
					print("1. ", row[fake1])
					print("2. ", ans)
					print("3. ", row[fake2])
				elif ansLocation == 3:
					print("1. ", row[fake1])
					print("2. ", row[fake2])
					print("3. ", ans)
			elif diff == 'Hard':
				ansLocation = random.randint(1, 4)
				if ansLocation == 1:
					print("1. ", ans)
					print("2. ", row[fake1])
					print("3. ", row[fake2])
					print("4. ", row[fake3])
				elif ansLocation == 2:
					print("1. ", row[fake1])
					print("2. ", ans)
					print("3. ", row[fake2])
					print("4. ", row[fake3])
				elif ansLocation == 3:
					print("1. ", row[fake1])
					print("2. ", row[fake2])
					print("3. ", ans)
					print("4. ", row[fake3])
				elif ansLocation == 4:
					print("1. ", row[fake1])
					print("2. ", row[fake2])
					print("3. ", row[fake3])
					print("4. ", ans)
			userAns = input("Enter the number of your choice\n")
			while not userAns.isnumeric():
				userAns = input("Only enter the number of your choice\n")
			if userAns == str(ansLocation):
				print("Correct")
				score += 1
			else:
				print("Incorrect")
	print("You scored ", score, "/5")
	percent = score/5
	percent *= 100
	print("Your percentage was ", percent, "%")
	if score == 5:
		print("You got an A")
	elif score == 4:
		print("You got a B")
	elif score == 3:
		print("You got a C")
	elif score == 2:
		print("You got a D")
	elif score == 1:
		print("You got an F")

def admin():
	x = True
	while x == True:
		print("""Would you like to:
		1. Create a report for a student
		2. Find the best mark for a topic
		3. Find the average for a topic
		4. Exit
Enter the number of your choice""")
		y = input()
		while y.isnumeric() == False: #data validation
			print("Only enter the number of your choice")
			y = input()
		if y == '1':
			print("Enter the name of the student you want a report of") #This allows Fergus to make reports on any student
			z = input()
			with open('userScores.csv', 'r') as csvfile:
				search = csv.reader(csvfile, delimiter = ',')
				os.remove(z+'.txt') #This deletes any previous files that were made for that student so it doesnt create duplicata data
				for row in search: #This scans the file for any results by the student he wishes to search for
					if row[0] == z:
						print("Found Test Results")
						print("Writing To File")
						file = open(z+'.txt', 'a') #Opens the file
						file.write("Topic: "+row[1]) #Writes the topic
						file.write("\nDifficulty: "+row[2]) #Writes the difficulty
						file.write("\nScore: "+row[3]+"/5\n\n") #Writes the score
						file.close() #Closes the file
						print("Finished Writing, Continuing Search")
			print("File Creation Complete")
			print("Check "+z+".txt for the report")
		elif y == '2': #This is used if Fergus wants the top scorers for a set topic and difficulty
			print("1. Computer Science")
			print("2. History")
			print("Enter the number of your choice")
			topic = input() #Asks for the input for the topic
			while topic.isnumeric() == False: #data validation
				print("Only enter the number of your choice")
				topic = input()
			if topic == '1': #Changes the topic number so it works better later on in the code
				topic = 'CompSci'
			elif topic == '2':
				topic = 'His'
			print("1. Easy")
			print("2. Medium")
			print("3. Hard")
			print("Enter the number of your choice")
			diff = input()
			while diff.isnumeric() == False: #data validation
				print("Only enter the number of your choice")
				diff = input()
			if diff == '1': #Changes the difficulty number so it works better later on in the code
				diff = 'Easy'
			elif diff == '2':
				diff = 'Medium'
			elif diff == '3':
				diff = 'Hard'
			count = 0
			topScore = 5
			c = True #This variable is used to stop the while loop
			while c == True:
				with open('userScores.csv', 'r') as csvfile: #Opens the file to search
					search = csv.reader(csvfile, delimiter = ',')
					for row in search:
						if row[2] == diff:
							if int(row[3]) == topScore: #If the result is of the correct difficulty and topic it will print the username of the user
								print("\nName: "+row[0])
								print("Score: "+row[3])
								count = count+1
					if topScore == 0: #If none were found it runs this code
						print("No Results Found")
						c = False #Breaks the while loop
					elif count == 0:
						topScore = topScore - 1
					else:
						c = False
			print("\n")
		elif y == '3': #This code get the average score
			print("1. Computer Science")
			print("2. History")
			print("Enter the number of your choice")
			topic = input()
			while topic.isnumeric() == False: #data validation
				print("Only enter the number of your choice")
				topic = input()
			if topic == '1': #Changes the topic number so it works better later on in the code
				topic = 'CompSci'
			elif topic == '2':
				topic = 'His'
			print("1. Easy")
			print("2. Medium")
			print("3. Hard")
			print("Enter the number of your choice")
			diff = input()
			while diff.isnumeric() == False: #data validation
				print("Only enter the number of your choice")
				diff = input()
			if diff == '1': #Changes the difficulty number so it works better later on in the code
				diff = 'Easy'
			elif diff == '2':
				diff = 'Medium'
			elif diff == '3':
				diff = 'Hard'
			with open('userScores.csv', 'r') as csvfile: #Opens 'userScores.csv'
				search = csv.reader(csvfile, delimiter = ',')
				sum = 0
				count = 0
				for row in search:
					if topic == row[1]:
						if diff == row[2]:
							sum = sum + int(row[3]) #This scans through the file and adds the scores to the sum variable
							count = count + 1 #Every time the criteria are met, the count increments so the average can be calculated at the end
			avg = sum/count #This calculates the average from the sum and count from the previous bit
			print("The average score is: ",avg)
		elif y == '4': #This code stops the program
			print("Exiting")
			x = False #Breaks the while loop
		else:
			print("Only enter the number you want")

def saveData(): #This saves the quiz data
	with open('userScores.csv', 'a', newline = '') as csvfile: #This opens the file
		cs = csv.writer(csvfile, delimiter = ',')
		cs.writerow([username, topic, diff, score, '']) #This saves the results

def main(): #The main code
	print("Quiz")
	print("Do you want to login (1) or signup (2)?")
	x = True #This variable is used to stop the while loop
	while x == True: #data validation
		y = input()
		if y == '1' or y == '2': #Asks if they want to signup or login and data validation
			x = False #Breaks the while loop
		else:
			print("Only enter the number that corresponds to your choice")
	if y == '1': #Based on the input of the previous section, the correct code is ran
		login() #Runs the login
	else:
		signup() #Runs the signup
	if userIsAdmin == True: #This runs if Fergus is signed in
		admin() #Runs the admin code
	else:
		quiz() #Runs the quiz
		saveData() #Saves the data
	print("Thank you for using this program")

main() #Runs the main code
#input("\nPress any key to end the program\n") #Stops the program from abruptly closing if in the command prompt/terminal window is open
