# We are asked to find the number of total splits of the tachyon beam.
# This is determined by the number of times the beam (or a split of the beam) encounters a splitter (^).

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
raw = open(folder_path + 'day7/data.txt', 'r').readlines()

data = [list(line.replace('\n','')) for line in raw]

answer = 0

for i in range(len(data)):
    for j in range(len(data[0])):

        if data[i][j] in ['.', 'S']: continue # we're only observing splitters

        for k in range(i-1, -1, -1): # backtracking from the splitter
            if data[k][j] == 'S':
                answer += 1
                break
            if data[k][j] == '^': break

            # which means data[k][j] must be '.'
            if data[k][j-1] == '^' or data[k][j+1] == '^':
                answer += 1
                break

print(answer)

# Part 2 asks us to count all the different timelines (aka, unique ways that a beam from S can go all the way down).
# To do this, we can create a tree structure and count the number of unique root-to-leaf paths.

# Step 1: creating the tree (borrows from part 1)

tree = {}
splitters = []

for i in range(len(data)):
    for j in range(len(data[0])):

        if data[i][j] in ['.', 'S']: continue # we're only observing splitters

        splitters.append((i, j))
        for k in range(i-1, -1, -1): # backtracking from the splitter
            if data[k][j] == 'S':
                tree[(k, j)] = [(i,j)]
                break
            if data[k][j] == '^': break

            # which means data[k][j] must be '.'
            found_splitter = False

            if data[k][j-1] == '^':
                if (k, j-1) not in tree:
                    tree[(k, j-1)] = [(i,j)]
                else:
                    tree[(k, j-1)].append((i,j))
                found_splitter = True
            
            if data[k][j+1] == '^':
                if (k, j+1) not in tree:
                    tree[(k, j+1)] = [(i,j)]
                else:
                    tree[(k, j+1)].append((i,j))
                found_splitter = True

            #if found_splitter: break

root = (0, 70) 

for splitter in splitters:
    if splitter not in tree:
        tree[splitter] = (str(splitter)+'-L', str(splitter)+'-R')

for splitter in tree:
    if len(tree[splitter]) == 1 and splitter != root:
        tree[splitter].append(str(splitter) + '-P')


# I used ChatGPT to help with the memoization bit.
# But the intuition was self-driven. 
memo = {}

def count_paths(v):
    if v in memo:
        return memo[v]

    if v not in tree: 
        memo[v] = 1
        return 1
    
    total = sum(count_paths(w) for w in tree[v])
    memo[v] = total
    return total

answer = count_paths(root)
print(answer)