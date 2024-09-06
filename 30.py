
def publicar(nombre_usuario, texto_publicacion, etiquetas=[], **opciones_adicionales):
    publicacion = {
        "Usuario": nombre_usuario,
        "Texto": texto_publicacion,
        "Etiquetas": etiquetas
    }
    publicacion.update(opciones_adicionales)
    return publicacion

detalle_publicacion = publicar(
    "Juan",
    "Mi primer post!",
    etiquetas=["#hola", "#primerPost"],
    visibilidad="publica",
    likes=100
)

print(detalle_publicacion)