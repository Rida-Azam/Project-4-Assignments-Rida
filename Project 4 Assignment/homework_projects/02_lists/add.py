# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_number(numbers)->int:

    total:int=0
    for number in numbers:
        total+=number
    return total

def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]  # Make a list of numbers
    sum_of_numbers: int = add_many_number(numbers)  # Find the sum of the list
    print(f"the sum of numbers are : {sum_of_numbers}")

main()        
