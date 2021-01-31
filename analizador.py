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
        response = self.ayuda._crear()
        return response

    def eliminar(self):
        pass

    def info(self):
        pass