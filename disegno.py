import turtle

def main():
    file = open("prova_disegno.txt", "r") 
    righe = file.readlines()
    file.close() 

    colori = {"rosso": "red", "blu": "blue", "verde": "green", "giallo": "yellow", "nero":"black"}

    for riga in righe:
        parti = riga.split()
        comando = parti[0]

        #print(f"Eseguo: {comando} {parti[1:]}")

        if comando == "avanti":
            turtle.forward(float(parti[1]))
            print(turtle.pos())
        elif comando == "indietro":
            turtle.backward(float(parti[1]))
            print(turtle.pos())
        elif comando == "destra":
            turtle.right(float(parti[1]))
        elif comando == "sinistra":
            turtle.left(float(parti[1]))
        elif comando == "salta":
            turtle.penup()
            turtle.goto(float(parti[1]), float(parti[2]))
            print(turtle.pos())
            turtle.pendown()
        elif comando == "cerchio":
            turtle.circle(float(parti[1]))
        elif comando == "colore":
            colore_italiano = parti[1]
            turtle.color(colori[colore_italiano])
        
    turtle.mainloop()

if __name__ == "__main__":
    main()

#avanti 200
#sinistra 120
#avanti 200
##sinistra 150
#colore verde
#avanti 173.205
#salta 0 0
#sinistra 150
#colore nero
#avanti 200
#salta 100 0
#sinistra 120
#colore rosso
#cerchio -57.5