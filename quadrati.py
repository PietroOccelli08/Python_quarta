n = int(input("Inserisci un numero -> "))
if n < 0:
    print(f"Non si possono calcolare i quadrati")
else:
    for i in range (n):
        quad = i*i
        print(quad, end = " ")