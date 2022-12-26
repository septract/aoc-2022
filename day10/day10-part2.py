with open('input.txt', 'r') as f:
  contents = f.read()

lines = contents.split('\n') 

def print_sprite(n): 
  for i in range(40): 
    if i-1 <= n % 40 <= i+1: 
      print("#", end="")
    else: 
      print(".", end="")

def draw_pixel(cyc,reg): 
  if reg-1 <= cyc % 40 <= reg+1: 
    return "#"
  else: 
    return "."

pixels = ""
start_cycle = 1
regx = 1 


for line in lines: 
  # print("Cycle:", start_cycle, ", Regx:", regx)
  # print("Sprite position:")
  # print_sprite(start_cycle)
  # print()

  cmd = line.split() 

  pixels = pixels + draw_pixel(start_cycle-1,regx)

  match cmd[0]: 
    case "noop": 
      start_cycle += 1 
    case "addx": 
      pixels = pixels + draw_pixel(start_cycle,regx)
      regx += int(cmd[1]) 
      start_cycle += 2
  
split = [pixels[i:i+40] for i in range(0, len(pixels), 40)]
for s in split: 
  print(s) 





#   if loglist != [] and loglist[0] + 1 <= cycle: 
#     logcyc = loglist.pop(0)
#     print(logcyc) 
#     print(regx) 
#     print("Updated sigstren:", logcyc * regx)
#     sigstren += logcyc * regx

#   match cmd[0]: 
#     case "addx": 
#       regx += int(cmd[1]) 
#     case _: 
#       pass 

#   print("Cycle:", cycle, ", regx:", regx)
