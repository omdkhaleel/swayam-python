def dconvert():
  try:
    inp = input("Enter Temperature in 'F: ")
    F = float(inp)
    C = (F-32)*5/9
    print(C)
  except:
    print("Please enter valid temperature")
