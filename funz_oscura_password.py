
def oscuraPassword(s):
    nCar = len(s)
    return s[0] + ((nCar-1) * "*")

def main():
    lista_password = ["ciao", "popopop", "lello"]
    password_oscurate = []
    for password in lista_password:
        password_oscurate.append(oscuraPassword(password))
    
    for password in password_oscurate:
        print(password)


if __name__ == "__main__":
    main()