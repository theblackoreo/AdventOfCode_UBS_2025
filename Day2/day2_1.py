total = 0

with open("day2_data.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        
        for ran in parts:
            start, end = map(int, ran.split("-"))

            for id in range(start, end + 1):
                id_str = str(id)
                if len(id_str) % 2 == 0:
                    
                    middle = int(len(id_str)/2)
                    m = 0
                    while m < len(id_str)/2:
                        if id_str[m] != id_str[middle]:
                            break
                        m += 1
                        middle += 1
                    else:
                        total += id


print(total)