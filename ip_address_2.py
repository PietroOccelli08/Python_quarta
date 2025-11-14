#chiede quanti bit  si vuole
#chiede un  numero bin
#confronta, se bin < bit aggiungo quanti zeri mancano

bit = int(input("inserisci il numero di bit che desideri -> "))
binario = input("inserisci un numero binario -> ")
len_binario = len(binario)

if len_binario < bit:
    binario_2 =("0" * (bit - len_binario)) + binario 
    print(binario_2)
    #print(type(binario))
elif len_binario == bit:
    print(binario)
