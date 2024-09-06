temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
def analisis_temperaturas(temperaturas):
    temperatura_media = sum(temperaturas) / len(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    return round(temperatura_media), temperatura_maxima, temperatura_minima

media, maxima, minima = analisis_temperaturas(temperaturas)

print(f"Temperatura media: {media}\n "+f"Temperatura máxima: {maxima}\n "+f"Temperatura mínima: {minima}\n")
