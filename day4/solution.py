# We are asked to find the total number of accessible paper rolls.
# A paper roll is accessible if there are less than 4 adjacent rolls.

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
raw = open(folder_path + 'day4/data.txt', 'r').readlines()

data = [list(line.replace('\n','')) for line in raw] # 136 x 136 = 18496 positions
n = 136

answer = 0

dirs = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
for i in range(n):
    for j in range(n):
        if data[i][j] != '@': continue
        adj_rolls = 0
        for dir_ in dirs:
            adj_x, adj_y = i + dir_[0], j + dir_[1]
            if adj_x < 0 or adj_x >= n or adj_y < 0 or adj_y >= n: continue
            if data[adj_x][adj_y] == '@': adj_rolls += 1
        if adj_rolls < 4:
            answer += 1

print(answer)


# Part 2 asks us to find the maximum number of paper rolls that can be removed.
# A proposed strategy is to repeatedly locate accessible paper rolls and remove them, until there are no more accessible paper rolls.

answer = 0
num_access_rolls = None

while num_access_rolls != 0:

    num_access_rolls = 0
    access_rolls = []
    for i in range(n):
        for j in range(n):
            if data[i][j] != '@': continue
            adj_rolls = 0
            for dir_ in dirs:
                adj_x, adj_y = i + dir_[0], j + dir_[1]
                if adj_x < 0 or adj_x >= n or adj_y < 0 or adj_y >= n: continue
                if data[adj_x][adj_y] == '@': adj_rolls += 1
            if adj_rolls < 4:
                num_access_rolls += 1
                access_rolls.append([i,j])
    
    # Once we access a roll, remove it.
    for access_roll in access_rolls:
        data[access_roll[0]][access_roll[1]] = '.'
    
    answer += num_access_rolls

print(answer)