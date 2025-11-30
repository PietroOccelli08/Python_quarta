def main():
    file = open("testo.txt", "r")
    testo = file.read()
    file.close()

    lettere_diz = {}
    conteggio = 0

    for carattere in testo:
        if carattere.isalpha():
            lettera = carattere.lower()
            conteggio += 1
            if lettera in lettere_diz:
                lettere_diz[lettera] += 1
            else:
                lettere_diz[lettera] = 1
    #print(conteggio)
    percentuali = {}
    for lettera in lettere_diz:
        #print(f"{lettera} - {lettere_diz[lettera]}")
        perc = (lettere_diz[lettera] * 100)/conteggio
        percentuali[lettera] = perc
    for lettera in lettere_diz:
        print(f"{lettera}: {lettere_diz[lettera]}")
        print(f"{percentuali[lettera]:.6f} %")
    

if __name__ == "__main__":
    main()

#Scrivere un programma che:
#legga un file di testo (ad esempio i  Promessi Sposi o qualsiasi altro testo italiano). Costruisca un dizionario che
#  associ ad ogni lettera il suo conteggio.Calcoli la frequenza percentuale di ogni lettera.
# Specifiche
#Ignorare maiuscole/minuscole (trattare 'A' come 'a')
#Ignorare spazi, punteggiatura, numeri — contare solo le 26 lettere dell'alfabeto base
#Il file di input si chiama testo.txt
#Suggerimenti
#str.isalpha() restituisce True se il carattere è una lettera
#str.lower() converte in minuscolo