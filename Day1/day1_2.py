

with open("day1_1_data.txt", "r") as f:
    rotations = [line.strip() for line in f]



starting_position = 50
count = 0
current_position = starting_position


for shift in rotations:

    print(shift)

    if shift[0] == "R":
        toAdd = int(shift[1:])
        
        for i in range(1, toAdd+1):
            if (current_position + i) % 100 == 0:
                count += 1
                
        current_position = (current_position + toAdd) % 100


    else:
        toSub = int(shift[1:])
        
        for i in range(1, toSub+1):
            if (current_position - i) % 100 == 0:
                count += 1
        current_position = (current_position - toSub) % 100


    

print(count)


