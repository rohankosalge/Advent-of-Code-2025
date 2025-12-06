# We are given a number of ID ranges.
# We need to sum up the invalid IDs. Invalid = made up of sequences repeated twice.

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
raw = open(folder_path + 'day2/data.txt', 'r').read().split(',')

data = []
for arange in raw:
    bounds = arange.split('-')
    data.extend(list(range(int(bounds[0]), int(bounds[1])+1)))

answer = 0
for number in data:
    str_number = str(number)
    if len(str_number) % 2 == 1: continue # odd-length numbers cannot satisfy this rule.
    if str_number[:len(str_number) // 2] == str_number[len(str_number) // 2: ]: # check if halves are equal.
        answer += number

print(answer)

# Part 2 asks us to redefine invalid ID's: made up of sequences repeated at least twice.

answer = 0
parts = lambda x,n: [x[i:i+n] for i in range(0, len(x), n)]

for number in data:
    
    str_number = str(number)
    length = len(str_number)
    for i in range(1, length // 2 + 1): # check all factors of the length of the number.
        if length % i == 0 and len(set(parts(str_number, i))) == 1: # split into equal parts and take the set.
            answer += number                                      # cardinality is 1 <-> made up of repeating sequences
            break

print(answer)