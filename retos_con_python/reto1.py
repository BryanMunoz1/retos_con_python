# **
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz:Bryan Muñoz
# Version: Python312
# Fecha: 29/05/2024
# **

"""
Este progra,a tiene la funcion de
"""
from datetime import datetime, timedelta
from random import randint

class Persona:
    def __init__(self, documento, nombre_completo):
        """
        Constructor de la clase Persona.
        """
        self._nombre_completo = nombre_completo
        self._documento = documento

    def set_documento(self, documento):
        """
        Método para establecer el documento de la persona.
        """
        self._documento = documento

    def get_documento(self):
        """
        Método para obtener el documento de la persona.
        """
        return self._documento

    def set_nombre(self, nombre_completo):
        """
        Método para establecer el nombre completo de la persona.
        """
        self._nombre_completo = nombre_completo

    def get_nombre(self):
        """
        Método para obtener el nombre completo de la persona.
        """
        return self._nombre_completo

    def informacion(self):
        """
        Método para imprimir la información de la persona.
        """
        print("El documento del aprendiz es {0} El nombre es {1}".format(self.get_documento(), self.get_nombre()))

class Aprendiz(Persona):
    def __init__(self, documento, nombre_completo, ficha, programa):
        """
        Constructor de la clase Aprendiz.
        """
        super().__init__(documento, nombre_completo)
        self._ficha = ficha
        self._programa = programa

    def set_ficha(self, ficha):
        """
        Método para establecer la ficha del aprendiz.
        """
        self._ficha = ficha

    def get_ficha(self):
        """
        Método para obtener la ficha del aprendiz.
        """
        return self._ficha

    def set_programa(self, programa):
        """
        Método para establecer el programa del aprendiz.
        """
        self._programa = programa

    def get_programa(self):
        """
        Método para obtener el programa del aprendiz.
        """
        return self._programa

    def matricula(self):
        """
        Método para obtener el estado de matrícula del aprendiz.
        """
        matricula = ['Inscripción', 'etapa 1', 'etapa 2', 'matriculado', 'en inducción']
        alt= randint(0,len(matricula)-1)
        print("El estado del aprendiz es {0}".format(matricula[alt]))

class Instructor(Persona):
    def __init__(self, documento, nombre_completo, salario_basico, profesion):
        """
        Constructor de la clase Instructor.
        """
        super().__init__(documento, nombre_completo)
        self._profesion = profesion
        self._salario_basico = salario_basico

    def set_profesion(self, profesion):
        """
        Método para establecer la profesión del instructor.
        """
        self._profesion = profesion

    def get_profesion(self):
        """
        Método para obtener la profesión del instructor.
        """
        return self._profesion

    def set_salario_basico(self, salario_basico):
        """
        Método para establecer el salario básico del instructor.
        """
        self._salario_basico = salario_basico

    def get_salario_basico(self):
        """
        Método para obtener el salario básico del instructor.
        """
        return self._salario_basico

    def contrato(self):
        """
        Método para obtener el estado del contrato del instructor.
        """
        contrato = ['activo', 'inactivo']
        alt= randint(0,len(contrato)-1)
        print("El contrato del aprendiz es {0}".format(contrato[alt]))

class InstructorPlanta(Instructor):
    def __init__(self, documento, nombre_completo, salario_basico, profesion, grado, fecha_vinculacion):
        """
        Constructor de la clase InstructorPlanta.
        """
        super().__init__(documento, nombre_completo, salario_basico, profesion)
        self._grado = grado
        self._fecha_vinculacion = fecha_vinculacion

    def set_grado(self, grado):
        """
        Método para establecer el grado del instructor de planta.
        """
        self._grado = grado

    def get_grado(self):
        """
        Método para obtener el grado del instructor de planta.
        """
        return self._grado

    def set_fecha_vinculacion(self, fecha_vinculacion):
        """
        Método para establecer la fecha de vinculación del instructor de planta.
        """
        self._fecha_vinculacion = fecha_vinculacion

    def get_fecha_vinculacion(self):
        """
        Método para obtener la fecha de vinculación del instructor de planta.
        """
        return self._fecha_vinculacion

    def informacion(self):
        """
        Método para imprimir la información del instructor de planta.
        """
        print("El documento del instructor es {0} El nombre es {1} Su salario basico es {2} Su profesion es {3} El grado es {4} La fecha de vinculacion es {5}".format(
                                                                                self.get_documento(),
                                                                                self.get_nombre(),
                                                                                self.get_salario_basico(),
                                                                                self.get_profesion(),
                                                                                self.get_grado(),
                                                                                self.get_fecha_vinculacion(),))

    def leer_datos(self):
        """
        Método para leer los datos del instructor de planta.
        """
        self.set_documento(int(input("Digite su documento: ")))
        self.set_nombre(input("Digite su nombre: "))
        self.set_salario_basico(int(input("Digite su salario basico: ")))
        self.set_profesion(input("Digite su profesion: "))
        self.set_grado(int(input("Digite el grado de su contrato: ")))
        self.set_fecha_vinculacion(input("Digite en que fecha se vinculo: "))

    def estado(self):
        """
        Método para obtener el estado del instructor de planta.
        """
        estados=["En induccion","En formacion","Aplazado","Condicionado", "retirado"]
        alt= randint(0,len(estados)-1)
        print("El estado del instructor es {0}".format(estados[alt]))

    def calcular_sueldo(self):
        """
        Método para calcular el sueldo del instructor de planta.
        """
        sueldo = self.get_grado() * 100000
        calcular = sueldo + self.get_salario_basico()
        print(f"su sueldo es: {calcular}")

