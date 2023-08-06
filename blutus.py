import bluetooth
import time
import os

def clear_console():
    # Verificamos si el sistema operativo es Windows o Unix (Linux/Mac) y limpiamos la consola en consecuencia
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def print_ascii():
    print("\x1b[95m")
    print(r"""
          
██████╗ ██╗     ██╗   ██╗████████╗██╗   ██╗███████╗
██╔══██╗██║     ██║   ██║╚══██╔══╝██║   ██║██╔════╝
██████╔╝██║     ██║   ██║   ██║   ██║   ██║███████╗
██╔══██╗██║     ██║   ██║   ██║   ██║   ██║╚════██║
██████╔╝███████╗╚██████╔╝   ██║   ╚██████╔╝███████║
╚═════╝ ╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝
          Hecho por 24_huugo

""")
    print("\x1b[0m")

def scan_bluetooth_devices():
    nearby_devices = bluetooth.discover_devices(duration=1, lookup_names=True, lookup_class=True)
    return nearby_devices

def print_devices(devices):
    print("Dispositivos Bluetooth encontrados:")
    for addr, name, _ in devices:
        print(f"  Dirección: {addr} - Nombre: {name}")
    print("\x1b[95mPulsa ctrl+c para salir\x1b[0m")  # Color rosa claro (formato ANSI)

if __name__ == "__main__":
    while True:
        devices = scan_bluetooth_devices()
        clear_console()  # Limpiar la consola antes de imprimir la nueva información
        print_ascii()  # Mostrar el ASCII nuevamente
        print_devices(devices)
        time.sleep(1)
