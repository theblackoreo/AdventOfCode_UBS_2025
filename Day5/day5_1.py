
ranges = []

ids = []

with open("day5_data.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue   
        if "-" in line:
            start, end = map(int, line.replace(" ", "").split("-"))
            ranges.append((start, end))
        else:
            ids.append(int(line))

completed_ranges = []
count = 0

for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1] and id not in completed_ranges:
            count += 1
            completed_ranges.append(id)

print(count)