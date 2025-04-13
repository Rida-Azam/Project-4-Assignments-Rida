# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

Inches_In_Foot:int=12

def main():
  feet:float=float(input("Enter number of feet :"))
  inches:float=Inches_In_Foot*feet
  print(f"That is inches :{inches}")

main()  
