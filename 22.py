inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]
def actualizar_inventario(inventario, ventas):
    for x in range(len(inventario)):
        # Restamos las ventas del inventario
        inventario[x] -= ventas[x]
    return inventario
inventario_actualizado = actualizar_inventario(inventario, ventas)
print(inventario_actualizado)