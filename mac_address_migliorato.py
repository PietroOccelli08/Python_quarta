def main():
    file = open("mac-vendors-export.csv", "r", encoding="utf-8") #file è un OGGETTO FILE
    righe = file.readlines()
    file.close()

    mac_address = []
    vendor = []
    data_prod = []

    for riga in righe[1:]:
        campi = riga.split(",")
        mac_address.append(campi[0])
        vendor.append(campi[1])
        data_prod.append(campi[-1])

    #print(mac_address)

    mac = input("Inserisci il MAC address per intero ->")
    mac = mac.replace("-", ":")
    print(mac)
    for i, (m, v, d) in enumerate(zip(mac_address, vendor, data_prod)):
        if m == mac[0:8]:
            print(f"{i+2} - Il produttore è {v}, La data di produzione è {d}")
##Stampare anche la data di produzione
##Gestire il carattere meno come separatore dei byte
#usare il metodo replace() delle 
#usare IA generativa per scrivere unA FUNZIONE PYTHON che restituisca il mac address
#della scheda di rete wi fi del mio pc

if __name__ == "__main__":
    main()