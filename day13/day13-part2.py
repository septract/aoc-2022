import ast
import functools

with open('input.txt', 'r') as f:
  contents = f.read()

lines = contents.split('\n')

vals = [ ast.literal_eval(line) 
          for line in lines 
          if line.strip() != ""]

vals += [[[2]], [[6]]]

print(vals)

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

vals_sorted = sorted(vals, key=functools.cmp_to_key(compare_value))

answer = 1 

for i, v in enumerate(vals_sorted): 
  print(v) 

  if v == [[2]]  or  v == [[6]]: 
    answer *= (i + 1)

print("Answer:", answer)
