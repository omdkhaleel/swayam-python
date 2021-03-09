inputlines = []
inputline = input()
while(inputline):
  inputlines.append(inputline)
  inputline = input()

for i in range(0,len(inputlines),2):
  print(inputlines[i])
for i in range(1,len(inputlines),2):
  print(inputlines[i])
