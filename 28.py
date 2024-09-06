notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]
def calcular_promedios(notas):
    promedios = {}

    for nombre, calificaciones in notas:
        promedio = sum(calificaciones) / len(calificaciones)
        promedios[nombre] = promedio
    return promedios
promedios_estudiantes = calcular_promedios(notas_estudiantes)
print(promedios_estudiantes)