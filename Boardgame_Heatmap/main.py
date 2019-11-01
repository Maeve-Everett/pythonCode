import random

players = 0
turns = 0
playerPos = []
playerLS = []
landed = []

# Setting up the sim
while True:
	temp = input("Enter the amount of players you want to simulate (normal game is 2-4 players): ")
	if temp.isnumeric:
		players = int(temp)
		break
	else:
		print("Enter a number")

while True:
	temp = input("Enter the amount of turns that you want to simulate: ")
	if temp.isnumeric:
		turns = int(temp)
		break
	else:
		print("Enter a number")


# Creating player positions list
for i in range(players):
	playerPos.append(0)
	if random.randint(1,2) == 1:
		playerLS.append(1) # Long route
	else:
		playerLS.append(2) # Short route



# turns
for n in range(players):
	for i in range(turns):
		roll = random.randint(1,6) + random.randint(1,6)
		if playerLS[n] == 1: # if the player has completed a lap on the long route,
			if playerPos[n] + roll >= 42: # +1 to route length to count for start tile i think
				#playerPos[n] = playerPos[n] - 42 + roll
				break
			else:
				playerPos[n] = playerPos[n] + roll
				landed.append(playerPos[n])
		else:
			if playerPos[n] + roll >= 33:
				#playerPos[n] = playerPos[n] - 33 + roll
				break
			else:
				playerPos[n] = playerPos[n] + roll
				landed.append(playerPos[n])

print(landed)
landed.sort()
print(landed)
for i in range(0, 42):
	print(i, landed.count(i))
