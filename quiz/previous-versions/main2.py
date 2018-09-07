#Python code for NEA

import random #imports the random class
import csv #imports the csv class
import os #imports the os class

#setting the global variables
username = '' #The variable that will store the user's username
userIsAdmin = False #This is used in main, it is used to give access to the admin commands
score = 0 #This is the score variable
topic = '' #This saves what topic the user is currently doing
diff = '' #This saves what Difficulty the user is currently doing

def login():
    global username #Calling the golbal variables to edit
    global userIsAdmin
    print("Login")
    userExists = False #This variable is used to stop the while loop
    while userExists == False:
        print("Enter your username")
        username = input()
        with open ('userProfiles.csv', 'r') as csvfile: #Opens the file that stores the user data
            temp = csv.reader(csvfile, delimiter = ',')
            for row in temp:                            #for every row in the file
                if username == row[0]:                  #it checks to see if the username
                    print("User Found")                 #the user entered matches an
                    userExists = True                   #existing user
                    userPassword = row[1]
                    if row[3] == 'Admin': #This checks to see if the user is an admin or not and changes the value accordingly
                        userIsAdmin = True
        if userExists == False: #This code gets ran if it cannot find the user in the file
            print("User does not exist, try again")
    passCorrect = False #This cariable is used to stop the while loop
    while passCorrect != True:
        print("Enter your password")
        password = input()
        if password == userPassword: #This checks to see if the password the user entered matches the one on the file
            print("Correct Password")
            passCorrect = True
        else:
            print("Incorrect Password, Try again")
    print("Welcome back", username)

def signup(): #This is ran to setup a user profile
    global username #Calls the global variable
    print("Signup")
    print("Enter your name")
    name = input() #Asks for their name to make the username from
    print("Enter your age")
    age = input() #Asks for their age to make the username from
    x = True #This variable is used to stop the while loop
    while x == True:
        if age.isnumeric(): #This stops the loop when the user only enters a number and nothing else
            x = False
        else:
            print("Only enter a number") #DATA VALIDATION!!!!
            print("Enter your age") #This makes sure the value will have the right format
            age = input()
    x = True #This variable is used to stop the while loop
    while x == True:
        print("Enter your year number (e.g. '10' or '11')")
        year = input()
        if age.isnumeric(): #MORE DATA VALIDATION!!!!
            x = False
        else:
            print("Only enter a number") #Makes sure the year is imputted correctly
    x = True #This variable is used to stop the while loop
    while x == True:
        print("Enter your password")
        password = input()
        print("Re-Enter your password")
        rePassword = input()
        if password == rePassword: #EVEN MORE DATA VALIDATION!!!!!!!!
            print("The passwords match") #Checks to make sure the user entered the correct password
            x = False
        else:
            print("The passwords do not match")
    count = 0 #This is used to make sure the right number of characters are in the username
    for i in name:
        if count < 3:
            username = username + i #This adds the letters to the username
        count = count + 1 #Increases the count so the right number of characters are in the username
    username = username + age #Adds the age to the username so it is properly formatted eg Kie14
    print("Your username is: ", username)
    with open('userProfiles.csv', 'a', newline = '') as csvfile: #Opens the csv file to save the new user profile
        writer = csv.writer(csvfile, delimiter = ',')
        writer.writerow([username, password, name, year, age]) #Writes all the required data to the file

