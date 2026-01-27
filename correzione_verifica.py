def temp_media(dati):
    tot = 0
    for diz in dati:
        tot += diz["temp"]

    return tot/len(dati)

def filtra_citta(dati, nome):
    temp = []
    for diz in dati:
        if nome == diz["citta"]:
            temp.append(diz["temp"])
    print(f"La media di {nome} è {temp}")
    
    return None

def temp_per_citta(dati):
    lista_citta = {}
    for luogo in dati:
        if luogo["citta"] not in lista_citta:
            lista_citta[luogo["citta"]] = [luogo["temp"]]
        else:
            lista_citta[luogo["citta"]].append(luogo["temp"])
    return lista_citta

def carica_regioni(nome_file):
    file = open(nome_file, "r")
    righe = file.readlines()
    file.close()

    diz = {}
    for riga in righe:
        campi = riga.split(":")
        diz[campi[0]] = campi[1][:-1]

    return diz

def main():
    dati = [
        {"citta" : "Milano", "temp" : 12},
        {"citta" : "Roma", "temp" : 18},
        {"citta" : "Milano", "temp" : 14},
        {"citta" : "Napoli", "temp" : 20},
        {"citta" : "Roma", "temp" : 17},
        {"citta" : "Napoli", "temp" : 22},
        {"citta" : "Milano", "temp" : 10}
    ]
    media = temp_media(dati)
    print(f"La media e {media:.2f} C°")
    filtra_citta(dati, "Milano")
    lista_citta = temp_per_citta(dati)
    print(lista_citta)
    diz_regioni = carica_regioni("regioni.txt")
    print(diz_regioni)
    
    


if __name__ == "__main__":
    main()