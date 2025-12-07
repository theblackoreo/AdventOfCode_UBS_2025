matrix = []

with open("day4_data.txt") as f:
    for line in f:
        row = list(line.strip())  
        matrix.append(row)


total = 0
atLeastOneRemoved = True

while atLeastOneRemoved:
    atLeastOneRemoved = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            count = 0
            if matrix[i][j] == "@":
                if i < len(matrix)-1:
                    if matrix[i+1][j] == "@":
                        count += 1
                    if j < len(matrix[i])-1:
                        if matrix[i+1][j+1] == "@":
                            count += 1
                    if j > 0:
                        if matrix[i+1][j-1] == "@":
                            count += 1
                if i > 0:
                    if matrix[i-1][j] == "@":
                        count += 1
                    if j < len(matrix[i])-1:
                        if matrix[i-1][j+1] == "@":
                            count += 1
                    if j > 0:
                        if matrix[i-1][j-1] == "@":
                            count += 1
                if j > 0:
                    if matrix[i][j-1] == "@":
                        count += 1
                if j < len(matrix[i])-1:
                    if matrix[i][j+1] == "@":
                        count += 1

                if count < 4:
                    matrix[i][j] = "x"
                    total += 1
                    atLeastOneRemoved = True
        
print(total)

