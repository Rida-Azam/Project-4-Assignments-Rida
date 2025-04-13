import random
NUM_ROUNDS = 5

def main():
     print("Welcome to the High-Low Game!\n")

     print("------------------------------")

     your_score = 0

     for i in range(NUM_ROUNDS):
         print("Round",i+1)
         computer_no=random.randint(1,100)
         your_no=random.randint(1,100)

         print(f"Your number is : {your_no}")

         choice:str=input("Do you think your number is higher or lower than the computer's?:")

         while choice != "higher" and choice != "lower":
          choice = input("Please enter either higher or lower: ")

         higher_to_correct=choice == "higher" and your_no > computer_no
         lower_to_correct =choice == "lower" and your_no < computer_no    

         if higher_to_correct or lower_to_correct:
          print(f"You were right! The computer's number was :{ computer_no}")
          your_score += 1
         else:
          print(f"Aww that's incorrect. The computer's number was :{computer_no}")

         print(f"Your score is {your_score}\n")
  
     print(f"Your final score is: {your_score}")
     if your_score == NUM_ROUNDS:
      print("Wow! You played perfectly!!")
     elif your_score >= NUM_ROUNDS // 2:
      print("Good job, you played really well!")
     else:
      print("Better luck next time!")

if __name__ == '__main__':
   main()