class InstructorContrato(Instructor):
    def __init__(self, documento, nombre_completo, salario_basico, profesion, duracion_contrato, fecha_vinculacion=None):
        """
        Constructor de la clase InstructorContrato.
        """
        super().__init__(documento, nombre_completo, salario_basico, profesion)
        self._duracion_contrato = duracion_contrato

        if fecha_vinculacion is not None and fecha_vinculacion != '':
            self._fecha_vinculacion = datetime.strptime(fecha_vinculacion, "%Y-%m-%d")
        else:
            self._fecha_vinculacion = None

    def get_documento(self):
        return self._documento

    def get_nombre(self):
        return self._nombre_completo

    def get_salario_basico(self):
        return self._salario_basico

    def get_profesion(self):
        return self._profesion

    def set_documento(self, documento):
        self._documento = documento

    def set_nombre(self, nombre_completo):
        self._nombre_completo = nombre_completo

    def set_salario_basico(self, salario_basico):
        self._salario_basico = salario_basico

    def set_profesion(self, profesion):
        self._profesion = profesion


class InstructorContrato(Instructor):
    def __init__(self, documento, nombre_completo, salario_basico, profesion, duracion_contrato, fecha_vinculacion=None):
        """
        Constructor de la clase InstructorContrato.
        """
        super().__init__(documento, nombre_completo, salario_basico, profesion)
        self._duracion_contrato = duracion_contrato

        if fecha_vinculacion is not None and fecha_vinculacion != '':
            self._fecha_vinculacion = datetime.strptime(fecha_vinculacion, "%Y-%m-%d")
        else:
            self._fecha_vinculacion = None

    def set_duracion_contrato(self, duracion_contrato):
        """
        Método para establecer la duración del contrato del instructor contratado.
        """
        self._duracion_contrato = duracion_contrato

    def get_duracion_contrato(self):
        """
        Método para obtener la duración del contrato del instructor contratado.
        """
        return self._duracion_contrato

    def get_fecha_vinculacion(self):
        """
        Método para obtener la fecha de vinculación del instructor contratado.
        """
        return self._fecha_vinculacion

    def set_fecha_vinculacion(self, fecha_vinculacion):
        """
        Método para establecer la fecha de vinculación del instructor contratado.
        """
        if fecha_vinculacion is not None:
            self._fecha_vinculacion = datetime.strptime(fecha_vinculacion, "%Y-%m-%d")
        else:
            self._fecha_vinculacion = None

    def informacion(self):
        """
        Método para imprimir la información del instructor contratado.
        """
        fecha_vinculacion_str = self.get_fecha_vinculacion().strftime("%Y-%m-%d") if self.get_fecha_vinculacion() is not None else 'N/A'
        print("El documento del instructor es {0}. El nombre es {1}. Su salario básico es {2}. Su profesión es {3}. La duración del contrato es {4} meses. La fecha de vinculación es {5}.".format(
            self.get_documento(),
            self.get_nombre(),
            self.get_salario_basico(),
            self.get_profesion(),
            self.get_duracion_contrato(),
            fecha_vinculacion_str
        ))

    def leer_datos(self):
        """
        Método para leer los datos del instructor contratado.
        """
        self.set_documento(input("Digite su documento: "))
        self.set_nombre(input("Digite su nombre: "))
        self.set_salario_basico(input("Digite su salario básico: "))
        self.set_profesion(input("Digite su profesión: "))
        self.set_duracion_contrato(input("Digite la duración de su contrato en meses: "))
        fecha_vinculacion = input("Digite en qué fecha se vinculó (YYYY-MM-DD): ")
        if fecha_vinculacion != '':
            self.set_fecha_vinculacion(fecha_vinculacion)

    def estado(self):
        """
        Método para obtener el estado del contrato del instructor contratado.
        """
        if self._fecha_vinculacion is None:
            return "Inactivo"
        fecha_fin = self._fecha_vinculacion + timedelta(days=int(self._duracion_contrato)*30)
        if datetime.now() <= fecha_fin:
            return "Activo"
        else:
            return "Inactivo"
    
    

