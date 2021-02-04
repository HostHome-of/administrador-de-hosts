from ayudantes import Ayudantes

class Analizar():
    def __init__(self, cuerda: str):
        self.cuerda = cuerda
        self.info = self.cuerda.split("|")

        self.modo = self.info[0]
        self.param1 = self.info[1]

        self.ayuda = Ayudantes(self.cuerda)

        try:
            self.param2 = self.info[2]
        except IndexError:
            pass

    def ejecutar(self):
        try:
            funcion = getattr(Analizar, self.modo)
        except AttributeError:
            raise Exception("Modo no encontrado")

        data = funcion(Analizar(self.cuerda))
        return data

    def crear(self):
        info = self.ayuda._crear_ruta()
        lenguage = info[0]
        cmdStart = info[1]
        token = info[2]

        tipo = None

        if lenguage in ["ruby", "python", "nodejs", "scala", "clojure", "cs", "php"]:
            if lenguage == "ruby":
               pass
            elif lenguage == "python":
                tipo = "python-buildpack"
            elif lenguage == "nodejs":
                tipo = "node-buildpack"
            elif lenguage == "scala":
                pass
            elif lenguage == "clojure":
                pass
            elif lenguage == "cs":
                pass
            else: # php
                pass
        else:
            return [False, "Ese lenguage no existe"] 

        response = self.ayuda._crear(tipo, lenguage, cmdStart, token)
        return response

    def eliminar(self):
        pass

    def info(self):
        pass