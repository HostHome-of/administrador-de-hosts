import socket
import requests

from flask import Flask, redirect

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
    return {"mensage": Analizar("Buscador|https://github.com/maubg-debug/Buscador.git").crear()}

app.run("localhost", 4000)