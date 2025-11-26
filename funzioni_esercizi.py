def funz1():
    file = open("ip.csv", "r")
    righe = file.readlines()
    file.close()

    for riga in righe:
        ip = riga[:-1].replace(",", ".")
        print(ip)
def controllaip(ip):
    lista = ip.split(".")
    print(lista)
    for campo in lista:
        pass


def main():
    file = open("voti.csv", "r") #file è un OGGETTO FILE
    righe = file.readlines() #restituisce una lista di stringhe che contine le righe del file
    file.close() #chiude il file

    lista_nomi = []
    lista_voti = []

    for riga in righe[1:]:
        campi = riga.split(",")
        lista_nomi.append(campi[0][0].upper() + campi[0][1:])
        lista_voti.append(int(campi[1]))    
    
    diz = {}
    for n, v in zip(lista_nomi, lista_voti):
        diz[n] = v
    
    print(diz)

    funz1()
    controllaip("192.168.168.1")

if __name__ == "__main__":
    main()