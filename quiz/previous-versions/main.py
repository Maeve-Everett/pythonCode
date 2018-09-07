#Python code for NEA

import random #imports the random class
import csv #imports the csv class
import os #imports the os class

username = ''
userIsAdmin = False
score = 0
topic = ''
diff = ''


def login():
    global username
    global userIsAdmin
    print("Login")
    userExists = False #This variable is used to stop the while loop
    while userExists == False:
        print("Enter your username")
        username = input()
        with open ('userProfiles.csv', 'r') as csvfile:
            temp = csv.reader(csvfile, delimiter = ',')
            for row in temp:
                if username == row[0]:
                    print("User Found")
                    userExists = True
                    userPassword = row[1]
                    if row[3] == 'Admin':
                        userIsAdmin = True
        if userExists == False:
            print("User does not exist, try again")
    passCorrect = False
    while passCorrect != True:
        print("Enter your password")
        password = input()
        if password == userPassword:
            print("Correct Password")
            passCorrect = True
        else:
            print("Incorrect Password, Try again")
    print("Welcome back", username)

def signup():
    global username
    print("Signup")
    print("Enter your name")
    name = input()
    print("Enter your age")
    age = input()
    x = True
    while x == True:
        if age.isnumeric():
            x = False
        else:
            print("Only enter a number")
            print("Enter your age")
            age = input()
    x = True
    while x == True:
        print("Enter your year number (e.g. 10 or 11)")
        year = input()
        if age.isnumeric():
            x = False
        else:
            print("Only enter a number")
    x = True
    while x == True:
        print("Enter your password")
        password = input()
        print("Re-Enter your password")
        rePassword = input()
        if password == rePassword:
            print("The passwords match")
            x = False
        else:
            print("The passwords do not match")
    count = 0
    for i in name:
        if count < 3:
            username = username + i
        count = count + 1
    username = username + age
    print("Your username is: ", username)
    userProfiles = open('userProfiles.csv', 'a', newline='')
    with userProfiles as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        writer.writerow([username, password, name, year, age])

def quiz():
    global score
    global topic
    global diff

    print("Would you like to do computer science (1) or history (2)?")
    topicA = True
    while topicA == True:
        topic = input()
        if topic == '1':
            topic = 'CompSci'
            topicA = False
        elif topic == '2':
            topic = 'His'
            topicA = False
        else:
            print("Only enter 1 or 2")
            topic = input()
    print("Would you like to play in easy (1), medium (2) or hard (3)?")
    diffA = True
    while diffA == True:
        diff = input()
        if diff == '1':
            diffA = False
        elif diff == '2':
            diffA = False
        elif diff == '3':
            diffA = False
        else:
            print("Only enter 1, 2 or 3")
            diff = input()
    ansLoc = 0
    userAns = ''
    if topic == 'CompSci':
        print("Computer Science")
        with open('compSci.csv', 'r') as csvfile:
            cs = csv.reader(csvfile, delimiter = ',')
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
    elif topic == 'His':
        print("History")
        with open('his.csv', 'r') as csvfile:
            cs = csv.reader(csvfile, delimiter = ',')
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
    print("You scored ",score,"/5")
    if diff == '1':
        diff = 'Easy'
    elif diff == '2':
        diff = 'Medium'
    elif diff == '3':
        diff = 'Hard'

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
        while y.isnumeric() == False:
            print("Only enter the number of your choice")
            y = input()
        if y == '1':
            print("Enter the name of the student you want a report of")
            z = input()
            with open('userScores.csv', 'r') as csvfile:
                search = csv.reader(csvfile, delimiter = ',')
                os.remove(z+'.txt')
                for row in search:
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
        elif y == '2':
            print("1. Computer Science")
            print("2. History")
            print("Enter the number of your choice")
            topic = input()
            while topic.isnumeric() == False:
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
            while diff.isnumeric() == False:
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
            c = True
            while c == True:
                with open('userScores.csv', 'r') as csvfile:
                    search = csv.reader(csvfile, delimiter = ',')
                    for row in search:
                        if row[2] == diff:
                            if int(row[3]) == topScore:
                                print("\nName: "+row[0])
                                print("Score: "+row[3])
                                count = count+1
                    if topScore == 0:
                        print("No Results Found")
                        c = False
                    elif count == 0:
                        topScore = topScore - 1
                    else:
                        c = False
            print("\n")
        elif y == '3':
            print("1. Computer Science")
            print("2. History")
            print("Enter the number of your choice")
            topic = input()
            while topic.isnumeric() == False:
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
            while diff.isnumeric() == False:
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
                            sum = sum + int(row[3])
                            count = count + 1
            avg = sum/count
            print("The average score is: ",avg)
        elif y == '4':
            print("Exiting")
            x = False
        else:
            print("Only enter the number you want")

def saveData():
    with open('userScores.csv', 'a', newline = '') as csvfile:
        cs = csv.writer(csvfile, delimiter = ',')
        cs.writerow([username, topic, diff, score, ''])

def main():
    print("Quiz")
    print("Do you want to login (1) or signup (2)?")
    x = True
    while x == True:
        y = input()
        if y == '1' or y == '2':
            x = False
        else:
            print("Only enter the number that corresponds to your choice")
    if y == '1':
        login()
    else:
        signup()
    if userIsAdmin == True:
        admin()
    else:
        quiz()
        saveData()
    print("Thank you for using this program")

main()
input("\nPress any key to end the program\n")
