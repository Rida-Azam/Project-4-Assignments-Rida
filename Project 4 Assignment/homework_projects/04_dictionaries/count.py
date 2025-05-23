# This program counts the number of times each number appears in a list. 
# It uses a dictionary to keep track of the information.


def get_user_input():

   user_number=[]

   while True:
    user_input=input("Enter a number:")

    if user_input=="":
      break

    num = int(user_input)
    user_number.append(num)

   return user_number

def count_nums(num_lst):

  num_dict={}
  for num in num_lst:
    if num not in num_dict:
      num_dict[num]=1
    else:
      num_dict[num]+=1

  return num_dict

def print_count(num_dict):
  for num in num_dict:
      print(f"{num}  appears {num_dict[num]} times.")

def main():
  user_number=get_user_input()
  num_dict=count_nums(user_number)
  print_count(num_dict)

if __name__=="__main__":
  main()
