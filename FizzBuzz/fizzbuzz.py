loops = 100
fizz = 3
buzz = 5
for i in range(loops):
	output = ""
	if i%fizz == 0:
		output += "Fizz"
	if i%buzz == 0:
		output += "Buzz"
	if output == "":
		output = i
	print(output)
