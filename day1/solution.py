# We are given a number of lock rotations.
# The password is the number of times the lock is left pointing at 0.

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
data = open(folder_path + 'day1/data.txt', 'r').readlines()

dial = 50
answer = 0

for instruction in data:
    direction, amount = instruction[0], int(instruction[1:])
    if direction == 'L':
        dial -= amount
    else:
        dial += amount
    dial = dial % 100

    if dial == 0:
        answer += 1
    
print(answer)

# Part 2 asks us to additionally track moments when the lock crosses 0. 

dial = 50
answer = 0

for instruction in data:
    direction, amount = instruction[0], int(instruction[1:])
    if direction == 'L':
        dial -= amount
        # If we started at 0, don't include this moment as a cross.
        if (dial + amount) % 100 == 0:
            crosses = abs(dial // 100) - 1
        else:
            crosses = abs(dial // 100)
    else:
        dial += amount
        # If we end up at 0, don't include this moment as a cross.
        if dial % 100 == 0:
            crosses = abs(dial // 100) - 1
        else:
            crosses = abs(dial // 100)
    
    dial %= 100

    if dial == 0:
        answer += 1

    answer += crosses

print(answer)

