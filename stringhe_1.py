# In python possiamo delimitare con "" oppure ''
stringa = "Ciao Mondo!"
print(stringa)

#Esempio di indicizzazione della stringa
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

#Esempio di slicing delle stringhe
print(f"La sottostringa 2-7 è {stringa[2:7]}.")

#Assegnazione multipla (vale per ogni tipo di dato)
nome, cognome = "Mario", "Rossi"

#Concatenazione fra stringhe
x = nome + " " + cognome
print(x)

#Concatenazione di una stringa con se stessa più volte
y = (nome + " ") * 5
print(y)

a = input("-> ")
print(a[1:-1])