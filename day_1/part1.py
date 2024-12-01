left, right = [], []

# Read input and populate the lists
with open("day1.txt") as file:
    for line in file:
        l, r = map(int, line.strip().split())
        left.append(l)
        right.append(r)

# Sort both lists
left = sorted(left)
right = sorted(right)

# Calculate the total distance
total = sum(abs(l - r) for l, r in zip(left, right))

# Print the result
print(total)
