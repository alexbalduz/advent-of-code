with open('Day 2/day2-input.txt') as file:
    rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]

#print(rounds)

salidas =  {
    "AX":4, "AY":8, "AZ":3,
    "BX":1, "BY":5, "BZ":9,
    "CX":7, "CY":2, "CZ":6
}

puntaje_total = 0
for round in rounds:
    puntaje_total += salidas[round]

print(puntaje_total)

salidas_deseadas = {
    "AX":3, "AY":4, "AZ":8,
    "BX":1, "BY":5, "BZ":9,
    "CX":2, "CY":6, "CZ":7
}

puntaje_total2 = 0
for round in rounds:
    puntaje_total2 += salidas_deseadas[round]

print(puntaje_total2)