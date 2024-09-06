puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
def ordenar_por_puntuacion(puntuaciones):
    puntuaciones.sort(key=lambda x: x[1], reverse=True)
    return puntuaciones
resultado = ordenar_por_puntuacion(puntuaciones)
print(resultado)