import re

with open ('input.txt', 'r') as file:
    data = file.read()

def isValid(input: str):
    pairs = re.split('\s', input)
    dataset = set()

    for pair in pairs:
        pair = pair.split(':')
        dataset.add(pair[0])
    
    if len(dataset) != len(pairs):
        return False
    elif len(pairs) == 7:
        if 'cid' not in dataset:
            return True
        else:
            return False
    elif len(pairs) == 8:
        return True
    else:
        return False

def part1():
    passports = str(data).split('\n\n')
    count = 0

    for passport in passports:
        if isValid(passport):
            count += 1
    print(count)

part1()