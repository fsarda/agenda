from PhoneBook import PhoneBook
from PhoneBookContact import PhoneBookContact
import random

# Genera 'limit' cantidad de contactos y los inserta en 'agenda'

def generarAgenda(agenda, limit = 100):
  names = ["lorenza", "amalia", "daniela", "pedro", "luis", "jose"]
  lastname = ["perez", "sarda", "rodriguez", "sanchez", "silva", "pasca"]
  numbers = range(6000000, 6999999)

  for i in range(limit):
    name = str(random.choice(names)).capitalize()+" "+str(random.choice(lastname)).capitalize().swapcase()
    correo = name.replace(" ","_")+str(i)+"@gmail.com"
    agenda.add(PhoneBookContact(name,random.choice(numbers),correo,"")) 
