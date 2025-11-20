def main():
    file = open("mac-vendors-export.csv", "r", encoding="utf-8")
    righe = file.readlines()
    file.close()
    #print(righe)
    #exit()

    elenco = {}  # crea subito il dizionario
    
    for riga in righe[1:]:  # salta l'intestazione
        campi = riga.split(",")
        mac = campi[0]
        vendor = campi[1]
        elenco[mac] = vendor # carica direttamente nel dizionario
    #print(elenco)
    #exit()

    mac_input = input("Inserisci il MAC address per intero ->")
    mac_input = mac_input.replace("-", ":")
    print(mac_input)

    mac_prefix = mac_input[0:8]  # estrai i primi 8 caratteri

    if mac_prefix in elenco:
        print(f"Il produttore è {elenco[mac_prefix]}")
    else:
        print("MAC address non trovato!")

if __name__ == "__main__":
    main()