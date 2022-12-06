with open('Day 1/day1-input.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

# Part 1
elfos_suma = []
suma = 0
for entry in calories:
    if entry != '':
        suma += int(entry)
    elif entry == '':
        elfos_suma.append(suma)
        suma = 0
elfos_suma.append(suma)
print(max(elfos_suma))

# Part 2
elfos_suma.sort(reverse=True)
print(elfos_suma[0]+elfos_suma[1]+elfos_suma[2])



