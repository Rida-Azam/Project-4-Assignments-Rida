# Print 10 random numbers in the range 1 to 100.

import random
N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
  
  for i in range(N_NUMBERS):
     print(random.randint(MIN_VALUE,MAX_VALUE) ,end=',')

if __name__ == '__main__':
    main()