def configurar(**kwargs):
    configuraciones = {
        "modo_oscuro": False,
        "idioma": "en",
        "notificaciones": True
    }
    configuraciones.update(kwargs)
    return configuraciones
config = configurar(modo_oscuro=True, idioma="es", notificaciones=False)
print(config)