with open('input.txt', 'r') as f:
  contents = f.read()

lines = contents.split('\n') 

regx = 1 
cycle = 1 
sigstren = 0 

loglist = [20, 60, 100, 140, 180, 220]

for i,line in enumerate(lines): 
  cmd = line.split() 
  print("Command:", cmd)
  print("Next cycle:", cycle)

  match cmd[0]: 
    case "noop": 
      cycle += 1 
    case "addx": 
      cycle += 2

  if loglist != [] and loglist[0] + 1 <= cycle: 
    logcyc = loglist.pop(0)
    print(logcyc) 
    print(regx) 
    print("Updated sigstren:", logcyc * regx)
    sigstren += logcyc * regx

  match cmd[0]: 
    case "addx": 
      regx += int(cmd[1]) 
    case _: 
      pass 


  print("Cycle:", cycle, ", regx:", regx)

print("Signal strength", sigstren)