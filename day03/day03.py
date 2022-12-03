priority_sum = 0

# Open the file in read mode
with open('input.txt', 'r') as f:
    # Iterate over the lines in the file
    for line in f:
        # Strip the line of any leading or trailing whitespace
        line = line.strip()

        # Calculate the index at which to split the string
        index = len(line) // 2
        
        # Use slicing to extract the two substrings
        substring1 = line[:index]
        substring2 = line[index:]

        # print(substring1, substring2)
        
        set1 = set(substring1)
        set2 = set(substring2)

        # print(set1, set2)

        # Use the intersection operator to find the overlapping characters
        overlapping_chars = set1 & set2

        # print(overlapping_chars)

        char = overlapping_chars.pop()

        if ('a' <= char <= 'z'): 
          char_val = ord(char) - ord('a') + 1 
        else: 
          char_val = (ord(char) - ord('A')) + 27

        priority_sum = priority_sum + char_val

        # print(char_val)

        # print(priority_sum)


print(priority_sum)