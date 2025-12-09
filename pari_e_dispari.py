"""
Simulare n partite a pari e dispari.
in input utente: 
 - n cioè numero di partite
 - nome primo giocatore
 - nome secondo giocatore

per simulare le partite usiamo un dizoionario che avrà come chiavi i nomi e come valori
una lista con le giocate
es n = 3
 d = {"Nome giocatore 1" : [3,2,5], "Nome giocatore 2" : [1,4,4]}
 le singole giocate sono generate con random.randint()

Creare una lista che contiene i nomi dei vincitori
"""
import random
MINIMO = 1
MASSIMO = 5

def randomici():
    return random.randint(MINIMO,MASSIMO)

def generaNumeri(n, nome1, nome2):
    d = {}
    lista1 = []
    lista2= []
    for i in range(n):
        lista1.append(randomici())
        lista2.append(randomici())
    d[nome1] = lista1
    d[nome2] = lista2
    return d

def vincitori(d, nome1, nome2):
    vincitori = []
    for mano1, mano2 in zip(d[nome1], d[nome2]):
        if(mano1 + mano2) % 2 == 0:
            vincitori.append(nome1)
        else:
            vincitori.append(nome2)
    
    return vincitori

def main():
    primo_giocatore = input("Inserisci il nome del primo giocatore -> ")
    secondo_giocatore = input("Inserisci il nome del secondo giocatore -> ")
    n = int(input("Inserisci il numero di partite da effettuare -> "))
    diz = generaNumeri(n, primo_giocatore, secondo_giocatore)
    print(diz)
    lista_vincitori = vincitori(diz, primo_giocatore, secondo_giocatore)
    print(lista_vincitori)


if __name__ == "__main__":
    main()



