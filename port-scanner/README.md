# Escáner TCP de Puertos (Termux Ready)

Este proyecto es un escáner de puertos escrito en Python, diseñado para fines educativos y auditorías de seguridad autorizadas.  
Funciona en **Termux** y aprovecha **multithreading** para acelerar el escaneo de rangos completos de puertos.

---

## 🚀 Características
- Escaneo de puertos TCP en rangos definidos por el usuario.
- Resolución automática de dominios a IP.
- Multithreading para mayor velocidad.
- Timeout configurable por puerto.
- Identificación de servicios comunes (SSH, HTTP, HTTPS, MySQL, etc.).
- Resultados ordenados y exportados en formato **JSON**.
- Compatible con **Termux** y cualquier entorno con Python 3.

---

## 🛠️ Instalación
1. Instala Python y Git en Termux:
   ```bash
   pkg update && pkg upgrade
   pkg install python git

Ejecutador y resultado: python3 scanner.py
==================================================
        ESCÁNER TCP DE PUERTOS (TERMUX READY)
==================================================
Introduce la IP o dominio: www.google.com
Puerto inicial: 1
Puerto final: 1000
Timeout por puerto en segundos [Defecto 0.5]: 0.7
[+] Objetivo resuelto a: 142.251.153.119

Escaneando www.google.com (142.251.153.119) del puerto 1 al 1000...

[+] Puerto 80 abierto (HTTP)
[+] Puerto 443 abierto (HTTPS)

==================================================
RESULTADOS DEL ESCANEO
==================================================
{
    "80": "HTTP",
    "443": "HTTPS"
}

[+] Resultados guardados en 'resultados.json'
~/CiberTermux/port-scanner $
