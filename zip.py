def main():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [[6, 10, 5],
                  [7, 6],
                  [8, 7, 9.5, 9, 8],
                  [5, 7, 9]]

    # Voglio stampare il voto a fianco di ogni nome
    #for nome, voti in zip(lista_nomi, lista_voti):
        #print(f"{nome} - Voti: {voti}")
    
    #zip() mi permette di ciclare in parallelo su due o più liste
    #Modificare il codice per stampare la media di ognuno,
    # il numero di voti per ognuno
    # il voto massimo e minimo per ognuno 
    #print(len(lista_voti))
    somme_voti = []   #contiene la somma dei voti di ogni alunno
    num_voti = []  #numeri di voti di ogni alunno
    lista_medie = []  #medie di ogni alunno
    lista_massimo = []  #voto max di ogni alunno
    lista_minimo = []  #vot min di ogni alunno
    for voti in lista_voti:  #calcola le somme e il numero di voti, il primo ciclo è per le liste dentro lista_voti
        somma = 0
        conta = 0
        for voto in voti:   #ciclo interno ad ogni lista di lista_voti
            somma = somma + voto    #somma i singoli voti
            conta += 1      #num di voti di ogni alunno
        somme_voti.append(somma)
        num_voti.append(conta)
    #print(f"Somme voti: {somme_voti}")
    #print(f"Numero voti ognuno:{num_voti}")

    for tot, num in zip(somme_voti, num_voti):  #ciclo in parallelo tra il numero di voti e le somme
        #print(f"{tot} - {num}")
        media = tot/num
        lista_medie.append(media)
        #print(media)
    #print(f"Media di ognuno: {lista_medie}")

    for voti in lista_voti: #calcola voto minimo e massimo di ogni alunno
        massimo = voti[0]  #inizializzo al primo voto
        minimo = voti[0]
        for voto in voti:
            if voto > massimo:
                massimo = voto
            if voto < minimo:
                minimo = voto
        lista_massimo.append(massimo)
        lista_minimo.append(minimo)

    #print(f"{lista_massimo} - {lista_minimo}")

    for nome, voti, num, media, mas, min in zip(lista_nomi, lista_voti, num_voti, 
                                                               lista_medie, lista_massimo, lista_minimo):
        print(f"{nome} - Voti: {voti} - Numero voti: {num} - Media: {media} - Voto max: {mas} - Voto min: {min}")

    

if __name__ == "__main__": #dunder = double underscore, si usa in divers contesti
    main()