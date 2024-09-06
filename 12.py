estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}
def promedio_estudiante(estudiantes, matricula):
    if matricula in estudiantes:
        calificaciones = estudiantes[matricula]["calificaciones"].values()
        promedio = sum(calificaciones) / len(calificaciones)
        return promedio
    else:
        return "Estudiante no encontrado."


matricula = 102
print(promedio_estudiante(estudiantes, matricula))