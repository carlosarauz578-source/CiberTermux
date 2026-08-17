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
