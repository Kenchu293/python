ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
def analizar_ventas(ventas):
    #comprobamos si tiene elementos la lista
    if not ventas:
        return {
            "Total de Ventas": 0,
            "Promedio Mensual": 0,
            "Mes con Mayores Ventas": None
        }
    total_ventas = sum(ventas)
    promedio_mensual = total_ventas / len(ventas)
    mes_maximo = ventas.index(max(ventas)) + 1
    resultado = {
        "Total de Ventas": total_ventas,
        "Promedio Mensual": promedio_mensual,
        "Mes con Mayores Ventas": mes_maximo
    }
    return resultado
resultado_ventas = analizar_ventas(ventas_mensuales)
print(resultado_ventas)