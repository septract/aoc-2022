import math 

with open('input.txt', 'r') as f:
  contents = f.read()

lines = contents.split('\n') 

groups = [lines[i:i+7] for i in range(0, len(lines), 7)]

num_monkeys = len(groups)

# Monkey data 
items = [[]] * num_monkeys
ops = [[]] * num_monkeys
divby = [[]] * num_monkeys
next_t = [[]] * num_monkeys
next_f = [[]] * num_monkeys

# Results: 
inspections = [0] * num_monkeys

# Parse the data 
for (i, g) in enumerate(groups): 
  items[i] = [int(x) for x in g[1][18:].split(", ")]
  ops[i] = (g[2][23], g[2][25:])
  divby[i] = int(g[3][21:])
  next_t[i] = int(g[4][29:])
  next_f[i] = int(g[5][30:])

def print_monkeys(): 
  for i in range(num_monkeys): 
    print("Items:", items[i])
    print("Ops:", ops[i])
    print("Divby:", divby[i])
    print("NextT:", next_t[i])
    print("NextF:", next_f[i])
    print()

def print_items(): 
  for i in range(num_monkeys): 
    print("Monkey:", i, ":", items[i])

print("Inital state:")
print_monkeys() 

def do_op(monkey, item): 
  if ops[monkey][1] == "old": 
    quant = item 
  else: 
    quant = int(ops[monkey][1])

  match ops[monkey][0]: 
    case "*": 
      return item * quant 
    case "+": 
      return item + quant 

def do_item(monkey, item): 
  inspections[monkey] += 1

  print("do_item", item) 
  
  item_new = do_op(monkey, item) 
  print("Result of do_op():", item_new)

  item_new = math.floor(item_new / 3)  
  print("Result of div:", item_new)

  print("Testing if", item_new, "divisable by", divby[monkey])
  if item_new % divby[monkey] == 0: 
    print("True")
    items[next_t[monkey]].append(item_new)
    print("Threw to:", next_t[monkey]) 
  else: 
    print("False")
    items[next_f[monkey]].append(item_new) 
    print("Threw to:", next_f[monkey]) 

def do_monkey(monkey): 
  print("do_monkey", monkey)
  items_old = items[monkey] 
  items[monkey] = [] 
  for item in items_old: 
    do_item(monkey, item) 

def do_round(): 
  print("do_round", round) 
  for i in range(num_monkeys): 
    do_monkey(i)

for i in range(20): 
  do_round() 

print_items() 

print("Inspection counts:", inspections)
print("Answer:", sorted(inspections)[-1] * sorted(inspections)[-2])