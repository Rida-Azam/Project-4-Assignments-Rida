def get_user_data():
  first_name:str=input("What is your first name?:")
  last_name:str=input("What is your last name?:")
  email:str=input("What is your email address?:")
  return first_name, last_name, email

def main():
  user_data=get_user_data()
  print("Recived data from user",user_data)

if __name__=="__main__":
  main()