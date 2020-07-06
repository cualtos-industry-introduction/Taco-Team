from agenda import Agenda
from contacto import Contacto
# Contactos es un objeto que contiente la lsita de todos los contactos
Contactos = agenda.obtenerContactos()

def crear():
    nuevo_contacto = Contacto (input "Ingresa el nombre del contacto")
    nuevo_contacto.correo = input("Ingresa el correo el del contacto")
    nuevo_contacto.teleono = input("Ingresa el teléfono del contacto")
    nuevo_contacto.empresa = input("Ingresarla empresa para la que labora:")
    nuevo_contacto.nota = input("Ingresarla empresa para la que labora:")
    contactos.append (nuevo_contacto)
