import time

with open('day2-input.txt', 'r') as file:
    data = file.read()

passwords = str(data).splitlines()

def part1():
    count = 0
    for password in passwords:
        pair = password.split(": ")
        rule = pair[0].split(" ")
        letterRange = rule[0].split("-")

        if int(letterRange[0]) <= pair[1].count(rule[1]) <= int(letterRange[1]):
            count += 1
    print(count)


def part2():
    count = 0
    for password in passwords:
        pair = password.split(": ")
        rule = pair[0].split(" ")
        letterLocs = rule[0].split("-")

        if (pair[1][int(letterLocs[0])-1] is rule[1]) ^ (pair[1][int(letterLocs[1])-1] is rule[1]):
            count += 1
    print(count)

part1() 
part2()
