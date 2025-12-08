matrix = []

with open("day6_data.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        matrix.append(line)

total = 0

for c in range(len(matrix[0])):
    operator = matrix[-1][c]
    part_res = 0 if operator == "+" else 1

    for r in range(len(matrix) - 1):
        value = int(matrix[r][c])    

        if operator == "+":
            part_res += value
        elif operator == "*":
            part_res *= value

    total += part_res

print(total)
