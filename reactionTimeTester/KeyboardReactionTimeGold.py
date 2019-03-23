import time
import keyboard
import random
import tkinter

# Checking to see if GOLD is active
def redCheck():
	return keyboard.is_pressed('r')

# Checking to see if BLACK is active
def blackCheck():
	return keyboard.is_pressed('b')

print("Welcome to the reaction time tester")

def main():
	update.set("                     ")
	window.update_idletasks()
	for i in range(1, 6):
		time.sleep(1)
		update.set(str(6 - i))
		window.update_idletasks()

	time.sleep(random.randint(1, 3))
	update.set("GO!")
	window.update_idletasks()

	redActive = False
	blackActive = False
	startTime = time.time()
	y = True
	while y:
		if redCheck() and not(redActive):
			redTime = time.time()
			redActive = True
		elif blackCheck() and not(blackActive):
			blackTime = time.time()
			blackActive = True
		elif redActive and blackActive:
			y = False

	if redTime < blackTime:
		update.set("Gold Wins!!!")
		window.update_idletasks()
	else:
		update.set("Black Wins!!!")
		window.update_idletasks()

	redUpdate.set("Gold Time: {}".format(redTime-startTime))
	blackUpdate.set("Black Time: {}".format(blackTime-startTime))
	window.update_idletasks()

# Basic window setup
window = tkinter.Tk()
window.title("Reaction time tester")
window.geometry("300x300")

update = tkinter.StringVar()
update.set("Press start")
redUpdate = tkinter.StringVar()
redUpdate.set("Gold Time: ")
blackUpdate = tkinter.StringVar()
blackUpdate.set("Black Time: ")

# Labels and Buttons
title = tkinter.Label(window, text="Reaction time tester")
startbutton = tkinter.Button(window, text="Start", command=main)
countdown = tkinter.Label(window, textvariable=update)
redLabel = tkinter.Label(window, textvariable=redUpdate)
blackLabel = tkinter.Label(window, textvariable=blackUpdate)

# Pack things and draw window
title.pack()
startbutton.pack()
countdown.pack()
redLabel.pack()
blackLabel.pack()
window.mainloop()
