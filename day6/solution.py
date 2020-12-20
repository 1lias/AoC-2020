# number: 26 yes-or-no questions - marked as a to z
# Duplicate answers to the same question don't count extra; each question counts at most once.

with open ('/Users/hexagon/Developer/AoC-2020/day6/input.txt', 'r') as file:
    data = file.read()

groups = str(data).split('\n\n')

def part1(data: [str]):
    sums = []
    for group in data:
        collection = set()
        for char in group:
            if char != '\n':
                collection.add(char)
        sums.append(len(collection))
    count = 0
    for num in sums:
        count += num
    print(count)

def part2(data: [str]):
    sums = []
    for group in data:
        dictionary = dict()
        groupCount = 0
        for single in group.splitlines():
            groupCount += 1
            for char in single:
                if char not in dictionary:
                    dictionary[char] = 1
                else :
                    dictionary[char] += 1
        count = 0
        for char in dictionary:
            if dictionary[char] == groupCount:
                count += 1
        sums.append(count)  
    print(sum(sums))




                
        


part1(groups)
part2(groups)

    

