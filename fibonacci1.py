n = int(input("Quanti numeri di Fibonacci vuoi? -> "))     #pass non fa niente, è vuota, il codice non da errore
a, b = 1, 1 #Inizializzazione, non dichiarazione  

if n > 2:
    print(f"La sequenza è: ")
    print(a, end = "-")
    print(b, end = "-")
    for i in range(n-2):
        a, b = a+b, a
        print(a, end = "-") 
elif n==2: 
    print(f"La sequenza è : {a}", end = "-")
    print(b, end = "-")
elif n==1:
    print(f"La sequenza è : {a}")
else:
    print(f"Non stampa la sequenza.")
