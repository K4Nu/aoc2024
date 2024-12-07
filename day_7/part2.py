from itertools import product

v = 0  # Total calibration result

with open("day7.txt") as f:
    for line in f:
        line = line.strip().replace(":", "").split()
        target = int(line[0])  # Target value
        values = list(map(int, line[1:]))  # Numbers
        signs = ("*", "+", "||")

        # Generate all combinations of operators
        combinations = list(product(signs, repeat=len(values) - 1))

        # Check all combinations
        for combination in combinations:
            temp = values.copy()
            v1 = temp.pop(0)  # Start with the first number

            # Apply each operator in the combination
            for s in combination:
                v2 = temp.pop(0)
                if s == "*":
                    v1 *= v2
                elif s == "+":
                    v1 += v2
                elif s == "||":
                    v1 = int(str(v1) + str(v2))

            # Check if the result matches the target
            if v1 == target:
                v += target
                break  # Stop processing further combinations for this target

print(v)  # Print the total calibration result
