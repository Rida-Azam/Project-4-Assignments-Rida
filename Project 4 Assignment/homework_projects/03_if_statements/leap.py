# # Write a program that reads a year from the user and tells whether a given year is a leap year or not.

def main():
    year=int(input("Enter a year you want to check : "))


    if year % 4 == 0:  
        if year % 100 == 0:  
            if year % 400 == 0:  
                print("That's a leap year!")

            else: 
                print("That's not a leap year.")
        else:  
            print("That's a leap year!")
    else: 
        print("That's not a leap year.")

        



if __name__ == "__main__":
    main()       


