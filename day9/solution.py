# We are asked to find the largest rectangle we can make between two red tiles.
# Red tiles are given as (x, y) coordinates.

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
raw = open(folder_path + 'day9/data.txt', 'r').readlines()

data = [[int(coord) for coord in coords.replace('\n', '').split(',')] for coords in raw]

area = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

answer = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        answer = max(answer, area(data[i], data[j]))

print(answer)

# Part 2 asks us to find the largest rectangle between two red tiles such that we only incorporate green tiles.
# Green tiles are in between adjacent red tiles.

answer = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):

        # Same structure.
        # We just need an extra condition to certify that the rectangle uses only red+green tiles.

        
        pass


