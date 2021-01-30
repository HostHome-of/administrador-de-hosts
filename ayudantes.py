import os, shutil
import rstr
import git
from pathlib import Path
from time import sleep
import stat

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

        if not ".host.home" in os.listdir(RUTA):
            # try:
            #     shutil.rmtree(RUTA)
            # except:
            #     for root, dirs, files in os.walk(RUTA, topdown=False):
            #         for name in files:
            #             os.chmod(os.path.join(root, name), 0o777)
            #             os.remove(os.path.join(root, name))
            #         for name in dirs:
            #             os.rmdir(os.path.join(root, name))
            # os.rmdir(RUTA)
            return [False, "Noy hay un .host.home en tu ruta padre"]

