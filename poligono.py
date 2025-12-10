#chiedere all'utente un numero intero maggiore di due e disegnare il 
#poligono regolare a n lati

import turtle

def main():
    l = int(input("Inserisci il numero di lati -> "))
    angolo = 360 / l
    lato = 100
    for i in range(l):
        turtle.forward(lato)
        turtle.left(angolo)
    
    turtle.mainloop()
    

if __name__ == "__main__":
    main()