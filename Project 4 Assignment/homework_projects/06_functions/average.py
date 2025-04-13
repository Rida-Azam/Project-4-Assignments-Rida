# Write a function that takes two numbers and finds the average between the two.

def average(a:float,b:float):
    sum=a+b
    avg=sum/2
    return avg
def main():
  avg1=average(10,8)
  avg2=average(0,8)
  final=average(avg1,avg2)

  print("Average 1",avg1)
  print("Average 2",avg2)
  print("Final",final)

if __name__=="__main__":
 main()