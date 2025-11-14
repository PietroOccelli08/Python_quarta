def main():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [[6, 10, 5],
                  [7, 6],
                  [8, 7, 9.5, 9, 8],
                  [5, 7, 9]]
    somme_voti = []
    num_voti = []
    lista_medie = []
    lista_massimo = []
    lista_minimo = []
    for voti in lista_voti:
        somma = 0
        n_voti = len(voti)
        massimo = 0
        minimo = voti[0]
        for voto in voti:
            somma = somma + voto
            if voto > massimo:
                massimo = voto
            if voto < minimo:
                minimo = voto
        media = somma/n_voti  #faccio direttamente la somma usando conta per il numero di voti e somma per ogni singola somma
        somme_voti.append(somma)
        num_voti.append(n_voti)
        lista_medie.append(media)
        lista_massimo.append(massimo)
        lista_minimo.append(minimo)
    
    for nome, voti, num, media, mas, min in zip(lista_nomi, lista_voti, num_voti, 
                                                               lista_medie, lista_massimo, lista_minimo):
        print(f"{nome} - Voti: {voti} - Numero voti: {num} - Media: {media} - Voto max: {mas} - Voto min: {min}")

if __name__ == "__main__": #dunder = double underscore, si usa in divers contesti
    main()