def quiz():
    global score #Calls all the globals
    global topic
    global diff
    print("Would you like to do computer science (1) or history (2)?")
    topicA = True #This variable is used to stop the while loop
    while topicA == True: #MOAR VALIDATION!!!!
        topic = input()
        if topic == '1':
            topic = 'CompSci' #Sets the topic variable to the right value for later on in hte program
            topicA = False
        elif topic == '2':
            topic = 'His'
            topicA = False
        else:
            print("Only enter 1 or 2")
            topic = input()
    print("Would you like to play in easy (1), medium (2) or hard (3)?")
    diffA = True #This variable is used to stop the while loop
    while diffA == True:
        diff = input() #Sets the difficulty the user wants to take the quiz in
        if diff == '1':
            diffA = False
        elif diff == '2':
            diffA = False
        elif diff == '3':
            diffA = False
        else:
            print("Only enter 1, 2 or 3")
            diff = input()
    ansLoc = 0 #The answer location variable is defined here as python didn't like it getting defined later on in the program
    userAns = '' #The saame problem as the last one
    if topic == 'CompSci': #This is ran if the user wants to do the computer science quiz
        print("Computer Science")
        with open('compSci.csv', 'r') as csvfile: #Opens the quiz file
            cs = csv.reader(csvfile, delimiter = ',')
            for row in cs: #The loop for the quiz
                question = row[0] #This sets the question to a variable because question is easier to remember than 'row[0]'
                ans = row[1] #This was for the same reason but with 'row[1]'
                if diff == '1': #This code is ran if the user wants to do the quiz on the easiest difficulty
                    print(question)
                    ansLoc = random.randint(1, 2) #This randomly places the answer in so the answer list is unique almost every time
                    fake = True #This variable is used to stop the while loop
                    while fake == True:
                        fake1 = random.randint(2, 4) #This code randomly sets the position of the fake answers
                        fake2 = random.randint(2, 4)
                        fake3 = random.randint(2, 4)
                        if fake1 != fake2 and fake1 != fake3 and fake2 != fake3: #This makes sure that all the fake answers are unique positions
                            fake = False
                    if ansLoc == 1: #This is ran if the answer is in the first position
                        print("1. ", ans)
                        print("2. ", row[fake1])
                        x = True #This variable is used to stop the while loop
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1': #THERE'S MORE DATA VALIDATION!?!?                   yup...
                                x = False
                            elif userAns == '2':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 2: #This is ran if the answer is in the second position
                        print("1. ", row[fake1])
                        print("2. ", ans)
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    ansLoc = str(ansLoc) #This changes the answer location to a string so it is comparable to
                    if ansLoc == userAns: #the user answer variable because you can't compare an int to a string
                        score = score+1 #If the user was correct it increments the score
                        print("Correct")
                    else:
                        print("Incorrect")
                elif diff == '2': #This is the code ran for the medium difficulty, unfortunatly I dont have the time to comment all the difficulies
                    print(question)
                    ansLoc = random.randint(1, 3)
                    fake = True
                    while fake == True:
                        fake1 = random.randint(2, 4)
                        fake2 = random.randint(2, 4)
                        fake3 = random.randint(2, 4)
                        if fake1 != fake2 and fake1 != fake3 and fake2 != fake3:
                            fake = False
                    if ansLoc == 1:
                        print("1. ", ans)
                        print("2. ", row[fake1])
                        print("3. ", row[fake2])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 2:
                        print("1. ", row[fake1])
                        print("2. ", ans)
                        print("3. ", row[fake2])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 3:
                        print("1. ", row[fake1])
                        print("2. ", row[fake2])
                        print("3. ", ans)
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    ansLoc = str(ansLoc)
                    if ansLoc == userAns:
                        score = score+1
                        print("Correct")
                    else:
                        print("Incorrect")
                elif diff == '3':
                    print(question)
                    ansLoc = random.randint(1, 4)
                    fake = True
                    while fake == True:
                        fake1 = random.randint(2, 4)
                        fake2 = random.randint(2, 4)
                        fake3 = random.randint(2, 4)
                        if fake1 != fake2 and fake1 != fake3 and fake2 != fake3:
                            fake = False
                    if ansLoc == 1:
                        print("1. ", ans)
                        print("2. ", row[fake1])
                        print("3. ", row[fake2])
                        print("4. ", row[fake3])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            elif userAns == '4':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 2:
                        print("1. ", row[fake1])
                        print("2. ", ans)
                        print("3. ", row[fake2])
                        print("4. ", row[fake3])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            elif userAns == '4':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 3:
                        print("1. ", row[fake1])
                        print("2. ", row[fake2])
                        print("3. ", ans)
                        print("4. ", row[fake3])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            elif userAns == '4':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 4:
                        print("1. ", row[fake1])
                        print("2. ", row[fake2])
                        print("3. ", row[fake3])
                        print("4. ", ans)
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            elif userAns == '4':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    ansLoc = str(ansLoc)
                    if ansLoc == userAns:
                        score = score+1
                        print("Correct")
                    else:
                        print("Incorrect")
    elif topic == 'His': #This is ran if the user wants to take the history quiz
        print("History")
        with open('his.csv', 'r') as csvfile: #This opens the history quiz file
            cs = csv.reader(csvfile, delimiter = ',') #Again, I dont have the time to comment all of this so just refer to the first section, its all the same
            for row in cs:
                question = row[0]
                ans = row[1]
                if diff == '1':
                    print(question)
                    ansLoc = random.randint(1, 2)
                    fake = True
                    while fake == True:
                        fake1 = random.randint(2, 4)
                        fake2 = random.randint(2, 4)
                        fake3 = random.randint(2, 4)
                        if fake1 != fake2 and fake1 != fake3 and fake2 != fake3:
                            fake = False
                    if ansLoc == 1:
                        print("1. ", ans)
                        print("2. ", row[fake1])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 2:
                        print("1. ", row[fake1])
                        print("2. ", ans)
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    ansLoc = str(ansLoc)
                    if ansLoc == userAns:
                        score = score+1
                        print("Correct")
                    else:
                        print("Incorrect")
                elif diff == '2':
                    print(question)
                    ansLoc = random.randint(1, 3)
                    fake = True
                    while fake == True:
                        fake1 = random.randint(2, 4)
                        fake2 = random.randint(2, 4)
                        fake3 = random.randint(2, 4)
                        if fake1 != fake2 and fake1 != fake3 and fake2 != fake3:
                            fake = False
                    if ansLoc == 1:
                        print("1. ", ans)
                        print("2. ", row[fake1])
                        print("3. ", row[fake2])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 2:
                        print("1. ", row[fake1])
                        print("2. ", ans)
                        print("3. ", row[fake2])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 3:
                        print("1. ", row[fake1])
                        print("2. ", row[fake2])
                        print("3. ", ans)
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    ansLoc = str(ansLoc)
                    if ansLoc == userAns:
                        score = score+1
                        print("Correct")
                    else:
                        print("Incorrect")
                elif diff == '3':
                    print(question)
                    ansLoc = random.randint(1, 4)
                    fake = True
                    while fake == True:
                        fake1 = random.randint(2, 4)
                        fake2 = random.randint(2, 4)
                        fake3 = random.randint(2, 4)
                        if fake1 != fake2 and fake1 != fake3 and fake2 != fake3:
                            fake = False
                    if ansLoc == 1:
                        print("1. ", ans)
                        print("2. ", row[fake1])
                        print("3. ", row[fake2])
                        print("4. ", row[fake3])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            elif userAns == '4':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 2:
                        print("1. ", row[fake1])
                        print("2. ", ans)
                        print("3. ", row[fake2])
                        print("4. ", row[fake3])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            elif userAns == '4':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 3:
                        print("1. ", row[fake1])
                        print("2. ", row[fake2])
                        print("3. ", ans)
                        print("4. ", row[fake3])
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            elif userAns == '4':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    elif ansLoc == 4:
                        print("1. ", row[fake1])
                        print("2. ", row[fake2])
                        print("3. ", row[fake3])
                        print("4. ", ans)
                        x = True
                        while x == True:
                            print("Enter the number of your choice")
                            userAns = input()
                            if userAns == '1':
                                x = False
                            elif userAns == '2':
                                x = False
                            elif userAns == '3':
                                x = False
                            elif userAns == '4':
                                x = False
                            else:
                                print("Only enter the number of your choice")
                    ansLoc = str(ansLoc)
                    if ansLoc == userAns:
                        score = score+1
                        print("Correct")
                    else:
                        print("Incorrect")
    print("You scored ",score,"/5") #This prints the score so the user can see how well they did
    if diff == '1': #This changes the difficulty variable for later use in the program
        diff = 'Easy'
    elif diff == '2':
        diff = 'Medium'
    elif diff == '3':
        diff = 'Hard'

