with open('input.txt', 'r') as f:
    s = f.read()

for i in range(len(s) - 3):
  substr = s[i:i+14]
  if len(set(substr)) == 14:
    print(substr, i + 14)
    break
