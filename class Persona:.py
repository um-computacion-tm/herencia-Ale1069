class Persona:
    def __init__(self, el_nombre, el_email):
        self.nombre = el_nombre
        self.email = el_email

    def dame_tu_nombre(self):
        return self.nombre
    
    def xxx(self):
        if type

class Alumno(Persona):
    def __init__(self, el_nombre_del_alumno, el_email, cod_alumno):
        super().__init__(el_nombre_del_alumno, el_email)
        self.inasistencias = 0
        self.dieta = ""
        self.mentor = None
        self.cod_alumno = cod_alumno

    def dame_tu_nombre(self):
        return "CONFIDENCIAL"

    def mentoria(self, profesor):
        self.mentor = profesor

    def falta(self):
        self.inasistencias += 1

    def elegir_dieta_especial(self, la_dieta):
        self.dieta = la_dieta

    def es_vegano(self):
        self.dieta = "vegano"

    def esta_libre(self):
        if self.inasistencias >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"

class Profesor(Persona):
    pass

profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

print(profe_elio.dame_tu_nombre())
print(profe_gabi.dame_tu_nombre())

alumno_juan = Alumno("Juancito", "alumno_juan@um.com", 12345)
alumno_Maria = Alumno("Maria", "alumno_maria@um.com", 5478)
print(alumno_juan.dame_tu_nombre())

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())

alumno_Maria.elegir_dieta_especial("vegetariana")
print(alumno_Maria.dieta)
alumno_juan.es_vegano()
print(alumno_juan.dieta)

alumno_juan.mentoria(profe_elio)

print(alumno_juan.mentor)