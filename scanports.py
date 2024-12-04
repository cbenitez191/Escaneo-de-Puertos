import socket

ip = input("Ingrese la dirección IP a escanear: ")

print(f"Escaneando puertos abiertos en {ip}...")

for port in range(1, 1025): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  
    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"Puerto abierto: {port}")

    sock.close()  

print("Escaneo completado.")
