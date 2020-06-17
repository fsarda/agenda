class PhoneBookContact:
  name = ""
  phone = 0
  email = ""
  address = ""

  def __init__(self, name, phone, email, address):
    self.name = name
    self.phone = phone
    self.email = email
    self.address = address
  
  def __str__(self):
    return self.name+":\n"+ str(self.phone)+"\t"+ self.email+"\n___________________________________\n"

  def __eq__(self, value):
    return self.name == value.name and self.phone == value.phone and self.email == value.email and self.address == value.address

  def __gt__(self, value):
    return self.name > value.name or (self.name == value.name and self.phone > value.phone)
  
  def __lt__(self, value):
    return self.name < value.name or (self.name == value.name and self.phone < value.phone)

  def printMyAddress(self):
    print(self.address)