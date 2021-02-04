import os, shutil
import rstr, pprint
from pathlib import Path
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

    def __eliminar_carpeta(self, RUTA):
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

    def _crear_ruta(self):
        token = self.__token()
        RUTA = f"./projectos/{token}"
        RUTA_LOGS = f"./logs/{token}.out"
        # os.mkdir(RUTA)
        git.Repo.clone_from(url=self.param2, to_path=RUTA)

        if not ".hosthome" in os.listdir(RUTA):
            self.__eliminar_carpeta(RUTA)
            return [False, "No hay un .hosthome en tu ruta padre"]

        cmdStart = None
        lenguage = None
        with open(str(RUTA)+"/.hosthome", "r") as f:
            f = f.read()
            lineas = f.split("\n")
            for line in lineas:
                line = line.replace(" = \"", "")
                if line.startswith("run"):
                    cmdStart = line.replace("run", "")[:-2]
                if line.startswith("len"):
                    lenguage = line.replace("len", "")[:-2]

        if cmdStart is None:
            self.__eliminar_carpeta(RUTA)
            return [False, "No hay un comando de empiezo"]

        return [lenguage, cmdStart, token]

    def _crear(self, tipo, lenguage, cmdStart, token):
        RUTA = f"./projectos/{token}"
        RUTA_LOGS = f"./logs/{token}.out"      

        open(RUTA_LOGS, 'a')
        open(RUTA+"/output_hosthome.sh", 'a')

        with open(RUTA+"/output_hosthome.sh", "w") as f:
            f.write(open("./ejemplo_output.sh", "r").read())
            f.close()

        if not lenguage is None:
            archivos_de_instalacion = []
            git.Git(RUTA).clone(f"https://github.com/HostHome-of/{tipo}.git")
            for f in Path(RUTA).glob(f'{tipo}/*'):
                if ".git" in str(f):
                    continue
                try:
                    shutil.copy(f, os.path.join(RUTA))
                except:
                    continue
                archivos_de_instalacion.append(str(f).replace(f"{tipo}\\", ""))

            if tipo == "python-buildpack":
                os.mkdir(os.path.join(RUTA) + "/bin")

                for f_bin in Path(RUTA).glob('{tipo}/bin/*'):
                    try:
                        shutil.copy(f_bin, os.path.join(RUTA)+"/bin")
                    except:
                        continue
                    archivos_de_instalacion.append(str(f_bin).replace("{tipo}\\", ""))      

            os.system(f"sh {RUTA}/start_hosthome.sh {str(os.path.abspath(RUTA))}")

            for archivo in archivos_de_instalacion:
                os.remove(archivo)

            os.system(f"sh {RUTA}/output_hosthome.sh '{cmdStart}' {token}")

            return [True, f"{token}"]
        else:
            self.__eliminar_carpeta(RUTA)
            return [False, "Lenguage no asignado"]