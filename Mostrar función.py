
def mostrar_contactos():
    for id, contacto in enumerate(contactos):
        print("ID: ", id, "=", "Nombre:", contacto.nombre, "Empresa:",contacto.empresa, "Correo:",contacto.correo, "Teléfono:",contacto.telefono, "Nota:", contacto.nota)
        print("-" * 15)
            
            