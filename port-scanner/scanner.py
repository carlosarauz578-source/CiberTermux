import socket
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# Diccionario de servicios comunes
SERVICIOS_COMUNES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-alt"
}

def check_port(ip, port, timeout=0.5):
    """Comprueba si un puerto TCP está abierto usando la IP directa."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))

            if result == 0:
                servicio = SERVICIOS_COMUNES.get(port, "Desconocido")
                print(f"[+] Puerto {port} abierto ({servicio})")
                return port, servicio

    except (socket.timeout, socket.error):
        pass

    return port, None

def scan_ports(target, start_port, end_port, timeout=0.5, max_workers=50):
    """Escanea un rango de puertos TCP usando un pool de hilos."""
    resultados = {}

    try:
        ip = socket.gethostbyname(target)
        print(f"[+] Objetivo resuelto a: {ip}\n")
    except socket.gaierror:
        print("[-] Error: Host o dominio no encontrado.")
        return resultados

    print(f"Escaneando {target} ({ip}) del puerto {start_port} al {end_port}...\n")

    try:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(check_port, ip, port, timeout): port
                for port in range(start_port, end_port + 1)
            }

            for future in as_completed(futures):
                try:
                    port, servicio = future.result()
                    if servicio:
                        resultados[port] = servicio
                except Exception as error:
                    print(f"[-] Error comprobando el puerto {futures[future]}: {error}")

    except KeyboardInterrupt:
        print("\n[-] Escaneo interrumpido por el usuario.")
        sys.exit(1)

    puertos_ordenados = sorted(resultados.keys())
    return {port: resultados[port] for port in puertos_ordenados}

def get_port(prompt):
    """Solicita y valida un número de puerto."""
    while True:
        try:
            port = int(input(prompt))
            if 0 <= port <= 65535:
                return port
            print("[-] El puerto debe estar entre 0 y 65535.")
        except ValueError:
            print("[-] Introduce un número de puerto válido.")

def main():
    print("=" * 50)
    print("        ESCÁNER TCP DE PUERTOS (TERMUX READY)")
    print("=" * 50)

    objetivo = input("Introduce la IP o dominio: ").strip()

    if not objetivo:
        print("[-] Debes introducir una IP o dominio.")
        sys.exit(1)

    inicio = get_port("Puerto inicial: ")
    fin = get_port("Puerto final: ")

    if inicio > fin:
        print("[-] El puerto inicial no puede ser mayor que el final.")
        sys.exit(1)

    try:
        timeout_input = input("Timeout por puerto en segundos [Defecto 0.5]: ").strip()
        timeout = float(timeout_input) if timeout_input else 0.5
    except ValueError:
        timeout = 0.5
        print("[!] Valor no válido. Usando timeout de 0.5s por defecto.")

    try:
        datos = scan_ports(objetivo, inicio, fin, timeout=timeout)
    except KeyboardInterrupt:
        print("\n[-] Escaneo interrumpido por el usuario.")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("RESULTADOS DEL ESCANEO")
    print("=" * 50)

    if datos:
        print(json.dumps(datos, indent=4))
    else:
        print("No se encontraron puertos abiertos.")

    try:
        with open("resultados.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print("\n[+] Resultados guardados en 'resultados.json'")
    except OSError as error:
        print(f"[-] No se pudo guardar el archivo: {error}")

if __name__ == "__main__":
    main()	