class EtapaLectiva(Aprendiz):
    def __init__(self, documento, nombre_completo, ficha, programa, numero_trimestre, fecha_inicio, fecha_terminacion):
        super().__init__(documento, nombre_completo, ficha, programa)
        self._numero_trimestre = numero_trimestre
        self._fecha_inicio = fecha_inicio
        self._fecha_terminacion = fecha_terminacion

    def set_numero_trimestre(self, numero_trimestre):
        self._numero_trimestre = numero_trimestre

    def get_numero_trimestre(self):
        return self._numero_trimestre

    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def set_fecha_terminacion(self, fecha_terminacion):
        self._fecha_terminacion = fecha_terminacion

    def get_fecha_terminacion(self):
        return self._fecha_terminacion

    def informacion(self):
        print("El documento del aprendiz es {0} El nombre es {1} Su ficha es {2} El programa es {3} El trimestre es {4} La fecha de inicio es {5} La fecha de terminacion {6} ".format(
                                                                                    self.get_documento(),
                                                                                    self.get_nombre(),
                                                                                    self.get_ficha(),
                                                                                    self.get_programa(),
                                                                                    self.get_numero_trimestre(),
                                                                                    self.get_fecha_inicio(),
                                                                                    self.get_fecha_terminacion()))

    def estado(self):
        estados=["En induccion","En formacion","Aplazado","Condicionado", "retirado"]
        alt= randint(0,len(estados)-1)
        print("El estado del aprendiz es {0}".format(estados[alt]))

    def leer_datos(self):
        self._documento = input("Digite su documento: ")
        self._nombre_completo = input("Digite su nombre: ")
        self._ficha = input("Digite su numero de ficha: ")
        self._programa = input("Digite su programa: ")
        self._numero_trimestre = input("Digite en que trimestre se encuentra: ")
        self._fecha_inicio = input("Digite la fecha de inicio: ")
        self._fecha_terminacion = input("Digite la fecha en que termina su programa: ")

        

class EtapaPractica(Aprendiz):
    def __init__(self, documento, nombre_completo, ficha, programa, modalidad, fecha_inicio, fecha_terminacion):
        """
        Constructor de la clase EtapaPractica.
        """
        super().__init__(documento, nombre_completo, ficha, programa)
        self._modalidad = modalidad
        self._fecha_inicio = fecha_inicio
        self._fecha_terminacion = fecha_terminacion

    def set_modalidad(self, modalidad):
        """
        Establece la modalidad de la práctica.
        """
        self._modalidad = modalidad

    def get_modalidad(self):
        """
        Obtiene la modalidad de la práctica.
        """
        return self._modalidad

    def set_fecha_inicio(self, fecha_inicio):
        """
        Establece la fecha de inicio de la práctica.
        """
        self._fecha_inicio = fecha_inicio

    def get_fecha_inicio(self):
        """
        Obtiene la fecha de inicio de la práctica.
        """
        return self._fecha_inicio

    def set_fecha_terminacion(self, fecha_terminacion):
        """
        Establece la fecha de terminación de la práctica.
        """
        self._fecha_terminacion = fecha_terminacion

    def get_fecha_terminacion(self):
        """
        Obtiene la fecha de terminación de la práctica.
        """
        return self._fecha_terminacion

    def informacion(self):
        """
        Imprime la información del aprendiz.
        """
        print("El documento del aprendiz es {0} El nombre es {1} Su ficha es {2} El programa es {3} La modalidad es {4} La fecha de inicio es {5} La fecha de termnacion {6} ".format(
                                                                                    self.get_documento(),
                                                                                    self.get_nombre(),
                                                                                    self.get_ficha(),
                                                                                    self.get_programa(),
                                                                                    self.get_modalidad(),
                                                                                    self.get_fecha_inicio(),
                                                                                    self.get_fecha_terminacion()))
    
    def estado(self):
        """
        Imprime el estado del aprendiz.
        """
        estados=["En induccion","En formacion","Aplazado","Condicionado", "retirado"]
        alt= randint(0,len(estados)-1)
        print("El estado del aprendiz es {0}".format(estados[alt]))

    def leer_datos(self):
        """
        Lee los datos del aprendiz desde la entrada estándar.
        """
        self.set_documento(input("Digite su documento: "))
        self.set_nombre(input("Digite su nombre: "))
        self.set_ficha(input("Digite su numero de ficha: "))
        self.set_programa(input("Digite su programa: "))
        self.set_modalidad(input("Digite en que modalidad se encuentra: "))
        self.set_fecha_inicio(input("Digite en que fecha inicio: "))
        self.set_fecha_terminacion(input("Digite la fecha en que termina su programa: "))


instructorplanta = InstructorPlanta("","","","","","")

instructorplanta.leer_datos()
instructorplanta.informacion()
instructorplanta.estado()
instructorplanta.calcular_sueldo()

instructorcontrato = InstructorContrato("","","","","")

instructorcontrato.leer_datos()
instructorcontrato.informacion()
instructorcontrato.estado()

etapalectiva = EtapaLectiva("","","","","","","")

etapalectiva.leer_datos()
etapalectiva.informacion()
etapalectiva.estado()

etapapractica = EtapaPractica("","","","","","","")

etapapractica.leer_datos()
etapapractica.informacion()
etapapractica.estado()