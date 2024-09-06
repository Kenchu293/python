usuarios = ["Ana", "Luis", "María"]
def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}

    for usuario in usuarios:
        configuraciones = [f"{clave}: {valor}" for clave, valor in kwargs.items()]
        perfiles[usuario] = configuraciones

    return perfiles
configuraciones_perfiles = configurar_perfiles(
    usuarios,
    idioma="es",
    modo_oscuro=True,
    notificaciones=False
)

print(configuraciones_perfiles)