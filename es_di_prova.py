voti = {"Luca":7, "Marco":8, "Giovanni":6}
alunno = ""
max = 0
for nome in voti:
    if voti[nome]> max:
        max = voti[nome]
        alunno = nome

print(f"L'alunno con il voto maggiore è {alunno}")


file = open("ip.csv")
righe = file.readlines()
file.close()

diz = {}

for riga in righe[1:]:
    campi = []
    campi = riga.split(",")
    diz[int(campi[0])] = int(campi[1])

for num in diz:
    print(f"{num} - {diz[num]}")

file = open("comandi.csv", "r")
righe = file.readlines()
file.close()

comandi = {0: "forward", 1: "backward", 2: "left", 3: "right"}

for riga, chiave in zip(righe, comandi):
    pass
    

