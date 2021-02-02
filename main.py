import socket
import requests

from analizador import Analizar
import asyncio

import json

# Parar un localhost
# 1) netstat -ano | findstr :<PUERTO>
# 2) taskkill /PID <PID> /F

config = requests.get("https://raw.githubusercontent.com/HostHome-of/config/main/config.json").json()

HOST =  config["socket"]["host"]
PORT =  config["socket"]["puerto"]

# Esto es para tests :)
Analizar("crear|Buscador|https://github.com/maubg-debug/Buscador.git").ejecutar()

# while True:
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
#         server.bind((HOST, PORT))
#         server.listen()
#         conn, addr = server.accept()
#         with conn:
#             print(f'Nueva conexion :: {addr}')
#             while True:
#                 data = conn.recv(1024).decode()
#                 if not data:
#                     break

#                 msg = Analizar(data).ejecutar()

#                 msg = {'mensage': msg}

#                 conn.sendall(json.dumps(msg).encode())