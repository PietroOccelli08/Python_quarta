import subprocess
import re

def preparaMac(mac_str):
    mac_str = mac_str.replace("-", ":")
    return mac_str.upper()

def get_wifi_mac_windows():
    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        # Regex più robusta e corretta
        match = re.search(
            r"(address|indirizzo).*?([0-9A-Fa-f:-]{17})",
            result,
            re.IGNORECASE
        )

        if match:
            return match.group(2).upper()

        return None

    except Exception as e:
        print("Errore:", e)
        return None



def main():
    file = open("mac-vendors-export.csv", "r", encoding="utf-8")
    righe = file.readlines()
    file.close()
    #print(righe)
    #exit()

    elenco = {}  
    elenco_date = {}
    
    for riga in righe[1:]:  # salta l'intestazione, riga è una stringa
        campi = riga.split(",") #campi è una lòista di stringhe
        mac = campi[0]
        vendor = campi[1]
        elenco[mac] = vendor # carica direttamente nel dizionario
    #print(elenco)
    #exit()

    mac_input = get_wifi_mac_windows()                #input("Inserisci un mac: ")
    mac_input = preparaMac(mac_input)
    print(mac_input)

    mac_prefisso = mac_input[0:8]  # prende i primi 8 caratteri del MAC

    if mac_prefisso in elenco:
        print(f"Il produttore è {elenco[mac_prefisso]}")
    else:
        print("MAC address non trovato!")

if __name__ == "__main__":
    main()