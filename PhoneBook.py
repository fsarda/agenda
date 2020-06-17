class PhoneBook:
  def __init__(self):
    self.phonelist = []

  def add(self, contacto):
    self.phonelist.append(contacto)
  
  def search(self, texto):
    return filter(lambda i: texto.lower() in i.name.lower(), self.phonelist)

  def remove(self, contact):
    self.phonelist.remove(contact)

  def __str__(self):
    response = "Agenda:\n"
    self.phonelist.sort()

    for i in self.phonelist:
      response +=  str(i) + "\n"
    return response
  
  def printAgenda(self):
    print("Agenda:\n")
    for i in self.phonelist:
      print(i)