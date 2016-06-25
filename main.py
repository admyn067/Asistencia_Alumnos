import random

alumnos = []

"""""
ESTA FUNCION ES PARA UN REGISTRO DE ALUMNOS
"""

def agregarAlumno(nombre, edad, telefono = None, asistencia = 0):
    alumnos.append({
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono,
        "asistencia": asistencia
    })

nombres = ["Jose" , "maria" , "Ramiro" , "Thomas"]

for alumno in range(1, 10):
    alumno = nombres[random.randint(0, 3)]
    edad = random.randint(7, 19)

    agregarAlumno(edad=edad, nombre=alumno)

for alumno in alumnos:
    print("Nombre: {}: {}".format(
        alumno["nombre"], alumno["asistencia"]))



