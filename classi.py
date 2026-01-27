#creare classi permette di creare oggetti
import math

class Punto():
    #costruttore viene chiamato da Punto()
    def __init__(self, x, y): #self = this in java
        #attributi
        self.x = x
        self.y = y
    
    def __str__(self):
        #ritornare una stringa
        return f"({self.x}, {self.y})"
    
    def distanza_origine(self):
        #ritorna la distanza del punto dall'origine 0,0
        return math.sqrt(self.x**2 + self.y**2)
    
    def scambia_coordinate(self):
        #ritorna un nuovo punto con x e y scambiate
        x, y = self.y, self.x
        b = Punto(x, y)
        return b

    def disegna(self):
        #usa turtle per disegnare il punto
        ...
    
    def distanza(self, altro):
        #restituisce la distanza tra il punto e altro
        #altro è una istanza di unn altro punto
        ...

def main():
    a = Punto(3, 4) #istanza di punti
    print(a)
    print(f"Il punto dista {a.distanza_origine()} dall'origine")
    a = a.scambia_coordinate
    print(a)

if __name__ == "__main__":
    main()