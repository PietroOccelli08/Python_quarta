# Crea un programma che chieda all'utente un numero intero e 
# stampi se il numero è divisibile per 2, 3 o per 5
# (Hint: usare l'operatore "%" per il resto della divisone

numero = int(input("Inserisci un numero intero -> "))
#print(f"il numero è {numero} di tipo {type(numero)}")

if (numero % 2 == 0 and numero % 3 == 0 and numero % 5 == 0):
    print(f"Il numero {numero} è divisibile per 2, per 3 e per 5.")
elif (numero % 2 == 0 and numero % 3 == 0):
    print(f"Il numero {numero} è divisibile per 2 e per 3.")
elif (numero % 2 == 0 and numero % 5 == 0):
    print(f"Il numero {numero} è divisibile per 2 e per 5.")
elif (numero % 3 == 0 and numero % 5 == 0):
    print(f"Il numero {numero} è divisibile per 3 e per 5.")
elif (numero % 2 == 0):
    print(f"Il numero {numero} è divisibile per 2.")
elif (numero % 3 == 0):
    print(f"Il numero {numero} è divisibile per 3.")
elif (numero % 5 == 0):
    print(f"Il numero {numero} è divisibile per 5.")
else: 
    print(f"Il numero {numero} non è divisibile nè per 2, nè per 3, nè per 5.")

