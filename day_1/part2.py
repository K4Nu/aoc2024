from collections import Counter

# Read and parse the input
left, right = [], []
with open("day1.txt") as file:
    for line in file:
        l, r = map(int, line.strip().split())
        left.append(l)
        right.append(r)

# Count occurrences in the right list
right_count = Counter(right)

# Calculate the similarity score
total = sum(num * right_count[num] for num in left)

print(total)
