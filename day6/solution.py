# We are asked to do some cephalopod math.
# Compute the math expressions column-wise, then sum up the total.

import numpy as np # for tranposing a matrix

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
raw = open(folder_path + 'day6/data.txt', 'r').readlines()

data = np.array([row.split() for row in raw]).T.tolist()

def prod(arr):
    res = int(arr[0])
    for num in arr[1:]:
        res *= int(num)
    return res 

answer = 0

for expression in data:
    if expression[-1] == '+':
        answer += sum([int(num) for num in expression[:-1]])
    else:
        answer += prod(expression[:-1])

#print(answer)

# Part 2 asks us to read the numbers by columns rather than by row, and re-compute the total sum.
# This part requires further pre-processing.

answer = 0

raw = open(folder_path + 'day6/data.txt', 'r').read()
lines = raw.split('\n')

# Since there's no tab tracking available, use the operators' indices as trackers for where to partition digits.
indices = [i for i in range(len(lines[-1])) if lines[-1][i] != ' ']

nums = [] # Compile array version of numbers w/ spaces.
for line in lines[:-1]:
    nums.append([])
    for i in range(len(indices) - 1):
        nums[-1].append(line[indices[i]: indices[i + 1] - 1])
    nums[-1].append(line[indices[-1]: ])

nums = np.array(nums).T.tolist()
ops = lines[-1].split()
data = [nums[i] + [ops[i]] for i in range(len(nums))]

for expression in data:

    nums = [list(num) for num in expression[:-1]]
    tabbed = np.array([['']*(len(max(nums,key=len)) - len(num)) + num for num in nums]).T.tolist()
    colwise_nums = [int(''.join(num)) for num in tabbed]

    if expression[-1] == '+':
        answer += sum(colwise_nums)
    else:
        answer += prod(colwise_nums)

print(answer)
