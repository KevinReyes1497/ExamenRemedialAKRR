def main():
    ip_red = input("Ingrese la dirección IP de red: ")
    prefijo = input("Ingrese el prefijo de la máscara de subred: ")

    ips_activas = ["192.168.1.1", "192.168.1.10"]  

    print("Direcciones IP activas:")
    for ip in ips_activas:
        print(ip)

    with open("IPsActivasX_X_X_X.txt", "w") as file:
        file.write("Direcciones IP activas:\n")
        for ip in ips_activas:
            file.write(ip + "\n")

if __name__ == "__main__":
    main()
