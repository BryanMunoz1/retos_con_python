# **
# Centro de Biotecnología Agropecuaria
# Ficha: 2877795
# Aprendiz: Bryan Muñoz
# Versión: Python 3.12
# Fecha: 29/05/2024
# **

"""
Este programa tiene la función de gestionar diferentes tipos de productos, 
tales como productos grabados, software, productos impresos, revistas y libros.
Permite ingresar, almacenar y mostrar información detallada de cada producto.
"""

from random import randint

class Producto:
    """
    Clase base que representa un producto genérico.
    """
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_codigo(self):
        return self.codigo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_autor(self, autor):
        self.autor = autor

    def get_autor(self):
        return self.autor

    def informacion(self):
        """
        Imprime la información básica del producto.
        """
        print("El código es: {0}, El título es: {1}, El autor es: {2}".format(
            self.get_codigo(), self.get_titulo(), self.get_autor()))

class ProductoGrabado(Producto):
    """
    Clase que representa un producto grabado, hereda de Producto.
    """
    def __init__(self, codigo, titulo, autor, tiempoduracion, mediotecnologico):
        super().__init__(codigo, titulo, autor)
        self.tiempoduracion = tiempoduracion
        self.mediotecnologico = mediotecnologico

    def set_tiempoduracion(self, tiempoduracion):
        self.tiempoduracion = tiempoduracion

    def get_tiempoduracion(self):
        return self.tiempoduracion

    def set_mediotecnologico(self, mediotecnologico):
        self.mediotecnologico = mediotecnologico

    def get_mediotecnologico(self):
        return self.mediotecnologico

    def informacion(self):
        """
        Imprime la información completa del producto grabado.
        """
        print("El código es: {0}, El título es: {1}, El autor es: {2}, El tiempo de duración es: {3}, El medio tecnológico es: {4}".format(
            self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_tiempoduracion(), self.get_mediotecnologico()))

    def leer_datos(self):
        """
        Solicita al usuario que ingrese los datos del producto grabado.
        """
        self.set_codigo(input("Digite el código: "))
        self.set_titulo(input("Digite el título: "))
        self.set_autor(input("Digite su autor: "))
        self.set_tiempoduracion(input("Digite el tiempo de duración: "))
        self.set_mediotecnologico(input("Digite el medio tecnológico: "))

class ProductoSoftware(Producto):
    """
    Clase que representa un producto de software, hereda de Producto.
    """
    def __init__(self, codigo, titulo, autor, version, sistemaOperativo):
        super().__init__(codigo, titulo, autor)
        self.version = version
        self.sistemaOperativo = sistemaOperativo

    def set_version(self, version):
        self.version = version

    def get_version(self):
        return self.version

    def set_sistemaOperativo(self, sistemaOperativo):
        self.sistemaOperativo = sistemaOperativo

    def get_sistemaOperativo(self):
        return self.sistemaOperativo

    def informacion(self):
        """
        Imprime la información completa del producto de software.
        """
        print("El código es: {0}, El título es: {1}, El autor es: {2}, La versión es: {3}, El sistema operativo es: {4}".format(
            self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_version(), self.get_sistemaOperativo()))

    def leer_datos(self):
        """
        Solicita al usuario que ingrese los datos del producto de software.
        """
        self.set_codigo(input("Digite el código: "))
        self.set_titulo(input("Digite el título: "))
        self.set_autor(input("Digite su autor: "))
        self.set_version(input("Digite la versión: "))
        self.set_sistemaOperativo(input("Digite el sistema operativo: "))

class ProductoImpreso(Producto):
    """
    Clase que representa un producto impreso, hereda de Producto.
    """
    def __init__(self, codigo, titulo, autor, editorial, año, precio):
        super().__init__(codigo, titulo, autor)
        self.editorial = editorial
        self.año = año
        self.precio = precio

    def set_editorial(self, editorial):
        self.editorial = editorial

    def get_editorial(self):
        return self.editorial

    def set_año(self, año):
        self.año = año

    def get_año(self):
        return self.año

    def set_precio(self, precio):
        self.precio = precio

    def get_precio(self):
        return self.precio

    def informacion(self):
        """
        Imprime la información completa del producto impreso.
        """
        print("El código es: {0}, El título es: {1}, El autor es: {2}, La editorial es: {3}, El año es: {4}, El precio del libro es: {5}".format(
            self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_año(), self.get_precio()))

class Revista(ProductoImpreso):
    """
    Clase que representa una revista, hereda de ProductoImpreso.
    """
    def __init__(self, codigo, titulo, autor, editorial, año, precio, revista):
        super().__init__(codigo, titulo, autor, editorial, año, precio)
        self.revista = revista

    def set_revista(self, revista):
        self.revista = revista

    def get_revista(self):
        return self.revista

    def informacion(self):
        """
        Imprime la información completa de la revista.
        """
        print("El código es: {0}, El título es: {1}, El autor es: {2}, La editorial es: {3}, El año es: {4}, El precio es: {5}, La revista es: {6}".format(
            self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_año(), self.get_precio(), self.get_revista()))

    def estado(self):
        """
        Imprime el estado de la revista.
        """
        estados = ["Edición pasada", "Edición actual"]
        alt = randint(0, len(estados) - 1)
        print("El estado de la revista es: {0}".format(estados[alt]))

    def leer_datos(self):
        """
        Solicita al usuario que ingrese los datos de la revista.
        """
        self.set_codigo(input("Digite el código: "))
        self.set_titulo(input("Digite el título: "))
        self.set_autor(input("Digite su autor: "))
        self.set_editorial(input("Digite la editorial: "))
        self.set_año(input("Digite el año: "))
        self.set_precio(input("Digite el precio: "))
        self.set_revista(input("Digite la revista: "))

class Libro(ProductoImpreso):
    """
    Clase que representa un libro, hereda de ProductoImpreso.
    """
    def __init__(self, codigo, titulo, autor, editorial, año, precio, idioma):
        super().__init__(codigo, titulo, autor, editorial, año, precio)
        self.idioma = idioma

    def set_idioma(self, idioma):
        self.idioma = idioma

    def get_idioma(self):
        return self.idioma

    def informacion(self):
        """
        Imprime la información completa del libro.
        """
        print("El código es: {0}, El título es: {1}, El autor es: {2}, La editorial es: {3}, El año es: {4}, El precio es: {5}, El idioma es: {6}".format(
            self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_año(), self.get_precio(), self.get_idioma()))

    def estado(self):
        """
        Imprime el estado del libro.
        """
        estados = ["Disponible", "Ocupado", "En mal estado", "Desaparecido"]
        alt = randint(0, len(estados) - 1)
        print("El estado del libro es: {0}".format(estados[alt]))

    def leer_datos(self):
        """
        Solicita al usuario que ingrese los datos del libro.
        """
        self.set_codigo(input("Digite el código: "))
        self.set_titulo(input("Digite el título: "))
        self.set_autor(input("Digite su autor: "))
        self.set_editorial(input("Digite la editorial: "))
        self.set_año(input("Digite el año: "))
        self.set_precio(input("Digite el precio: "))

# Crear instancias y leer datos

productograbado = ProductoGrabado("", "", "", "", "")
productograbado.leer_datos()
productograbado.informacion()

productosoftware = ProductoSoftware("", "", "", "", "")
productosoftware.leer_datos()
productosoftware.informacion()


revista = Revista("", "", "", "", "", "", "")
revista.leer_datos()
revista.informacion()
revista.estado()

libro = Libro("", "", "", "", "", "", "")
libro.leer_datos()
libro.informacion()
libro.estado()