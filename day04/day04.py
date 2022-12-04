# Open the file and read its contents
with open('input.txt', 'r') as f:
    contents = f.read()

# Split the file contents by newline characters
lines = contents.split('\n')

# Create an empty list to store the tuples
tuples = []

# Iterate over the lines in the file
for line in lines:
    # Split each line by the comma character
    fields = line.split(',')

    # Create a list to store the four-tuple
    four_tuple = []

    # Iterate over the fields in the line
    for field in fields:
        # Split each field by the dash character and convert the resulting fields to integers
        # Add the resulting tuple to the four-tuple list
        four_tuple.append(tuple(int(f) for f in field.split('-')))

    # Add the four-tuple to the list of tuples
    tuples.append(four_tuple)

# Create a counter variable to count the number of tuples where the intervals overlap
counter = 0

# Iterate over the tuples in the list
for (a, b), (c, d) in tuples:
    # Check if the intervals overlap
    if b >= c and a <= d:
        counter += 1

# Print the counter variable
print(f'The number of tuples where the intervals overlap is {counter}')
