#In python abbiamo le collezioni che sono insiemi di diversi elementi. 
#Abbiamo liste, tuple, dizionari, set

#vediamo le liste

#Creare una lista

l = [3, 3.14, 10, "ciao", True]

#per accedere agli elementi vigono le stesse regole di indicizzazione e slicing
# delle stringhe

print(f"L'ultimo elemento della lista è {l[-1]}")
print(l)
print(f"Tutta la lista senza il primo e l'ultimo elemento è {l[1:-1]}")

#Aggiungere un elemento alla lista

l.append("NUOVO") #NON RESTITUISCE NULLA MA MODIFICA l
print(l)
l.pop() #Rimuove l'ultimo elemento della lista
l.pop()
print(l)