with open('input.txt', 'r') as f:
    contents = f.read()

rope = [(5,10)] * 10 
visited = set() 

def print_state(rope): 
  grid_size = 25
  for i in range(grid_size): 
    for j in range(grid_size): 
      if ((grid_size - 1 - i, j) == rope[0]): 
        print("H", end="")
      else: 
        try: 
          r = rope.index((grid_size - 1 - i, j))
          print(r, end="")
        except ValueError: 
          print('.', end="")
    print("")
  print() 

def update_knot(h, t): 
  # print("Knot:", (h,t))
  if ( abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2):   
    # Nothing to do 
    return t 

  if h[0] == t[0]:  # Horizontal case 
    # print("Horizontal case")
    if h[1] > t[1]: 
      # print("Right")
      return (t[0], t[1] + 1)
    else: 
      # print("Left")
      return (t[0], t[1] - 1) 

  if h[1] == t[1]:  # Vertical case 
    # print("Vertical case")
    if h[0] > t[0]: 
      # print("Up")
      return (t[0] + 1, t[1])
    else: 
      # print("Down") 
      return (t[0] - 1, t[1])

  if h[0] > t[0]: # Diagonal case 
    if h[1] > t[1]: 
      return (t[0] + 1, t[1] + 1)
    else: 
      return (t[0] + 1, t[1] - 1)
  else: 
    if h[1] > t[1]: 
      return (t[0] - 1, t[1] + 1)
    else: 
      return (t[0] - 1, t[1] - 1)



  return(t) 

lines = contents.split('\n') 

print("Starting state:")
# print_state(rope) 
print() 

for line in lines: 
  cmd = line.split() 
  print("Move:", cmd)
  for _ in range(int(cmd[1])): 
    match cmd[0]: 
      case "U": 
        rope[0] = (rope[0][0] + 1, rope[0][1])
      case "D": 
        rope[0] = (rope[0][0] - 1, rope[0][1])
      case "R": 
        rope[0] = (rope[0][0], rope[0][1] + 1)
      case "L": 
        rope[0] = (rope[0][0], rope[0][1] - 1)

    for i in range(len(rope) - 1): 
      rope[i+1] = update_knot(rope[i], rope[i+1])
    visited.add(rope[-1])
     

  # print_state(rope) 


print("Number of locations visited:", len(visited))