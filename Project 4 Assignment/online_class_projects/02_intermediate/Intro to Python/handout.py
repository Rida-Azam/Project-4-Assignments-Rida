def main():
  earth_weight=float(input("Enter a weight on Earth:"))
  planet_name=input("Enter a planet:")
  if planet_name=="Mars":
    gravity=earth_weight*0.378
  elif planet_name=="Venus":
    gravity=earth_weight*0.889
  elif planet_name=="Mercury":
    gravity=earth_weight*0.376
  elif planet_name=="Jupiter":
    gravity=earth_weight*236.0
  elif planet_name =="Neptune":
    gravity=earth_weight*1.14
  elif planet_name=="Saturn":
    gravity=earth_weight*1.081

  print(f"The equivalent weight on {planet_name}: {round(gravity,2)}")


if __name__ == '__main__':
    main()
