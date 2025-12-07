with open("day3_data.txt", "r") as f:
    banks = [line.strip() for line in f]

totalJoltage = 0

for bank in banks:
    max = 0

    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):
            if int(bank[i] + bank[j]) > max:
                max = int(bank[i] + bank[j])
        
    totalJoltage += max


print(totalJoltage)



