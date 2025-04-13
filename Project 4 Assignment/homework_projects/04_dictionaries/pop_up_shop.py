# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

def main():
  fruits={'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

  total=0
  for fruit_name in fruits:
    price=fruits[fruit_name]
    buy_amount=int(input(f"How many ({fruit_name}) do you want?: "))
    total+=price*buy_amount

  print(f"Your total is ${total}")

if __name__=="__main__":
  main()