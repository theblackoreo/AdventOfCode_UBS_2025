matrix = []

with open("day6_data.txt", "r") as f:
    for line in f:
        matrix.append(line.strip())

operators = []
for i, char in enumerate(matrix[-1]):
    if char in ['+', '*']:
        operators.append((char, i))

total = 0

for op_idx in range(len(operators)):
    operator, start_idx = operators[op_idx]
    
    if op_idx + 1 < len(operators):
        end_idx = operators[op_idx + 1][1] - 2
    else:
        end_idx = max(len(row) - 1 for row in matrix[:-1])
    
    numbers = []
    for col_idx in range(start_idx, end_idx + 1):
        num_str = ""
        for row_idx in range(len(matrix) - 1):
            if col_idx < len(matrix[row_idx]) and matrix[row_idx][col_idx].isdigit():
                num_str += matrix[row_idx][col_idx]
        
        if num_str:
            numbers.append(int(num_str))
    
    part_res = 0 if operator == '+' else 1
    for num in numbers:
        if operator == '+':
            part_res += num
        elif operator == '*':
            part_res *= num
    
    total += part_res

print(total)