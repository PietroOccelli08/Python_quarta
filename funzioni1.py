#suddividere il codice in funzioni significa renderlo MODULARE
#MODULARITA': suddividere il codice in moduli = funzioni
#COSTANTE è una  variabile globale
#ATTENZIONE: COSTANTE è accessibile da tutte le funzioni soltanto in lettura

COSTANTE = 3.14

def prima_lettera_maiusc(stringa):
    '''
    DOCSTRING:
    La funzione restituisce stringa
    con la lettera maiuscola.
    '''
    #stringa è una variabile locale
    s = stringa[0].upper() + stringa[1:].lower()
    return s

def media(lista):
    '''
    La funzione restituisce la media dei valori presenti in 
    lista e il numero di elementi di lista
    '''
    somma = 0.  #float
    n_lista = len(lista)
    for val in lista: #
        somma = somma + val
    return somma/n_lista, n_lista

def oscuraPassword(s):
    nCar = len(s)
    return s[0] + ((nCar-1) * "*")

def main():
    #print(help(prima_lettera_maiusc))
    #nome = input("Inserisci una parola -> ")
    #print(prima_lettera_maiusc(nome)) #chiamo la funzione e stampo il risultato
    voti = [4.5, 5.5, 8.25, 5, 6]
    m, n = media(voti)
    print(f"La media è {m}, il numero di voti è {n}.")
    if m > 6:
        print("🤣")
    else:
        print("🤮")

    
    

if __name__ == "__main__":
    main()