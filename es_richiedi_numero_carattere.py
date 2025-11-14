#Chiedere all'utente un numero intero, un carattere e creare una strigna che sia quel carattere 
#ripetuto tante volte quante il numero
intero = int(input("Inseriscii un numero intero -> "))

parola = input("Inserisci una parola -> ")

stringa = (parola + " ") * intero

print(stringa)