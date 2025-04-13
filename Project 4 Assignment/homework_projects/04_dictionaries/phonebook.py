# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_number():

  phonebook={}

  while True:
    name = input(" Name: ")
    if name=="":
      break
    number =input("Number: ")
    phonebook[name]=number
  return phonebook


def print_phone(phonebook):
  for name in phonebook:
    print(f"{name} -> {phonebook[name]}")

def lookup(phonebook):
  while True:
    name=input("Enter a name for lookup:")
    if name == "":
     break

    if name not in phonebook:
      print(f"{name} is not in a phonebook")
    else:
      print(phonebook[name])


def main():
  phonebook=read_phone_number()
  print_phone(phonebook)
  lookup(phonebook)

if __name__=="__main__":
  main()
