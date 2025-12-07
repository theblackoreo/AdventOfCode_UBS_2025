total = 0

with open("day2_data.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        
        for ran in parts:
            start, end = map(int, ran.split("-"))

            for id in range(start, end + 1):
                s = str(id)
                n = len(s)

                for size in range(1, n // 2 + 1):
                    if n % size != 0:
                        continue
                    pattern = s[:size]
                    if pattern * (n // size) == s:
                        total += id
                        break 

print(total)
