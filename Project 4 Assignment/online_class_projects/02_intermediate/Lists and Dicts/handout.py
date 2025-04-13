
def access(lst,index):
  try:
      return lst[index]
  except IndexError:
      return "Index out of range."  

def modify(lst,index,new_value):
  try:
    lst[index]=new_value
    return lst
  except IndexError:
    return "Index out of range."

def slice(lst,start_index,end_index):
  try:
    return lst[start_index:end_index]
  except IndexError:
    return "Index out of range."

def index_game():
  lst=[1,2,3,4,5]
  operation=input("Select an operation (access, modify, slice):")

  if operation=="access":
    index=int(input("Enter the index:"))
    print(access(lst,index))

  elif operation=="modify":
    index=int(input("Enter the index:"))
    new_value=input("Enter the new value:")
    print(modify(lst,index,new_value))

  elif operation=="slice":
    start_index=int(input("Enter the start index:"))
    end_index=int(input("Enter the end index:"))
    print(slice(lst,start_index,end_index))
  else:
        print("Invalid operation.")

index_game()  