import ast

with open('input.txt', 'r') as f:
  contents = f.read()

lines = contents.split('\n')

pairs =  [( ast.literal_eval(lines[i]),  
            ast.literal_eval(lines[i+1]) ) 
                for i in range(0, len(lines), 3)]
print(pairs)

def compare_value(v0, v1): 
  print("comparing:", v0, v1)

  if v0 == v1: 
    return 0 
  elif isinstance(v0, int) and isinstance(v1,int): 
    if v0 < v1: 
      return -1 
    else: 
      return 1
  elif isinstance(v0, int) and isinstance(v1,list): 
    return compare_value([v0], v1) 
  elif isinstance(v0, list) and isinstance(v1,int): 
    return compare_value(v0, [v1])
  elif v0 == []: 
    return -1 
  elif v1 == []: 
    return 1
  else: 
    first = compare_value(v0[0],v1[0])
    if first == 0: 
      return compare_value(v0[1:], v1[1:])
    else: 
      return first 

index_sum = 0 

for i,p in enumerate(pairs): 
  print("Pair:", p)
  comp = compare_value(p[0],p[1])
  if comp == -1: 
    print("Correct order")
    index_sum += (i + 1) 
  else: 
    print("Wrong order")
  print()

print("Answer:", index_sum)