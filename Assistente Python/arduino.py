import serial
import time

arduino = None

def conectar():
    global arduino
    if arduino is None:
        arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        time.sleep(2)

def enviar(comando):
    conectar()
    arduino.write(f"{comando}\n".encode())
    return arduino.readline().decode().strip()
