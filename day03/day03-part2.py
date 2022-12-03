
def score_char(char): 
  if ('a' <= char <= 'z'): 
    return ord(char) - ord('a') + 1 
  else: 
    return (ord(char) - ord('A')) + 27

priority_sum = 0

# Open the file for reading
with open("input.txt", "r") as file:
    # Initialize a counter variable
    counter = 0 

    # Read the file line by line
    for line in file:
      line = line.strip()
      
      if counter % 3 == 0: 
        running_set = set(line)
      else: 
        running_set = running_set & set(line)
        if counter % 3 == 2:
          char = running_set.pop()
          priority_sum += score_char(char)

      print(running_set)
      # Increment the counter
      counter += 1

print(priority_sum)