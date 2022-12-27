import math 

with open('input.txt', 'r') as f:
  contents = f.read()

lines = contents.split('\n') 

groups = [lines[i:i+7] for i in range(0, len(lines), 7)]

num_monkeys = len(groups)

# Monkey data 
items_basic = [[]] * num_monkeys
ops = [[]] * num_monkeys
divby = [[]] * num_monkeys
next_t = [[]] * num_monkeys
next_f = [[]] * num_monkeys

# Results: 
inspections = [0] * num_monkeys

# Parse the data 
for (i, g) in enumerate(groups): 
  items_basic[i] = [int(x) for x in g[1][18:].split(", ")]
  ops[i] = (g[2][23], g[2][25:])
  divby[i] = int(g[3][21:])
  next_t[i] = int(g[4][29:])
  next_f[i] = int(g[5][30:])

def print_monkeys(): 
  for i in range(num_monkeys): 
    print("Items:", items_basic[i])
    print("Ops:", ops[i])
    print("Divby:", divby[i])
    print("NextT:", next_t[i])
    print("NextF:", next_f[i])
    print()

def make_item(x): 
  return [x % divby[i] for i in range(num_monkeys)]

items_enc = [ [make_item(i) for i in ib]
                    for ib in items_basic ]

print("Inital state:")
print_monkeys() 

def do_op(monkey, item): 
  match ops[monkey][0]: 
    case "*": 
      if ops[monkey][1] == "old": 
        return [ (item[i] * item[i]) % divby[i] 
                  for i in range(num_monkeys) ] 
      else: 
        return [ (item[i] * int(ops[monkey][1])) % divby[i] 
                  for i in range(num_monkeys) ] 
    case "+": 
      return [ (item[i] + int(ops[monkey][1])) % divby[i] 
                for i in range(num_monkeys) ]

def do_item(monkey, item): 
  inspections[monkey] += 1

  print("do_item", item) 
  
  item_new = do_op(monkey, item) 
  print("Result of do_op():", item_new)

  print("Testing if", item_new, "divisable by", divby[monkey])
  if item_new[monkey] == 0: 
    print("True")
    items_enc[next_t[monkey]].append(item_new)
    print("Threw to:", next_t[monkey]) 
  else: 
    print("False")
    items_enc[next_f[monkey]].append(item_new) 
    print("Threw to:", next_f[monkey]) 

def do_monkey(monkey): 
  print("\ndo_monkey", monkey)
  items_old = items_enc[monkey] 
  items_enc[monkey] = [] 
  for item in items_old: 
    do_item(monkey, item) 

def do_round(): 
  print("do_round") 
  for i in range(num_monkeys): 
    do_monkey(i)

for i in range(10000): 
  do_round() 

print("Inspection counts:", inspections)
print("Answer:", sorted(inspections)[-1] * sorted(inspections)[-2])