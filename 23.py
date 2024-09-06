def organizar_eventos(*eventos):
    for i, evento in enumerate(eventos, 1):
        print(f"{i}. {evento}")
organizar_eventos("Concierto", "Exposición de arte", "Conferencia")