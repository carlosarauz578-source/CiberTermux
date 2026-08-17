import os
import exifread

def analizar_imagen(ruta):
    print(f"\n🔍 Analizando: {ruta}")

    # Tamaño del archivo
    size = os.stat(ruta).st_size
    print(f"📂 Tamaño del archivo: {size} bytes")

    # Metadatos EXIF
    with open(ruta, 'rb') as f:
        tags = exifread.process_file(f)
        if tags:
            print("📑 Metadatos encontrados:")
            for tag in list(tags.keys())[:10]:  # muestra los primeros 10
                print(f"  {tag}: {tags[tag]}")
        else:
            print("⚠️ No se encontraron metadatos EXIF.")

if __name__ == "__main__":
    ruta = input("Ingresa la ruta de la imagen: ")
    analizar_imagen(ruta)
