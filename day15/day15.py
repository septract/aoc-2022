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

print("Coordinates:", coords)

dists = [] 
maxdist = 0 

def manhattan(x1,y1,x2,y2): 
  return abs(x1-x2) + abs(y1-y2)

for c in coords: 
  (sx,sy,bx,by) = c 

  d = manhattan(sx,sy,bx,by)
  dists.append(d) 
  maxdist = max(maxdist, d)

print("Beacon distances:", dists) 
print("Max distance:", maxdist)

minx = maxx = coords[0][1]

for c in coords: 
  minx = min(minx,c[0])
  maxx = max(maxx,c[0])

print("Min/max y:", minx, maxx)

def is_beacon(x,y): 
  for c in coords: 
    (_, _, bx, by) = c 
    if (x,y) == (bx,by): 
      return True 
  return False 

yrow = 2000000  # NOTE: different between test.txt / input.txt
covered = 0 

for x in range( minx - maxdist, maxx + maxdist ): 
  for i,c in enumerate(coords): 
    (sx,sy,_,_) = c 
    if (not is_beacon(x,yrow) and 
        manhattan(x,yrow,sx,sy) <= dists[i]): 
      covered += 1 
      break

print("Answer:", covered)
