ip = input("Inserisci un indirizzo IP -> ")
ottetti_str = ip.split(".")  # .split è un METODO  delle strinhghe che sudivide una stringa
#cercando il carattere separatore che viene passato 
print(ottetti_str)
ottetti = []  #lista nuova con gli elemneti INT
for s in ottetti_str:
    ottetti.append(int(s))     #192.168.1.2

print(ottetti)
bit = 8 #numero di bit che deve avere il binario
    
ottetti_bin = []  #stringa che contiene i binari
for n in ottetti:
    binario = bin(n)[2:]  #conversione di ogni numero in binario senza "0b" all'inizio
    #print(binario)
    len_binario = len(binario)  #lunghezza di ogni binario
    #print(len_binario)
    if len_binario < bit:
        binario =("0" * (bit - len_binario)) + binario  #assegna a binario il numero di zeri necessario per arrivare a 8 bit
        print(binario)
        ottetti_bin.append(binario)  #aggiunge i binari alla lista
        #print(type(binario))
    elif len_binario == bit:
        print(binario)
        ottetti_bin.append(binario)

print(ottetti_bin)

ip_binario = ottetti_bin[0] + "." + ottetti_bin[1] + "." + ottetti_bin[2] + "." + ottetti_bin[3] + "."
print(ip_binario)