def admin(): #This code is ran when Fergus goes on his account
    x = True
    while x == True:
        print("""Would you like to:
        1. Create a report for a student
        2. Find the best mark for a topic
        3. Find the average for a topic
        4. Exit
Enter the number of your choice""")
        y = input()
        while y.isnumeric() == False: #I'M RUNNING OUT OF JOKES, THERE'S SO MUCH VALIDATION!!!!!
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
                        file = open(z+'.txt', 'a')
                        file.write("Topic: "+row[1])
                        file.write("\nDifficulty: "+row[2])
                        file.write("\nScore: "+row[3]+"/5\n\n")
                        file.close()
                        print("Finished Writing, Continuing Search")
            print("File Creation Complete")
            print("Check "+z+".txt for the report")
        elif y == '2': #This is used if Fergus wants the top scorers for a set topic and difficulty
            print("1. Computer Science")
            print("2. History")
            print("Enter the number of your choice")
            topic = input()
            while topic.isnumeric() == False: #SERIOUSLY, I'VE GOT NO MORE JOKE!!!!
                print("Only enter the number of your choice")
                topic = input()
            if topic == '1':
                topic = 'CompSci'
            elif topic == '2':
                topic = 'His'
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("Enter the number of your choice")
            diff = input()
            while diff.isnumeric() == False: #WHAT HAS 4 LETTERS, SOMETIMES 9, NEVER 5
                print("Only enter the number of your choice")
                diff = input()
            if diff == '1':
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
                        c = False
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
            while topic.isnumeric() == False: #I HATE WHEN PEOPLE ASK HOW I SEE MY SELF IN A COUPLE YEARS, I DONT HAVE 2020 VISION
                print("Only enter the number of your choice")
                topic = input()
            if topic == '1':
                topic = 'CompSci'
            elif topic == '2':
                topic = 'His'
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("Enter the number of your choice")
            diff = input()
            while diff.isnumeric() == False: #SET YOUR WIFI PASSWORD TO 2444666668888888 SO WHEN SOMEONE ASKS YOU CAN TELL THEM IT'S 12345678
                print("Only enter the number of your choice")
                diff = input()
            if diff == '1':
                diff = 'Easy'
            elif diff == '2':
                diff = 'Medium'
            elif diff == '3':
                diff = 'Hard'
            with open('userScores.csv', 'r') as csvfile:
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
        elif y == '4':
            print("Exiting")
            x = False
        else:
            print("Only enter the number you want")

def saveData(): #This saves the quiz data
    with open('userScores.csv', 'a', newline = '') as csvfile: #This opens the file
        cs = csv.writer(csvfile, delimiter = ',')
        cs.writerow([username, topic, diff, score, '']) #This saves the results

def main(): #The main code
    print("Quiz")
    print("Do you want to login (1) or signup (2)?")
    x = True
    while x == True: #I THINK THIS IS THE LAST ONE
        y = input()
        if y == '1' or y == '2': #Aks if they want to signup or login
            x = False
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
input("\nPress any key to end the program\n") #Stops the program from abruptly closing if in the command prompt/terminal like window is open
