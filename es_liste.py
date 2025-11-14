l = ["ciao", "python", "casa"]
for parola in l:
    if parola[0] == "c":
        print("!")

stringa = ""
for parola in l:
    stringa = stringa + " " + parola
print(stringa)

stringa = l[0]
for parola in l[1:]:
    stringa = stringa + " " + parola
print(stringa)