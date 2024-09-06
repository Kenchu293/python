reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}
def hacer_reserva(fecha, nombre_huesped, habitacion, precio, reservas):

    if fecha not in reservas:
        reservas[fecha] = []
    for huesped, hab, precio in reservas[fecha]:
        if hab == habitacion:
            return f"La habitación {habitacion} ya está ocupada en la fecha {fecha}."
    reservas[fecha].append((nombre_huesped, habitacion, precio))

    return f"Reserva confirmada para {nombre_huesped} en la habitación {habitacion} para la fecha {fecha}."

resultado = hacer_reserva("2024-08-15", "Carlos", 103, 200, reservas)
print(resultado)
