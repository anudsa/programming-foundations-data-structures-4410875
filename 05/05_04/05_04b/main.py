#Use a queue to generate the first n binary numbers
from collections import deque
n=6
def decimalToBinary(number):
  binaryNumber = deque()
  if number > 0 :
    quotient=number//2
    remainder=number%2
    binaryNumber.appendleft(remainder)
    while quotient != 0:
      remainder=quotient%2 #reminder is updated first
      binaryNumber.appendleft(remainder)
      quotient= quotient//2 #the quotient is updated bc it's not 0 yet 
  return binaryNumber
#printing unpacked queue
for decimal in range(1,n+1):
  print(*decimalToBinary(decimal)) 