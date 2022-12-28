with open('test.txt', 'r') as f:
  contents = f.read()

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


route = [ [ 999999 for y in range(len(heights[0]))]
            for x in range(len(heights)) ] 

route[start[0]][start[1]] = 0 

def print_route(): 
  for r in route: 
    print(r) 

print_route() 

stack = [start] 

def try_update(x,y,oldheight,newdist): 
  if (x >= 0 and 
      x < len(route) and
      y >= 0 and
      y < len(route[0]) and 
      heights[x][y] - oldheight <= 1 and 
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

print("Answer:", route[end[0]][end[1]])

