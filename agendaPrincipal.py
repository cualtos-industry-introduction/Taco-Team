from agenda import Agenda
from contacto import Contacto

def menu():
    print("_______________MENÚ_____________")
    print("Agregar contactos")
    print("Ver contacto")
    print("Mostrar todo")
    print("Borrar")
    print("Aactualizar")


op = "si"

if __name__ == "__main__":
    while(op != "no"):
        op = input("Escribe la acción a realizar:\n\t1.- Agregar\n\t2.- Mostrar todo\n\t3.- Buscar\n\t4.- Salir\n\t   : ")
        if op == "1":
            print("Contacto agregado\n")
        elif op == "2":
        elif op in ["salir", "no", "4"]:
            print("\nAdiós, bye")
            exit()
        else:
            print("\nOpción no válida\n")