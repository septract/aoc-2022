with open('input.txt', 'r') as f:
  contents = f.read()

maxdist = 999999

lines = contents.split('\n') 
heights = [[ord(ch) for ch in line] for line in lines]

for i in range(len(heights)):
  for j in range(len(heights[0])): 
    if heights[i][j] == ord('S'): 
      heights[i][j] = ord('a')
      start = (i,j)
    if heights[i][j] == ord('E'): 
      heights[i][j] = ord('z')
      end = (i,j)

print("Start:", start)
print("End:", end) 

print("Heights:")
for h in heights: 
  print(h) 


route = [ [ maxdist for y in range(len(heights[0]))]
            for x in range(len(heights)) ] 

route[end[0]][end[1]] = 0 

def print_route(): 
  for r in route: 
    print(r) 

print_route() 

stack = [end] 

def try_update(x,y,oldheight,newdist): 
  if (x >= 0 and 
      x < len(route) and
      y >= 0 and
      y < len(route[0]) and 
      oldheight - heights[x][y] <= 1 and 
      route[x][y] > newdist): 
    route[x][y] = newdist
    stack.append((x,y))

while stack != []: 
  (xn,yn) = stack.pop() 
  h = heights[xn][yn] 
  newdist = route[xn][yn] + 1
  
  try_update(xn+1,yn,h,newdist)
  try_update(xn-1,yn,h,newdist)
  try_update(xn,yn+1,h,newdist)
  try_update(xn,yn-1,h,newdist)

  # print_route() 

print_route() 
# print("Answer:", route[start[0]][start[1]])

mindist = maxdist

for x, ys in enumerate(heights): 
  for y, h in enumerate(ys): 
    if h == ord('a'): 
      mindist = min(mindist, route[x][y])

print("Answer:", mindist)