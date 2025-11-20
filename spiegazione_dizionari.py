# Creazione
studente = {"nome": "Marco", "età": 18, "classe": "4A"}

# Accesso
print(studente["nome"])  # "Marco"

# Aggiunta/Modifica
studente["voto"] = 8.5  # aggiunge nuovo elemento
studente["età"] = 19     # modifica valore esistente

# Verifica esistenza
if "nome" in studente:
    print("Chiave trovata!")

# Rimozione
del studente["voto"]  # elimina la coppia chiave-valore

# Metodi utili
studente.keys()    # restituisce tutte le chiavi
studente.values()  # restituisce tutti i valori
studente.items()   # restituisce coppie (chiave, valore)