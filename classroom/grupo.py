from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = [estudiantes]
        
    def __str__(self):
        cadena = "Grupo de estudiantes: grupo predeterminado"
        return cadena

    def listadoAsignaturas(self, *args, **kwargs):
        self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista=[]
            lista.append(alumno)
            self.listadoAlumnos = lista
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista
            
            
    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

