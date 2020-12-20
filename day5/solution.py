# Split the input into two parts work firts with the [FB]* input and then contibue with the [LR]* 
# Plane has 128 rows and 8 columns

with open ('/Users/hexagon/Developer/AoC-2020/day5/input.txt', 'r') as file:
    data = file.read()

passes = str(data).splitlines()

def getRow(row: str):
    count = 0
    rng = list(range(128))
    for ch in row:
        count += 1
        if ch == 'F':
            rng = rng[:int(len(rng)/2)]
        elif ch == 'B':
            rng = rng[int(len(rng)/2):]
    return rng[0]

def getColumn(column: str):
    rng = list(range(8))
    for ch in column:
        if ch == 'L':
            rng = rng[:int(len(rng)/2)]
        elif ch == 'R':
            rng = rng[int(len(rng)/2):]
    return rng[0]

def getSeatID(row: int, column: int):
    return (row*8)+column

def part1():
    seatIDs = []
    for pss in passes:
        row = pss[:7]
        column = pss[7:]
        
        seatIDs.append(getSeatID(getRow(row), getColumn(column)))

    seatIDs.sort(reverse = True)
    print(seatIDs[0])
    return seatIDs

def part2():
    l = part1()
    l.sort()
    rng = list(range(63,935))
    index = 0

    for val in l:
        if rng[index] != l[index]:
            print(rng[index])
            return
        index += 1
        

part2()