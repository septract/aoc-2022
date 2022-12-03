def calculate_total(strategy_guide):
  total = 0

  for round in range(len(strategy_guide)):
    opponent_move = strategy_guide[round][0]
    your_move = strategy_guide[round][2]

    if (your_move == "X"): # Lose
      if (opponent_move == "A"): 
        decision = "Z"
      elif (opponent_move == "B"): 
        decision = "X"
      elif (opponent_move == "C"): 
        decision = "Y"

    elif (your_move == "Y"): # Draw
      if (opponent_move == "A"): 
        decision = "X"
      elif (opponent_move == "B"): 
        decision = "Y"
      elif (opponent_move == "C"): 
        decision = "Z"

    elif (your_move == "Z"): # Win 
      if (opponent_move == "A"): 
        decision = "Y"
      elif (opponent_move == "B"): 
        decision = "Z"
      elif (opponent_move == "C"): 
        decision = "X"

    total = total + calculate_score(opponent_move, decision)

  return total

def calculate_score(opponent_move, your_move):
  score = 0 

  if (your_move == "X"):
    score = score + 1
  elif (your_move == "Y"): 
    score = score + 2
  elif (your_move == "Z"): 
    score = score + 3

  if ( (opponent_move == "A" and your_move == "X") or
        (opponent_move == "B" and your_move == "Y") or
        (opponent_move == "C" and your_move == "Z") ):
    score = score + 3
  else:
    if ( (opponent_move == "A" and your_move == "Y") or
          (opponent_move == "B" and your_move == "Z") or
          (opponent_move == "C" and your_move == "X") ):
      score = score + 6
    else:
      score = score + 0

  return score

# Open the file and read the strategy guide
with open("input.txt") as file:
  strategy_guide = file.readlines()

# Remove the newline character from each line of the strategy guide
strategy_guide = [line.strip() for line in strategy_guide]

# Calculate the total score
score = calculate_total(strategy_guide)
print(score)  # 15
