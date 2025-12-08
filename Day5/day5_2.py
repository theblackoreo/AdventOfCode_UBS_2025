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

ranges.sort(key=lambda x: (x[0], x[1]))

merged = []

if ranges:  
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

total = 0
for s, e in merged:
    total += e - s +1   

print(total)
