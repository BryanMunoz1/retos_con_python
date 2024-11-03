# *****
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz: Bryan Muñoz
# Version: Python312
# Fecha: 12/06/2024
# *****

class Persona:
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato):
        self.__id_persona = id_persona
        self.__nom_persona = nom_persona
        self.__ape_persona = ape_persona
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad_nacimiento = ciudad_nacimiento
        self.__genero = genero
        self.__estrato = estrato

    # Getters
    def get_id_persona(self):
        return self.__id_persona

    def get_nom_persona(self):
        return self.__nom_persona

    def get_ape_persona(self):
        return self.__ape_persona

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_ciudad_nacimiento(self):
        return self.__ciudad_nacimiento

    def get_genero(self):
        return self.__genero

    def get_estrato(self):
        return self.__estrato

    # Setters
    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona

    def set_nom_persona(self, nom_persona):
        self.__nom_persona = nom_persona

    def set_ape_persona(self, ape_persona):
        self.__ape_persona = ape_persona

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_ciudad_nacimiento(self, ciudad_nacimiento):
        self.__ciudad_nacimiento = ciudad_nacimiento

    def set_genero(self, genero):
        self.__genero = genero

    def set_estrato(self, estrato):
        self.__estrato = estrato

    def mostrar_dg(self):
        return f"ID: {self.__id_persona}, Nombre: {self.__nom_persona}, Apellido: {self.__ape_persona}, Fecha de Nacimiento: {self.__fecha_nacimiento}, Ciudad de Nacimiento: {self.__ciudad_nacimiento}, Género: {self.__genero}, Estrato: {self.__estrato}"

    def calcula_eps(self):
        return f"EPS calculada para {self.__nom_persona} {self.__ape_persona}"

    def calcula_pension(self):
        return f"Pensión calculada para {self.__nom_persona} {self.__ape_persona}"

    def calcula_arl(self):
        return f"ARL calculada para {self.__nom_persona} {self.__ape_persona}"

    def calcula_sena(self):
        return f"SENA calculado para {self.__nom_persona} {self.__ape_persona}"

    def calcula_cajas(self):
        return f"Cajas de compensación calculadas para {self.__nom_persona} {self.__ape_persona}"

    def calcula_icbf(self):
        return f"ICBF calculado para {self.__nom_persona} {self.__ape_persona}"


class Docentes(Persona):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, area_formacion, titulo_profesional, unidad_academica):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato)
        self.__area_formacion = area_formacion
        self.__titulo_profesional = titulo_profesional
        self.__unidad_academica = unidad_academica

    # Getters
    def get_area_formacion(self):
        return self.__area_formacion

    def get_titulo_profesional(self):
        return self.__titulo_profesional

    def get_unidad_academica(self):
        return self.__unidad_academica

    # Setters
    def set_area_formacion(self, area_formacion):
        self.__area_formacion = area_formacion

    def set_titulo_profesional(self, titulo_profesional):
        self.__titulo_profesional = titulo_profesional

    def set_unidad_academica(self, unidad_academica):
        self.__unidad_academica = unidad_academica

    def mostrar_datos_docente(self):
        return f"Área de Formación: {self.__area_formacion}, Título Profesional: {self.__titulo_profesional}, Unidad Académica: {self.__unidad_academica}"

    def calcular_sueldo(self):
        return "Método calcular_sueldo debe ser implementado en las subclases."


class TiempoCompleto(Docentes):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, area_formacion, titulo_profesional, unidad_academica, categoria, salario):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, area_formacion, titulo_profesional, unidad_academica)
        self.__categoria = categoria
        self.__salario = salario

    # Getters
    def get_categoria(self):
        return self.__categoria

    def get_salario(self):
        return self.__salario

    # Setters
    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_sueldo(self):
        return self.__salario

    def liquidar_tc(self):
        return f"Liquidación de Tiempo Completo: {self.__nom_persona} {self.__ape_persona}, Salario: {self.__salario}"

    def mostrar_liqtc(self):
        return f"ID: {self.get_id_persona()}, Nombre: {self.get_nom_persona()}, Apellido: {self.get_ape_persona()}, Salario: {self.__salario}, Categoría: {self.__categoria}, Unidad Académica: {self.get_unidad_academica()}"


