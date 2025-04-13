# Problem Statement

# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def main():
  for i in range(10):
    if is_odd(i):
      print(f"{i} odd")
    else:
      print(f"{i} even")

def is_odd(num):
  if num%2==0:
    return False
  return True

if __name__=="__main__":
  main()