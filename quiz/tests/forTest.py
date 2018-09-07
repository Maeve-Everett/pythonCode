x = input()
y = ''
count = 0
for i in x:
    print(i)
    if count < 3:
        y = y+i
    count = count + 1
print(y)
