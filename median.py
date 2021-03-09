def median3(x,y,z):
  if x <= y:
    if x >= z:
       mymedian = x
  if x >= y and x <= z:
    mymedian = x
  if y <= x and y >= z:
    mymedian = y
  if y >= x and y <= z:
    mymedian = y
  if z <= x and z >= y:
    mymedian = z
  if z >= x and z <= y:
    mymedian = z
  return(mymedian)
