# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.


def main():
 try:
   print("!! This program add two numbers!!")
   num1=input("Enter the First Number:")
   num1:int=int(num1)
   num2=input("Enter the Second Number:")
   num2:int=int(num2)
   total:int=num1+num2 
   print(f"The sum of {num1} and {num2} is : {str(total)}")
 except ValueError:
   print("Invalid Input! Please  Enter Number Only")
main() 
