import random
def ping(ip):
    i = random.randint(0,1)
    if i == 0:
        return False
    else:
        return True

def main():
    lista_ip = ["192.168.100.1", "10.100.23.201", "176.37.0.1"]
    diz = {}
    for ip in lista_ip:
        result = ping(ip)
        diz[ip] = result
    print(diz)

if __name__ == "__main__":
    main()