arr = []
value = 0

# Read the input file
with open("day4.txt") as file:
    for line in file:
        line = line.strip()
        arr.append(line)


DIRECTIONS = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
    (-1, -1), (1, 1),     (-1, 1), (1, -1)
]


def find_xmas(arr, i, j):
    count = 0
    for dx, dy in DIRECTIONS:
        found = True
        word = "XMAS"
        for k in range(len(word)):
            ni, nj = i + dx * k, j + dy * k
            if not (0 <= ni < len(arr) and 0 <= nj < len(arr[0]) and arr[ni][nj] == word[k]):
                found = False
                break
        if found:
            count += 1
    return count


for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == "X":
            value += find_xmas(arr, i, j)

print("Total XMAS found:", value)
