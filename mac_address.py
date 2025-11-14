def main():
    file = open("mac-vendors-export.csv", "r", encoding="utf-8") #file è un OGGETTO FILE
    righe = file.readlines() #restituisce una lista di stringhe che contine le righe del file
    file.close() #chiude il file

    macaddress = input("Inserisci un MAC Address -> ")
    campi = []

    for i, riga in enumerate(righe):
        campi = riga[:-1].split(",")
        if macaddress == campi[0]:
            print(f"{i+1} - {campi[1]}")
    


    #print(righe[2])
    #print(righe[7])
    #print(righe[38])
    #print(righe[102])
    #print(righe[300])


if __name__ == "__main__":
    main()