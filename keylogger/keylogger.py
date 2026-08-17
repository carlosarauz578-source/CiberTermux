import datetime

ARCHIVO_LOG = "registro.txt"

def main():
    print("🎯 Keylogger educativo (simulado en consola)")
    print("⚠️ Escribe texto, se guardará con timestamp. Ctrl+C para salir.\n")

    try:
        while True:
            entrada = input("> ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
                archivo.write(f"[{timestamp}] {entrada}\n")
            print(f"[{timestamp}] {entrada}")
    except KeyboardInterrupt:
        print("\n✅ Detenido correctamente")

if __name__ == "__main__":
    main()
