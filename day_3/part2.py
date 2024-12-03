import re

value = 0
flag = True  # At the start, mul instructions are enabled

with open("day3.txt") as file:
    for line in file:
        line = line.strip()

        # Combine all patterns into one with labels for processing order
        combined_pattern = re.compile(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))")
        for match in combined_pattern.finditer(line):
            if match.group(1):
                if flag:
                    curr = match.group(1)
                    x = curr[curr.index("(") + 1:curr.index(")")].strip()
                    a, b = map(int, x.split(","))
                    value += a * b
            elif match.group(2):
                flag = True
            elif match.group(3):
                flag = False
print(value)