encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}
def calcular_frecuencias(encuestas):
    frecuencias = {}

    for pregunta, respuestas in encuestas.items():
        conteo_respuestas = {}
        for respuesta in respuestas:
            if respuesta in conteo_respuestas:
                conteo_respuestas[respuesta] += 1
            else:
                conteo_respuestas[respuesta] = 1
        frecuencias[pregunta] = conteo_respuestas
    return frecuencias
resultados_frecuencias = calcular_frecuencias(encuestas)
print(resultados_frecuencias)