class Ocasionales(Docentes):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, area_formacion, titulo_profesional, unidad_academica, ultimo_titulo, num_meses, salario):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, area_formacion, titulo_profesional, unidad_academica)
        self.__ultimo_titulo = ultimo_titulo
        self.__num_meses = num_meses
        self.__salario = salario

    # Getters
    def get_ultimo_titulo(self):
        return self.__ultimo_titulo

    def get_num_meses(self):
        return self.__num_meses

    def get_salario(self):
        return self.__salario

    # Setters
    def set_ultimo_titulo(self, ultimo_titulo):
        self.__ultimo_titulo = ultimo_titulo

    def set_num_meses(self, num_meses):
        self.__num_meses = num_meses

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_sueldo(self):
        return self.__salario

    def liquidar_oc(self):
        return f"Liquidación de Ocasional: {self.__nom_persona} {self.__ape_persona}, Salario: {self.__salario}"

    def mostrar_liqoc(self):
        return f"ID: {self.get_id_persona()}, Nombre: {self.get_nom_persona()}, Apellido: {self.get_ape_persona()}, Salario: {self.__salario}, Último Título: {self.__ultimo_titulo}, Meses: {self.__num_meses}, Unidad Académica: {self.get_unidad_academica()}"


class HoraCatedra(Docentes):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, area_formacion, titulo_profesional, unidad_academica, num_horas, valor_contrato):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, area_formacion, titulo_profesional, unidad_academica)
        self.__num_horas = num_horas
        self.__valor_contrato = valor_contrato

    # Getters
    def get_num_horas(self):
        return self.__num_horas

    def get_valor_contrato(self):
        return self.__valor_contrato

    # Setters
    def set_num_horas(self, num_horas):
        self.__num_horas = num_horas

    def set_valor_contrato(self, valor_contrato):
        self.__valor_contrato = valor_contrato

    def calcular_sueldo(self):
        return self.__num_horas * (self.__valor_contrato / self.__num_horas)

    def liquidar_hc(self):
        return f"Liquidación de Hora Cátedra: {self.__nom_persona} {self.__ape_persona}, Salario: {self.calcular_sueldo()}"

    def mostrar_liqhc(self):
        return f"ID: {self.get_id_persona()}, Nombre: {self.get_nom_persona()}, Apellido: {self.get_ape_persona()}, Horas: {self.__num_horas}, Valor Contrato: {self.__valor_contrato}, Unidad Académica: {self.get_unidad_academica()}"


class Administrativos(Persona):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato)
        self.__dependencia = dependencia
        self.__titulo = titulo

    # Getters
    def get_dependencia(self):
        return self.__dependencia

    def get_titulo(self):
        return self.__titulo

    # Setters
    def set_dependencia(self, dependencia):
        self.__dependencia = dependencia

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def mostrar_datos_admin(self):
        return f"Dependencia: {self.__dependencia}, Título: {self.__titulo}"

    def calcular_cajas(self):
        return f"Cajas de compensación calculadas para {self.get_nom_persona()} {self.get_ape_persona()}"

    def calcular_icbf(self):
        return f"ICBF calculado para {self.get_nom_persona()} {self.get_ape_persona()}"


class Planta(Administrativos):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo, fecha_vinculacion):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo)
        self.__fecha_vinculacion = fecha_vinculacion

    # Getters
    def get_fecha_vinculacion(self):
        return self.__fecha_vinculacion

    # Setters
    def set_fecha_vinculacion(self, fecha_vinculacion):
        self.__fecha_vinculacion = fecha_vinculacion

    def mostrar_datos_admin_planta(self):
        return f"{self.mostrar_datos_admin()}, Fecha de Vinculación: {self.__fecha_vinculacion}"

    def liquidar_valor_contrato(self):
        return f"Liquidación de contrato para {self.get_nom_persona()} {self.get_ape_persona()}"

    def mostrar_liqops(self):
        return f"{self.mostrar_datos_admin_planta()}, Liquidación: {self.liquidar_valor_contrato()}"


class OPS(Administrativos):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo, fecha_vinculacion, num_meses, valor_contrato):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo)
        self.__fecha_vinculacion = fecha_vinculacion
        self.__num_meses = num_meses
        self.__valor_contrato = valor_contrato

    # Getters
    def get_fecha_vinculacion(self):
        return self.__fecha_vinculacion

    def get_num_meses(self):
        return self.__num_meses

    def get_valor_contrato(self):
        return self.__valor_contrato

    # Setters
    def set_fecha_vinculacion(self, fecha_vinculacion):
        self.__fecha_vinculacion = fecha_vinculacion

    def set_num_meses(self, num_meses):
        self.__num_meses = num_meses

    def set_valor_contrato(self, valor_contrato):
        self.__valor_contrato = valor_contrato

    def liquidar_valor_contrato(self):
        return f"Liquidación de contrato por {self.__valor_contrato} para {self.__num_meses} meses"

    def mostrar_liqops(self):
        return f"{self.mostrar_datos_admin()}, Fecha de Vinculación: {self.__fecha_vinculacion}, Valor del Contrato: {self.__valor_contrato}, Meses: {self.__num_meses}"

