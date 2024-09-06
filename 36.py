hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]
umbral = 100

def analizar_tendencias(hashtags, tendencias, umbral):
    conteo_hashtags = {}
    for hashtag in hashtags:
        if hashtag in conteo_hashtags:
            conteo_hashtags[hashtag] += 1
        else:
            conteo_hashtags[hashtag] = 1
    frecuencias_tendencias = dict(tendencias)
    hashtags_filtrados = []
    for hashtag, frecuencia in conteo_hashtags.items():
        if hashtag in frecuencias_tendencias and frecuencias_tendencias[hashtag] > umbral:
            hashtags_filtrados.append(hashtag)

    return hashtags_filtrados
resultados = analizar_tendencias(hashtags, tendencias, umbral)
print(resultados)