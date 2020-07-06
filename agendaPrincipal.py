from agenda import Agenda
from contacto import Contacto

opcion = "si"
agenda = Agenda('agenda')

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
    elif opcion == "2":
        print("\n", 15*"-", "Buscar Contacto", 15*"-")
    elif opcion == "3":
        print("\n", 15*"-", "Mostrar todo", 15*"-")
    elif opcion == "4":
        print("\n", 15*"-", "Borrar Contacto", 15*"-")
    elif opcion == "5":
        print("\n", 15*"-", "Actualizar Contacto", 15*"-")
    elif opcion in ["salir", "no", "6"]:
        print("\nGracias por utilizar el programa")
        exit()
    else:
        print("\nOpción no válida\n")

if __name__ == "__main__":
    while(opcion != "no"):
        menu()
        opciones()