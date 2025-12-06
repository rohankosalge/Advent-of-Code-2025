# We need to find the maximum total joltage.
# joltage per bank = max 2-digit pairing.

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
raw = open(folder_path + 'day3/data.txt', 'r').readlines()

data = [list(bank[:100]) for bank in raw]

answer = 0

for bank in data:
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            max_joltage = max(max_joltage, int(bank[i] + bank[j]))

    answer += max_joltage

print(answer)


# Part 2 asks us to redefine max joltage per bank = max 12-digit pairing.

answer = 0

# The brute force idea was to have 12 nested for loops.
# But that approach was taking way too long to execute.

# Greedy approach.
# Find the largest number before the last 11 digits.
# Then past that number, find the largest number before the last 10 digits.
# So on, so forth.

for bank in data:
    bank_list = [int(battery) for battery in bank]
    bank_joltage = ''
    l, r = 0, len(bank) - 11
    for i in range(12):
        max_joltage = max(bank_list[l: r])
        bank_joltage += str(max_joltage)
        l = bank_list[l: r].index(max_joltage) + l + 1
        r += 1
    
    answer += int(bank_joltage)

print(answer)