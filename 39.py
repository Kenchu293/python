estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}
def calcular_ranking(estudiantes):
    promedios = {}
    for id_estudiante, materias in estudiantes.items():
        suma_total = 0
        cantidad_calificaciones = 0
        for calificaciones in materias.values():
            suma_total += sum(calificaciones)
            cantidad_calificaciones += len(calificaciones)
        promedio_general = suma_total / cantidad_calificaciones
        promedios[id_estudiante] = promedio_general
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    return ranking
ranking = calcular_ranking(estudiantes)
print("Ranking de estudiantes basado en el promedio general:")
for id_estudiante, promedio in ranking:
    print(f"ID: {id_estudiante}, Promedio General: {promedio:.2f}")