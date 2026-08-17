# Detector de Metadatos EXIF (Termux Ready)

Este proyecto contiene un script en Python que analiza imágenes y extrae metadatos EXIF.  
Funciona en **Termux** y en cualquier entorno con Python 3.

---

## 🚀 Características
- Muestra el tamaño del archivo en bytes.
- Extrae y lista los metadatos EXIF disponibles.
- Compatible con imágenes JPG/JPEG.
- Uso sencillo desde la terminal.

---

## 🛠️ Instalación
1. Instala Python y Git en Termux:
   ```bash
   pkg update && pkg upgrade
   pkg install python git


Ejecutador y resultado: $ python3 detector.py
Ingresa la ruta de la imagen: ~/storage/downloads/image_1782931892219.jpeg

🔍 Analizando: /data/data/com.termux/files/home/storage/downloads/image_1782931892219.jpeg
📂 Tamaño del archivo: 448467 bytes
⚠️ No se encontraron metadatos EXIF.
~/CiberTermux/detector $
