inputlines = []
inputline = input()
while(inputline):
  inputlines.append(inputline)
  inputline = input()

n = len(inputlines)//2
for i in range(n,len(inputlines)):
  print(inputlines[i])
for i in range(n):
  print(inputlines[i])
