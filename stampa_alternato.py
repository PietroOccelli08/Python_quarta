# Crea un programma che chieda all'utente una frase e stampi 
# la stringa inserita un carattere si e uno no (caratteri alternati)

frase = input("Scrivi una frase -> ")
#print(frase)
frase_alternata = frase[::2]
print(f"La tua frase alternata è: {frase_alternata}")
