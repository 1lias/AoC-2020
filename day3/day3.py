
import time

with open('input.txt', 'r') as file:
    data = file.read()

forest = str(data).splitlines()

def checkSlope(x,y):
    line = 0
    column = 0
    counter = 0
    lineCounter = 0

    for treeLine in forest:
        if lineCounter == 0:
            line += x
            column = (column + y) % len(treeLine)
        elif line == lineCounter:
            if treeLine[column] == '#':
                counter += 1
            line += x
            column = (column + y) % len(treeLine)
        lineCounter += 1
    return counter

# part 1
print(checkSlope(1,3)) # 230
# part 2
print(checkSlope(1,1)*checkSlope(1,3)*checkSlope(1,5)*checkSlope(1,7)*checkSlope(2,1)) # 9533698720