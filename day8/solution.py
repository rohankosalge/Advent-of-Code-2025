# We are asked to find the product of the lengths of the three largest circuits.
# A circuit is determined by a string of lights that are mutually closest to each other.

folder_path = '/Users/rohankosalge/Desktop/Coding/Advent-of-Code-2025/'
raw = open(folder_path + 'day8/data.txt', 'r').readlines()

boxes = [[int(coord) for coord in line.replace('\n', '').split(',')] for line in raw]

# straight-line distance
sld = lambda p1, p2: ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2) ** 0.5


# assign each coords to its own unique circuit.
# observe current coords p and its closest coords q
# if circuit(p) != circuit(q): join them.
# This procedure is reliant on the Disjoint Set (Union-Find).

# I used GPT for this class.
# No way I could build this from scratch... haha. Sorry 61B.
class DisjointSet:

    def __init__(self, n):
        self.circuit = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.circuit[x] != x:
            self.circuit[x] = self.find(self.circuit[x])
        return self.circuit[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return ra 
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.circuit[rb] = ra # merge circuits by incorporating the smaller into the larger.
        self.size[ra] += self.size[rb]
        return ra

    def size(self, x):
        return self.size[self.find(x)]
    
    def all_sizes(self):
        return [self.size[i] for i in range(len(self.circuit)) if self.circuit[i] == i]

    def max_size(self):
        return max(self.all_sizes())

circuits = DisjointSet(len(boxes))
pairings = []

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        pairings.append([i, j, sld(boxes[i], boxes[j])])

pairings = sorted(pairings, key=lambda x: x[-1], reverse=True)

for _ in range(1000):
    pairing = pairings.pop()
    circuits.union(pairing[0], pairing[1])

sizes = sorted(circuits.all_sizes(), reverse=True)
answer = sizes[0] * sizes[1] * sizes[2]
print(answer)

# Part 2 asks us to keep connecting boxes until they are all in the same circuit.
# And then, retrieve the product of the X coordinates of the last two boxes we connect.

while circuits.max_size() != len(boxes):
    pairing = pairings.pop()
    x0, x1 = boxes[pairing[0]][0], boxes[pairing[1]][0]
    circuits.union(pairing[0], pairing[1])

answer = x0 * x1
print(answer)



