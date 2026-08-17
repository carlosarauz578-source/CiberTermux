import os
import exifread

def analizar_imagen(ruta):
    # Expande ~ a la ruta completa del home en Termux
    ruta = os.path.expanduser(ruta)
    print(f"\n🔍 Analizando: {ruta}")

    # Tamaño del archivo
    try:
        size = os.stat(ruta).st_size
        print(f"📂 Tamaño del archivo: {size} bytes")
    except FileNotFoundError:
        print(f"[-] Error: No se encontró el archivo en {ruta}")
        return

    # Metadatos EXIF
    try:
        with open(ruta, 'rb') as f:
            tags = exifread.process_file(f)
            if tags:
                print("📑 Metadatos encontrados:")
                for tag in list(tags.keys())[:10]:  # muestra los primeros 10
                    print(f"  {tag}: {tags[tag]}")
            else:
                print("⚠️ No se encontraron metadatos EXIF.")
    except Exception as e:
        print(f"[-] Error al leer la imagen: {e}")

if __name__ == "__main__":
    ruta = input("Ingresa la ruta de la imagen: ")
    analizar_imagen(ruta)	

