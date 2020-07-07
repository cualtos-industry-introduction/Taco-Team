from agenda import Agenda
from contacto import Contacto

opcion = "si"
agenda = Agenda('agenda')
contactos = agenda.obtenerContactos()


def menu():
    print("\n", 18*"_", "MENÚ", 18*"_")
    print("\t1.- Agregar contacto")
    print("\t2.- Buscar contacto")
    print("\t3.- Mostrar todo")
    print("\t4.- Borrar")
    print("\t5.- Actualizar")
    print("\t6.- Salir")

def opciones():
    opcion = input("\t   : ")
    if opcion == "1":
        print("\n", 15*"-", "Agregar Contacto", 15*"-")
        agregar()
        agenda.agregarContactos(contactos)
        agenda.guardar()
    elif opcion == "2":
        print("\n", 15*"-", "Buscar Contacto", 15*"-")
        contactobuscar=input("nombre a buscar: ")
        busquedacotaco={}
        busquedacotaco=agenda.obtenerContacto(contactobuscar)
        print(busquedacotaco)
    elif opcion == "3":
        print("\n", 15*"-", "Mostrar todo", 15*"-")
        mostrar_contactos()
    elif opcion == "4":
        print("\n", 15*"-", "Borrar Contacto", 15*"-")
    elif opcion == "5":
        print("\n", 15*"-", "Actualizar Contacto", 15*"-")
    elif opcion in ["salir", "no", "6"]:
        print("\nGracias por utilizar el programa")
        exit()
    else:
        print("\nOpción no válida\n")
def agregar():
    nuevo_contacto = Contacto (input("Ingresa el nombre del contacto: "))
    nuevo_contacto.correo = input("Ingresa el correo el del contacto: ")
    nuevo_contacto.teleono = input("Ingresa el teléfono del contacto: ")
    nuevo_contacto.empresa = input("Ingresarla empresa para la que labora: ")
    nuevo_contacto.nota = input("Ingresar nota del contacto: ")
    contactos.append(nuevo_contacto)
 
def mostrar_contactos():
    for id, contacto in enumerate(contactos):
        print("ID: ", id, "=", "Nombre:", contacto.nombre, "Empresa:",contacto.empresa, "Correo:",contacto.correo, "Teléfono:",contacto.telefono, "Nota:", contacto.nota)
        print("-" * 15)
3

if __name__ == "__main__":
    while(opcion != "no"):
        menu()
        opciones()
