with open('input.txt', 'r') as f:
    contents = f.read()

# Split the file contents by newline characters
lines = contents.split('\n')
lines.pop(0) # drop 'cd /'

current_space = 70000000 - 42476859
space_needed = 30000000 - current_space 

answer = 70000000

def parse_dir(): 
  global answer 

  # print("Entering directory")
  lines.pop(0) # drop the 'ls' command 

  dir_size = 0 

  while lines != []: 
    cmd = lines.pop(0) 

    if cmd[0:3] == "dir": 
      pass 
      # print("Found dir:", cmd)
    elif cmd[0:8] == "$ cd ..":
      break
    elif cmd[0:4] == "$ cd":
      print("CD dir:", cmd)
      dir_size += parse_dir() 
    else:  
      # print("Found file:", cmd)
      dir_size += int(cmd.split()[0])

  print("Leaving directory. Size:", dir_size)

  if dir_size >= space_needed and dir_size < answer: 
    answer = dir_size 
  
  return dir_size 

parse_dir() 

print("Answer 1:", answer)
  

