precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]
def calcular_beneficio(precios_diarios, operaciones):
    beneficio_total = 0
    precio_compra = None
    for operacion, dia in operaciones:
        precio_dia = precios_diarios[dia]
        if operacion == "compra":
            precio_compra = precio_dia
        elif operacion == "venta":
            if precio_compra is not None:
                beneficio_total += precio_dia - precio_compra
                precio_compra = None
            else:
                return "Error: Intento de venta sin una compra registrada."
    return beneficio_total
beneficio = calcular_beneficio(precios_diarios, operaciones)
print(f"Beneficio o pérdida total: {beneficio}")