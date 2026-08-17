# Keylogger Ético (Simulado en Termux)

Este proyecto demuestra cómo funcionan los keyloggers, adaptado a Termux/Android.  
En lugar de capturar teclas globales (no soportado en Android), simula la captura de entradas en consola.

## 🚀 Características
- Guarda cada entrada en `registro.txt` con fecha y hora.
- Funciona en cualquier dispositivo Android con Termux.
- Uso exclusivo en entornos educativos.

## ⚠️ Advertencia
El uso indebido en sistemas ajenos sin permiso es ilegal.  
Este proyecto es solo para fines educativos y de concienciación.

## 🛠️ Instalación
```bash
pkg install python git


Ejecutador y resultado: ~/CiberTermux/keylogger $ python3 keylogger.py
🎯 Keylogger educativo (simulado en consola)
⚠️ Escribe texto, se guardará con timestamp. Ctrl+C para salir.

> HOLA
[2026-08-17 03:02:41] HOLA
> ^C

✅ Detenido correctamente