class Auxiliar(Administrativos):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo, nivel, salario):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo)
        self.__nivel = nivel
        self.__salario = salario

    # Getters
    def get_nivel(self):
        return self.__nivel

    def get_salario(self):
        return self.__salario

    # Setters
    def set_nivel(self, nivel):
        self.__nivel = nivel

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_sueldo(self):
        return self.__salario

    def liquidar_aux(self):
        return f"Liquidación de Auxiliar: {self.__nom_persona} {self.__ape_persona}, Salario: {self.__salario}"

    def mostrar_liqaux(self):
        return f"ID: {self.get_id_persona()}, Nombre: {self.get_nom_persona()}, Apellido: {self.get_ape_persona()}, Salario: {self.__salario}, Dependencia: {self.get_dependencia()}, Título: {self.get_titulo()}, Nivel: {self.__nivel}"


class Tecnico(Administrativos):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo, nivel, salario):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo)
        self.__nivel = nivel
        self.__salario = salario

    # Getters
    def get_nivel(self):
        return self.__nivel

    def get_salario(self):
        return self.__salario

    # Setters
    def set_nivel(self, nivel):
        self.__nivel = nivel

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_sueldo(self):
        return self.__salario

    def liquidar_tec(self):
        return f"Liquidación de Técnico: {self.__nom_persona} {self.__ape_persona}, Salario: {self.__salario}"

    def mostrar_liqtec(self):
        return f"ID: {self.get_id_persona()}, Nombre: {self.get_nom_persona()}, Apellido: {self.get_ape_persona()}, Salario: {self.__salario}, Dependencia: {self.get_dependencia()}, Título: {self.get_titulo()}, Nivel: {self.__nivel}"


class Profesional(Administrativos):
    def __init__(self, id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo, nivel, salario):
        super().__init__(id_persona, nom_persona, ape_persona, fecha_nacimiento, ciudad_nacimiento, genero, estrato, dependencia, titulo)
        self.__nivel = nivel
        self.__salario = salario

    # Getters
    def get_nivel(self):
        return self.__nivel

    def get_salario(self):
        return self.__salario

    # Setters
    def set_nivel(self, nivel):
        self.__nivel = nivel

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_sueldo(self):
        return self.__salario

    def liquidar_prof(self):
        return f"Liquidación de Profesional: {self.__nom_persona} {self.__ape_persona}, Salario: {self.__salario}"

    def mostrar_liqprof(self):
        return f"ID: {self.get_id_persona()}, Nombre: {self.get_nom_persona()}, Apellido: {self.get_ape_persona()}, Salario: {self.__salario}, Dependencia: {self.get_dependencia()}, Título: {self.get_titulo()}, Nivel: {self.__nivel}"
    

    # Instancias de Docentes
docente1 = Docentes(
    id_persona=1, nom_persona="Carlos", ape_persona="Gonzalez",
    fecha_nacimiento="1980-01-01", ciudad_nacimiento="Bogotá", genero="M",
    estrato=3, area_formacion="Biología", titulo_profesional="Biólogo",
    unidad_academica="Ciencias Naturales"
)

# Instancias de Administrativos
admin1 = Administrativos(
    id_persona=2, nom_persona="Laura", ape_persona="Martinez",
    fecha_nacimiento="1975-05-12", ciudad_nacimiento="Medellín", genero="F",
    estrato=4, dependencia="Recursos Humanos", titulo="Administradora de Empresas"
)

# Instancias de Planta
planta1 = Planta(
    id_persona=3, nom_persona="Juan", ape_persona="Perez",
    fecha_nacimiento="1985-03-23", ciudad_nacimiento="Cali", genero="M",
    estrato=3, dependencia="TI", titulo="Ingeniero de Sistemas",
    fecha_vinculacion="2010-07-01"
)

# Instancias de OPS
ops1 = OPS(
    id_persona=4, nom_persona="Ana", ape_persona="Ramirez",
    fecha_nacimiento="1990-10-15", ciudad_nacimiento="Cartagena", genero="F",
    estrato=2, dependencia="Marketing", titulo="Publicista",
    fecha_vinculacion="2022-01-01", num_meses=6, valor_contrato=3000000
)

# Mostrar datos y realizar cálculos
print(docente1.mostrar_dg())
print(docente1.mostrar_datos_docente())

print(admin1.mostrar_dg())
print(admin1.mostrar_datos_admin())
print(admin1.calcular_cajas())
print(admin1.calcular_icbf())

print(planta1.mostrar_dg())
print(planta1.mostrar_datos_admin_planta())
print(planta1.liquidar_valor_contrato())
print(planta1.mostrar_liqops())

print(ops1.mostrar_dg())
print(ops1.mostrar_liqops())
print(ops1.liquidar_valor_contrato())
