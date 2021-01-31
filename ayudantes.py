import os, shutil
import rstr
import git
from pathlib import Path
from time import sleep
from win32 import win32api
from win32.lib import win32con

class Ayudantes():
    def __init__(self, cuerda:str):
        self.cuerda = cuerda.split("|")

        self.info = self.cuerda[0]
        self.param1 = self.cuerda[1]

        try:
            self.param2 = self.cuerda[2]
        except IndexError:
            pass

    def __token(self):
        _token = rstr.xeger(r'^[a-zA-Z0-9]*$')
        for carpeta in os.listdir("./projectos"):
            if carpeta == _token:
                return self.__token()

        return _token

    def _crear(self):
        token = self.__token()
        RUTA = f"./projectos/{token}"
        os.mkdir(RUTA)
        git.Repo.clone_from(url=self.param2, to_path=RUTA)

        if not ".hosthome" in os.listdir(RUTA):
            try:
                shutil.rmtree(RUTA)
            except:
                for root, dirs, files in os.walk(RUTA, topdown=False):
                    for name in files:
                        win32api.SetFileAttributes(os.path.join(root, name), win32con.FILE_ATTRIBUTE_NORMAL)
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
            os.rmdir(RUTA)
            return [False, "No hay un .hosthome en tu ruta padre"]
