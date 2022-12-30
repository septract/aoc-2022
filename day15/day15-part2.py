with open('input.txt', 'r') as f:
  contents = f.read()

lines = contents.split('\n')

def strip_to_int(str):
  return int("".join([c for c in str if (c.isdigit() or c == '-')]))

coords = [] 

for line in lines: 
  chunks = line.split()
  new = ( strip_to_int(chunks[2]), 
          strip_to_int(chunks[3]), 
          strip_to_int(chunks[8]),
          strip_to_int(chunks[9]) )
  coords.append(new) 

# print("Coordinates:", coords)

dists = [] 
maxdist = 0 

def manhattan(x1,y1,x2,y2): 
  return abs(x1-x2) + abs(y1-y2)

for c in coords: 
  (sx,sy,bx,by) = c 

  d = manhattan(sx,sy,bx,by)
  dists.append(d) 
  maxdist = max(maxdist, d)

# print("Beacon distances:", dists) 
# print("Max distance:", maxdist)

def sensor_ring(x,y,d): 
  return  [(x+i,y+(d-i)) for i in range(d+1)] + \
          [(x-i,y+(d-i)) for i in range(d+1)] + \
          [(x+i,y-(d-i)) for i in range(d+1)] + \
          [(x-i,y-(d-i)) for i in range(d+1)] 

def covered(t): 
  (tx,ty) = t 
  for i, c in enumerate(coords): 
    (sx,sy,_,_) = c 
    if manhattan(tx,ty,sx,sy) <= dists[i]: 
      return True
  return False 

covermax = 4000000 

for i, c in enumerate(coords): 
  (sx,sy,_,_) = c 
  test_locations = sensor_ring(sx,sy, dists[i]+1)

  for t in test_locations: 
    (tx,ty) = t
    if ((0 <= tx <= covermax) 
        and (0 <= ty <= covermax) 
        and not covered(t)): 
      print("Uncovered location:", t)
      print("Answer:", (tx * 4000000) + ty)
      quit() 