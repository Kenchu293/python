productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]
def lista(productos):

    if productos[0][1] >productos[1][1] and productos[0][1] >productos[2][1]: producto_preciomayor=productos[0][0]
    if productos[1][1] > productos[0][1] and productos[1][1] > productos[2][1]: producto_preciomayor=productos[1][0]
    if productos[2][1] > productos[1][1] and productos[2][1] > productos[0][1]: producto_preciomayor=productos[2][0]
    return producto_preciomayor
llamada=lista(productos)
print(llamada)

