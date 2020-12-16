import re

with open ('/Users/hexagon/Developer/AoC-2020/day4/input.txt', 'r') as file:
    data = file.read()

passports = str(data).split('\n\n')

def isDataPresent(input: str):
    pairs = re.split(r'\s', input)
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

def isValid(input: str):
    pairs = re.split(r'\s', input)
    dataDict = {}
    for pair in pairs:
        pair = pair.split(':')
        dataDict[pair[0]] = pair[1]
    
    if checkBYR(dataDict['byr']) and checkIYR(dataDict['iyr']) and checkEYR(dataDict['eyr']) and checkHGT(dataDict['hgt']) and checkHCL(dataDict['hcl']) and checkECL(dataDict['ecl']) and checkPID(dataDict['pid']):
        return True    
    return False

def checkBYR(year: str): #checked
    if 1920 <= int(year) <= 2002:
        if len(year) == 4:
            return True
    return False      

def checkIYR(year: str): #checked
    if 2010 <= int(year) <= 2020:
        if len(year) == 4:
            return True
    return False

def checkEYR(year: str): #checked
    if 2020<= int(year) <= 2030:
        if len(year) == 4:
            return True
    return False

def checkHGT(height: str): #checked
    digit = re.findall(r'\d+', height)
    if "cm" in height:
        if 150 <= int(digit[0]) <= 193:
            return True
    if "in" in height:
        if 56 <= int(digit[0]) <= 76:
            return True
    return False

def checkHCL(color: str): #checked
    if re.match(r'#[a-fA-F0-9]', color):
        if len(color) == 7:
            return True
    return False

def checkECL(color: str): #checked
    if color == 'amb' or color == 'blu' or color == 'brn' or color == 'gry' or color == 'grn' or color == 'hzl' or color == 'oth':
        return True
    return False

def checkPID(passport: str): #checked
    if re.match(r'[0-9]', passport):
        if len(passport) == 9:
            return True
    return False


def part1():
    count = 0

    for passport in passports:
        if isDataPresent(passport):
            count += 1
    print(count)

def part2():
    count = 0

    for passport in passports:
        if isDataPresent(passport):
            if isValid(passport):
                count += 1
    print(count)


part1()
part2()