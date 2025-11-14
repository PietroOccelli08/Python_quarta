a = input("Inserisci una parola -> ")
a = a.lower()
if a == a[::-1]:
    print(f"La stringa è palindroma")
else: 
    print(f"La stringa NON è palindroma")