import heapq

# Open the file
with open('input.txt', 'r') as f:
    # Initialize the list of numbers
    numbers = [[]]

    # Iterate over the lines in the file
    for line in f:
        # Strip leading and trailing whitespace from the line
        line = line.strip()

        # If the line is empty, start a new group of numbers
        if not line:
            numbers.append([])
            continue

        # Otherwise, convert the line to a number and add it to the current group of numbers
        numbers[-1].append(int(line))

# Use the map function to apply the sum function to each group of numbers
sums = map(sum, numbers)

# Convert the iterator to a list
sums = list(sums)

# Find the 3 largest elements in the list of sums
largest_sums = heapq.nlargest(3, sums)

# Add up the 3 largest sums
total_sum = sum(largest_sums)

# Print the total sum
print("The total sum of the 3 largest sums is:", total_sum)
