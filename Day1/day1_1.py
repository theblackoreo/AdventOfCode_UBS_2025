

with open("day1_1_data.txt", "r") as f:
    rotations = [line.strip() for line in f]



starting_position = 50
count = 0
current_position = starting_position


for shift in rotations:

    print(shift)

    if shift[0] == "R":
        toAdd = int(shift[1:])
        
        current_position = (current_position + toAdd) % 100

    else:
        toSub = int(shift[1:])

        current_position = (current_position - toSub) % 100

    
    if current_position == 0:
        count += 1


print(count)


