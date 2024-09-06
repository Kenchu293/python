suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}
def actualizar_suscripcion(suscripciones, usuario, suscripcion, **opciones_adicionales):
    if usuario not in suscripciones:
        suscripciones[usuario] = []
    if suscripcion not in suscripciones[usuario]:
        suscripciones[usuario].append(suscripcion)

    return suscripciones
estado_actualizado = actualizar_suscripcion(
    suscripciones,
    usuario="Luis",
    suscripcion="mensual",
    auto_renovacion=True
)

print(estado_actualizado)