class PhoneBook:
  def __init__(self):
    self.phonelist = []

  def add(self, contacto):
    self.phonelist.append(contacto)
  
  def search(self, name):
    return filter(lambda i: i.name == name, self.phonelist)

  def remove(self, contact):
    self.phonelist.remove(contact)

  def __str__(self):
    response = "Agenda:\n"
    for i in self.phonelist:
      response +=  str(i)
    return response
  
  def printAgenda(self):
    print("Agenda:\n")
    for i in self.phonelist:
      print(i)