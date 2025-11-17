file = open("./dati.csv", "r")  #file è un OGGETTO FILE
righe = file.readlines() #restituisce una lista di stringhe che contine le righe del file
file.close() #chiude il file
#print(righe[0])

prima_riga = righe[0]
#titoli = righe[0][:-1].split(",") #separa le tre parole e le stampa in titoli
# [:-1] toglie lo \n finale
#print(titoli) #titoli è una lista

titolo1, titolo2, titolo3 = prima_riga[:-1].split(",")
print(titolo1)

#lleggere tutte le altre righe del file e stamparle
#usare un ciclo for pythonico (NO RANGE)

def main():
    pass