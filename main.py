import socket
import requests

from flask import Flask, redirect, session, request

from analizador import Analizar
import asyncio

import json

# Parar un localhost
# 1) netstat -ano | findstr :<PUERTO>
# 2) taskkill /PID <PID> /F

app = Flask(__name__)
config = requests.get("https://raw.githubusercontent.com/HostHome-of/config/main/config.json").json()

URL  =  config["url"]
HOST =  config["socket"]["host"]
PORT =  config["socket"]["puerto"]

# Esto es para tests :)
# Analizar("crear|Buscador|https://github.com/maubg-debug/Buscador.git").ejecutar()

@app.route("/")
def paginaPrincipal():
    return redirect(URL)

@app.route("/crear", methods=["GET", "POST"])
def crear():
    if session.method == "POST":
        nombre = request.args.get("nombre") # Nombre

        # Headers
        gitUrl = request.headers.get("gitUrl")

        return {"mensage": Analizar(f"{nombre}|{gitUrl}").crear()}

if __name__ == "__main__":
    app.run("localhost", 4000)