with open('input.txt', 'r') as f:
    contents = f.read()

visited = set() 

def print_state(h,t): 
  grid_size = 6
  for i in range(grid_size): 
    for j in range(grid_size): 
      if ((grid_size - 1 - i, j) == h): 
        print("H", end="")
      elif ((grid_size - 1 - i, j) == t): 
        print("T", end="")
      else: 
        print('.', end="") 
    print("")
  print() 

def move_up(h,t,i): 
  print("Moving up", i)

  for n in range(i): 
    h = ( h[0] + 1, h[1] )
    print_state(h,t)
    if abs(h[0] - t[0]) > 1: 
      t = (h[0] - 1, h[1])
      print_state(h,t)
    visited.add(t) 
  
  return (h,t)


def move_down(h,t,i): 
  print("Moving down", i)

  for n in range(i): 
    h = ( h[0] - 1, h[1] )
    print_state(h,t)
    if abs(h[0] - t[0]) > 1: 
      t = (h[0] + 1, h[1])
      print_state(h,t)
    visited.add(t) 
  
  return (h,t)

def move_right(h,t,i): 
  print("Moving right", i)

  for n in range(i): 
    h = ( h[0], h[1] + 1)
    print_state(h,t)
    if abs(h[1] - t[1]) > 1: 
      t = (h[0], h[1] - 1)
      print_state(h,t)
    visited.add(t) 
  
  return (h,t)

def move_left(h,t,i): 
  print("Moving left", i)

  for n in range(i): 
    h = ( h[0], h[1] - 1)
    print_state(h,t)
    if abs(h[1] - t[1]) > 1: 
      t = (h[0], h[1] + 1)
      print_state(h,t)
    visited.add(t)
  
  return (h,t)

lines = contents.split('\n') 

head = (0,0)
tail = (0,0)

print_state(head,tail) 
print() 

for line in lines: 
  cmd = line.split() 
  print(cmd)
  match cmd[0]: 
    case "U": 
      (head,tail) = move_up(head, tail, int(cmd[1])) 
    case "D": 
      (head,tail) = move_down(head, tail, int(cmd[1])) 
    case "R": 
      (head,tail) = move_right(head, tail, int(cmd[1])) 
    case "L": 
      (head,tail) = move_left(head, tail, int(cmd[1])) 

print(len(visited))