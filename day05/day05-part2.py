import re 

with open('input.txt', 'r') as f:
    contents = f.read()

# Split the file contents by newline characters
lines = contents.split('\n')

i = 0 

crates = []
num_piles = 0  
moves = []

while i < len(lines) and lines[i][1] != '1': 
  chunks = [] 
  chunk_size = 4 
  for j in range(0,len(lines[i]), chunk_size): 
    chunks.append(lines[i][j:j+chunk_size]) 
  crates.append(chunks)
  i += 1

num_piles = int(lines[i].split()[-1])

for k in range(i+2, len(lines)): 
  numbers = re.findall(r"\d+", lines[k])
  moves.append(tuple([int(n) for n in numbers]))

# print(crates)
# print(num_piles)

piles = [[] for _ in range(num_piles)] 

for cratelist in crates: 
  for i in range(num_piles): 
    if cratelist[i][0] == '[':
      piles[i].insert(0,cratelist[i][1])

print("Initial configuration: ", piles)
# print(moves)

for (num, source, target) in moves: 
  tmp = [] 
  for n in range(num): 
    tmp.append(piles[source - 1].pop()) 

  for n in range(num): 
    piles[target - 1].append(tmp.pop())

  print(piles)

answer = [] 
for p in piles: 
  answer.append(p[-1])

print("Answer 2: ", answer)


