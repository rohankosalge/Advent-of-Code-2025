# We are asked to find the total number of "fresh" IDs.
# An ID is "fresh" if it falls into at least one of the available ranges in the data.

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
raw = open(folder_path + 'day5/data.txt', 'r').readlines()

split_index = raw.index('\n')

ranges, ids = raw[:split_index], raw[split_index+1:]

all_bounds = []
for arange in ranges:
    bounds = arange.strip().split('-') 
    all_bounds.append([int(bounds[0]), int(bounds[1])])

answer = 0

for id_str in ids:
    id = int(id_str.strip())

    is_fresh = False
    for bound in all_bounds:
        if bound[0] <= id <= bound[1]:
            is_fresh = True
            break
    
    if is_fresh:
        answer += 1

print(answer)

# Part 2 asks us to find the total number of fresh IDs based on the given ranges.

answer = 0

# prev_bounds = []

# print(ranges[:5])
# for arange in ranges[:5]:
#     lower, upper = [int(bound) for bound in arange.strip().split('-')]

#     for bound in prev_bounds:
#         if bound[0] <= lower <= bound[1]:
#             lower = bound[1] + 1
#         if bound[0] <= upper <= bound[1]:
#             upper = bound[0] - 1
    
#     print(upper - lower + 1)
#     answer += (upper - lower + 1)
#     prev_bounds.append([lower, upper])

# print(answer)


answer = 0
lower_bounds, upper_bounds = [], []

for arange in ranges:
    lower, upper = [int(bound) for bound in arange.strip().split('-')]
    lower_bounds.append(lower)
    upper_bounds.append(upper)

lower_bounds.sort()
upper_bounds.sort()

print(lower_bounds)
print(upper_bounds)