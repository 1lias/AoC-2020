# I would like to check each number and subtract it from 2020. Then search the table for the number that I find. 
#  If that number is not found then I continue with the next number. I believe I should put the whole list in a hash.

# Gotta find a much much more optimised way to solve this...
import time


with open('day1a-input.txt', 'r') as file:
    data = file.read()

lines = str(data).splitlines()

def expenseReport(numbers, k):
    numbers.sort(key=int)
    numbers = list(map(int, numbers))
    lhs = 0
    rhs = len(numbers) - 1
    while (lhs < rhs):
        sum = numbers[lhs] + numbers[rhs]
        if sum == k:
            print(numbers[lhs]*numbers[rhs])
            return
        elif (sum < k):
            lhs += 1
        else:
            rhs -= 1
        
start = time.time()
expenseReport(lines, 2020)
end = time.time()
print(start-end)
    

# Correct answers: 
# 1: 494475
# 2: 267520550