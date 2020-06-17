# 1 Agregar contactos
# 2 Borrar contactos
# 3 Listar contactos
# 4 Buscar uno/unos contactos

from PhoneBookContact import PhoneBookContact
from PhoneBook import PhoneBook

agenda = PhoneBook()
agenda.add(PhoneBookContact("jose", "perez", 23232, "")) 
agenda.add(PhoneBookContact("jose1", "perez", 23232, "")) 
agenda.add(PhoneBookContact("jose2", "perez", 23232, "")) 
agenda.add(PhoneBookContact("ramon", "perez", 23232, "")) 
agenda.add(PhoneBookContact("lorenza", "perez", 23232, "")) 
agenda.add(PhoneBookContact("fran", "perez", 23232, "")) 


##########################
def agregar():
  nombre = input("\nindique el nombre: ")
  correo = input("\nindique el correo: ")
  telefono = int(input("\nindique el telefono: "))
  direccion = input("\nindique la direccion: ")

  contacto = PhoneBookContact(nombre, correo, telefono, direccion)
  agenda.add(contacto)

def listar():
  agenda.printAgenda()
  
def borrar():
  nombre = input("\nindique el nombre a buscar: ")
  lista = agenda.search(nombre)
  for i in lista:
    agenda.remove(i)
  
def buscar():
  nombre = input("\nindique el nombre a buscar: ")
  lista = agenda.search(nombre)
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