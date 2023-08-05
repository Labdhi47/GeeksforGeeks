#    A
#   ABA
#  ABCBA
# ABCDCBA

v=65
for row in range(4):
  for col in range(N-1-row):
    print(" ",end="")
  for col in range(row+1):
    print(chr(v+col),end="")
  for col in range(row,0,-1):
    print(chr(v+col-1),end="")
  print()
