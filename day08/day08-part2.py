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
    trees[-1].append((int(char), 0))

print_trees() 

def viewing_distance(x,y): 
  curr_tree = trees[x][y][0]
  print("Current tree:", curr_tree)

  # Up
  updist = 0 
  for i in range(x-1, -1, -1): 
    updist += 1 
    if trees[i][y][0] >= curr_tree: 
      break 
  print("Up distance:", updist)

  # Left
  leftdist = 0 
  for j in range(y-1, -1, -1): 
    leftdist += 1 
    if trees[x][j][0] >= curr_tree: 
      break 
  print("Left distance:", leftdist)

  # Right
  rightdist = 0 
  for j in range(y+1,len(trees[0])): 
    rightdist += 1 
    if trees[x][j][0] >= curr_tree: 
      break 
  print("Right distance:", rightdist)

  # Down
  downdist = 0 
  for i in range(x+1,len(trees)): 
    downdist += 1 
    if trees[i][y][0] >= curr_tree: 
      break 
  print("Down distance:", downdist)

  score = updist * downdist * leftdist * rightdist
  print("Score:", score)
  return score

viewing_distance(1,2)
  
answer2 = 0 

for i in range(len(trees)):
  for j in range(len(trees[0])): 
    answer2 = max(viewing_distance(i,j), answer2) 

print(answer2)
