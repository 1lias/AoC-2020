import time

with open('day1a-input.txt', 'r') as file:
    data = file.read()

lines = str(data).splitlines()

def expenseReport(numbers, k, n, product):
    numbers.sort(key=int)
    numbers = list(map(int, numbers))

    lhs = 0
    rhs = len(numbers) - 1

    for number in numbers:
        if (n > 2):
            if expenseReport(numbers, k - number, n - 1, number*product):
                return True
        else:
            while (lhs < rhs):
                sum = numbers[lhs] + numbers[rhs]
                if sum == k:
                    print(product*numbers[lhs]*numbers[rhs])
                    return True
                elif (sum < k):
                    lhs += 1
                else:
                    rhs -= 1
        
start = time.time()
expenseReport(lines, 2020, 2, 1) # part 1: 494475
end = time.time()
print("Time for part 1:", start-end) 

start = time.time()
expenseReport(lines, 2020, 3, 1) # part 2: 267520550
end = time.time()
print("Time for part 2:", start-end)