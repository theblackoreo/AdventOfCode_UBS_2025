with open("day3_data.txt", "r") as f:
    banks = [line.strip() for line in f]

totalJoltage = 0

for bank in banks:
    
    pos = 0
    final = []
    i = 0

    for n in range(11,-1, -1):
        max = 0
        while i < len(bank)-n:
            if int(bank[i]) > max:
                max = int(bank[i])
                pos = i+1
            i += 1      
        i = pos
        final.append(bank[pos-1])
    
    totalJoltage += int(''.join(str(x) for x in final))


            




print(totalJoltage)



