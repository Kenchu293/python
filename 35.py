inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizar_inventario(inventario, tienda, **kwargs):
    if tienda not in inventario:
        return "La tienda no existe en el inventario."
    productos = inventario[tienda]
    for producto, cantidad in kwargs.items():
        if producto in productos:
            productos[producto] += cantidad
            if productos[producto] < 0:
                productos[producto] = 0
        else:
            return f"El producto {producto} no existe en la tienda {tienda}."
    return inventario
estado_inventario = actualizar_inventario(
    inventario,
    "Tienda A",
    producto_1=10,
    producto_2=-5
)

print(estado_inventario)