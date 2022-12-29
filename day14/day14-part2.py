with open('input.txt', 'r') as f:
  contents = f.read()

lines = contents.split('\n')

cavestart_x = 200 
cavestart_y = 0 
cavesize = 1000 

cave = [ ['.' for x in range(cavestart_x,cavestart_x + cavesize)] 
              for y in range(cavestart_y,cavestart_y + cavesize) ]

paths = [ [ (int(c.split(',')[0]),  int(c.split(',')[1])) 
              for c in line.split(' -> ') ] 
          for line in lines ] 

max_y = 0 

for path in paths: 
  for (x,y) in path: 
    max_y = max(max_y, y)

print("Max depth", max_y + 1)

def draw_cave(): 
  for ys in cave: 
    for x in ys: 
      print(x, end="")
    print()

def draw_line(start, end): 
  print("Drawing line:", start, end) 

  (xstart,ystart) = start
  (xend,yend) = end 

  assert xstart == xend  or  ystart == yend 

  if xstart != xend: 
    for x in range(min(xstart,xend), max(xstart,xend)+1): 
      cave[ystart - cavestart_y][x - cavestart_x] = '#'
  else: 
    for y in range(min(ystart,yend), max(ystart,yend)+1): 
      cave[y - cavestart_y][xstart - cavestart_x] = '#'

for path in paths: 
  for i in range(len(path) - 1): 
    draw_line(path[i], path[i+1])

cave[0 - cavestart_y][500 - cavestart_x] = '+'

# draw_cave()
  
def do_sand(x,y): 
  # print("do_sand:", (x,y))

  if ((y - cavestart_y) == (max_y + 1)): 
    return (x,y)

  if cave[(y + 1) - cavestart_y][x - cavestart_x] == '.': 
    # print("Down case")
    return do_sand(x, y + 1)
  elif cave[(y + 1) - cavestart_y][(x - 1) - cavestart_x] == '.': 
    # print("Left case")
    return do_sand(x - 1, y + 1)
  elif cave[(y + 1) - cavestart_y][(x + 1)- cavestart_x] == '.': 
    # print("Right case")
    return do_sand(x + 1, y + 1)
  else: 
    return (x,y) 

sand_count = 0 

while True:
  loc = do_sand(500,0)
  if not loc: 
    break 
  else: 
    if loc == (500,0): 
      break 
    else: 
      cave[loc[1] - cavestart_y][loc[0] - cavestart_x] = 'o'
      sand_count += 1

  # draw_cave() 

print("Answer:", sand_count + 1)