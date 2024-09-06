def calcular_promedio(*args):
    promedio = sum(args) / len(args)
    return promedio
resultado = calcular_promedio(85, 90, 78, 92)
print(f"El promedio es: {resultado}")