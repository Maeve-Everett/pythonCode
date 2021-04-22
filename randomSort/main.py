import random
import time
import numpy

x = []
n = 6

randomSortTime = []
bogoSortTime = []

for i in range(1, n+1): # 1 to 100-1, ie 99
    x.append(i)

random.shuffle(x)

def checkOrder():
    last = 0
    for i in x:
        if i > last:
            last = i
        else:
            return True
    return False


def randomSort():
    while checkOrder():
        last = 0
        count = 0
        current = 0
        for i in x:
            #if i < last:
            #    current = i
            #    x.insert(random.randint(0, n-1), x[count]) # randint inclusive
            #    if current == x[count]:
            #        del x[count]
            #    else:
            #        del x[count+1]
            if i > last:
                current = i
                x.insert(random.randint(0, n-1), x[count])
                if current == x[count]:
                    del x[count]
                else:
                    del x[count+1]
            #input(x)
            count += 1
        #print(x)

def bogoSort():
    while checkOrder():
        random.shuffle(x)


iterations = int(input("Iterations: "))

for i in range(1, iterations+1):
    #print(i)

    startTime = time.time()
    random.shuffle(x)
    randomSort()
    randomSortTime.append(time.time() - startTime)

    startTime = time.time()
    random.shuffle(x)
    bogoSort()
    bogoSortTime.append(time.time() - startTime)

print("Random Sort Average: ", numpy.average(randomSortTime))
print("Bogo Sort Average: ", numpy.average(bogoSortTime))