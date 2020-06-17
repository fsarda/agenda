# 1 Agregar contactos
# 2 Borrar contactos
# 3 Listar contactos
# 4 Buscar uno/unos contactos

from PhoneBookContact import PhoneBookContact
from PhoneBook import PhoneBook
from util import generarAgenda

agenda = PhoneBook()
generarAgenda(agenda, 150)


##########################
def agregar():
  telefono = int(input("\nindique el telefono: "))
  nombre = input("\nindique el nombre: ")
  correo = input("\nindique el correo: ")
  direccion = input("\nindique la direccion: ")

  contacto = PhoneBookContact(nombre, correo, telefono, direccion)
  agenda.add(contacto)

def listar():
  print(agenda)
  
def borrar():
  nombre = input("\nindique el nombre a buscar: ")
  lista = agenda.search(nombre)
  for i in lista:
    agenda.remove(i)
  
def buscar():
  texto = input("\nindique el nombre a buscar: ")
  lista = agenda.search(texto)
  for i in lista:
    print(i)
  

eleccion = input("Que quieres hacer \n 1 agregar contacto \n 2 borrar contacto \n 3 listar contactos \n 4 buscar contactos\n")

while eleccion != "salir":
  if eleccion == "1":
    agregar()

  if eleccion == "3":
    listar()

  if eleccion == "2":
    borrar()

  if eleccion == "4":
    buscar()

  eleccion = input("Que quieres hacer \n 1 agregar contacto \n 2 borrar contacto \n 3 listar contactos \n 4 buscar contactos\n ")