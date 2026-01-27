# attributi: lato, x, y del vertice di un lato a sinistra
# funzioni: area, perimetro, disegna(colore pieno)
# disegna 100 quadrati casuali

import turtle
import random

class Quadrato():
    def __init__(self, x, y, lato): # self è come this. in java
        # Attributi (in Python tutto è pubblico)
        self.x = x
        self.y = y
        self.lato = lato

    def __str__(self):
        return f"({self.x}, {self.y}, {self.lato})"
    
    def area(self):
        return self.lato ** 2
    
    def perimetro(self):
        return self.lato * 4
        
    def disegna(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color("blue") 
        turtle.begin_fill() 
        for _ in range(4):
            turtle.forward(self.lato)
            turtle.right(90)
        turtle.end_fill()

    def casuali(self):
        colori = ["red", "green", "blue", "yellow"]
        for _ in range(100):
            
            turtle.penup()
            turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
            turtle.pendown()
            colore = random.choice(colori)
            turtle.color(colore)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(self.lato)
                turtle.right(90)
            turtle.end_fill()
        

def main():
    q = Quadrato(3, 4, 50)

    a = q.area()
    print(f"Area: {a}")

    p = q.perimetro()
    print(f"Perimetro: {p}")

    turtle.speed(0)

    q.disegna()

    q.casuali()

    turtle.mainloop()



if __name__ == "__main__":
    main()