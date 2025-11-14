# Crea un programma che chieda all'utente al suo nome 
# e lo stampi con sempre con l'iniziale maiuscola

nome = input("Inserisci il tuo nome -> ")
nome_maiusc = nome[0].upper() + nome[1:]
print(f"Il tuo nome è: {nome_maiusc}")
