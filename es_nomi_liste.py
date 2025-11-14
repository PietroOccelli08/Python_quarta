lista = ["Luca", "Pierlorenzo", "Alice", "Giovanni"]

nomemax = ""
lenmax = 0

for nome in lista:
    n = len(nome)
    if n > lenmax:
        lenmax = n
        nomemax = nome
print(nomemax)

lista_maiusc = []

for nome in lista:
    lista_maiusc.append(nome.upper())
print(lista_maiusc)
print(lista_maiusc[-2:])

lista_minusc = []

for nome in lista_maiusc:
    lista_minusc.append(nome.lower())
print(lista_minusc)

