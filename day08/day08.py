with open('input.txt', 'r') as f:
    contents = f.read()

lines = contents.split() 
trees = [] 

def print_trees() : 
  for t in trees: 
    print(t) 

for line in lines: 
  trees.append([])
  for char in line: 
    trees[-1].append((int(char), False))

# print(trees)

for i in range(len(trees)): 
  lmax = rmax = -1 
  for j in range(len(trees[0])): 
    # print("\nAddress:", i, j)

    # Left 
    if trees[i][j][0] > lmax: 
      lmax = trees[i][j][0]
      trees[i][j] = (trees[i][j][0], True) 

    # Right 
    if trees[i][-j - 1][0] > rmax: 
      rmax = trees[i][-j - 1][0]
      trees[i][-j - 1] = (trees[i][-j - 1][0], True) 

# print("Horizontal result:")
# print_trees()

for j in range(len(trees[0])): 
  lmax = rmax = -1 
  for i in range(len(trees)): 
    # print("\nAddress:", i, j)

    if trees[i][j][0] > lmax: 
      lmax = trees[i][j][0]
      trees[i][j] = (trees[i][j][0], True) 

    ri = -i -1
    if trees[ri][j][0] > rmax: 
      rmax = trees[ri][j][0]
      trees[ri][j] = (trees[ri][j][0], True) 

    # print_trees() 

# print("\nVertical result:")
# print_trees() 

answer1 = 0 
for i in range(len(trees)): 
  for j in range(len(trees[0])): 
    if trees[i][j][1]: 
      answer1 += 1

print("Answer 1:", answer1)
  